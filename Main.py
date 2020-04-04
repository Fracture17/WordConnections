import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QGridLayout, QDialog, QFrame, QRadioButton, QButtonGroup, QSizePolicy, QLineEdit
from random import shuffle
import gensim.downloader as api
from nltk.corpus import wordnet as wn


class Model:
    def __init__(self, model, similarityFunc):
        self.model = model
        self.similarityFunc = similarityFunc

    def similarity(self, a, b):
        return self.similarityFunc(self.model, a, b)


class Display(QDialog):
    def __init__(self, parent, words, model=None):
        super().__init__()

        self.wordDisplays = []
        self.iterationsRemaining = 10
        self.wordLayout = None
        self.words = words
        self.suggestion = None
        self.makeDisplay()
        self.setWords(words)
        self.model = model

    def getSuggestion(self):
        self.iterationsRemaining -= 1
        self.save()
        self.suggestionBox.setText('')
        self.setWords(self.words)
        if self.iterationsRemaining <= 0:
            self.done(0)

    def save(self):
        with open('connections.txt', 'a') as file:
            suggestion = self.suggestionBox.text().lower()
            for x in self.wordDisplays:
                word = x.word.lower()
                score = x.getScore()
                file.write(f'{suggestion} {word} {score}\n')

    def makeDisplay(self):
        layout = QGridLayout(self)

        for r in range(5):
            for c in range(5):
                label = WordDisplay(self, '')
                self.wordDisplays.append(label)
                layout.addWidget(label, r, c)

        self.suggestionBox = QLineEdit(self, placeholderText='Enter Word')
        layout.addWidget(self.suggestionBox, 5, 0)

        confirmationButton = QPushButton(self, text='Confirm')
        confirmationButton.clicked.connect(self.getSuggestion)
        layout.addWidget(confirmationButton, 5, 1)

        compareButton = QPushButton(self, text='Compare')
        compareButton.clicked.connect(self.compareToModel)
        layout.addWidget(compareButton, 5, 2)

        self.setLayout(layout)

    def setWords(self, words):
        for i, word in enumerate(words):
            self.wordDisplays[i].reset(word)

    def compareToModel(self):
        if self.model is None:
            return

        suggestion = self.suggestionBox.text().lower()
        for display in self.wordDisplays:
            similarity = self.model.similarity(suggestion, display.word.lower())
            display.modelSimilarity.setText(str(similarity))


class WordDisplay(QFrame):
    def __init__(self, parent, word):
        super().__init__(parent)

        self.word = word

        self.makeDisplay()

        self.reset(word)

    def reset(self, word):
        self.wordLabel.setText(word)
        self.buttons[0].setChecked(True)
        self.word = word

    def makeDisplay(self):
        layout = QGridLayout(self)

        wordLabel = QLabel(self)
        self.wordLabel = wordLabel
        font = wordLabel.font()
        font.setPointSize(32)
        font.setBold(True)
        wordLabel.setFont(font)
        layout.addWidget(wordLabel, 0, 0, 1, 6)
        layout.setMargin(10)

        group = QButtonGroup(self)
        self.group = group

        self.buttons = []

        for i in range(4):
            scoreButton = QPushButton(self, text=str(i))
            scoreButton.setCheckable(True)
            if i == 0:
                scoreButton.setChecked(True)
            scoreButton.setMaximumWidth(40)
            group.addButton(scoreButton, i)
            layout.addWidget(scoreButton, 1, i)
            self.buttons.append(scoreButton)

        self.modelSimilarity = QLabel(self, text='')
        layout.addWidget(self.modelSimilarity, 2, 0)

        self.setLayout(layout)

    def getScore(self):
        score = int(self.group.checkedButton().text())
        return score / 3


def getRandomWords(n):
    words = getWordPool()
    shuffle(words)
    words = words[:n]
    return [word[:-1] for word in words]


def getWordPool():
    with open('game_wordpool.txt', 'r') as file:
        words = file.readlines()
    return words


def makeDisplay(model=None):
    words = getRandomWords(25)
    x = Display(app, words, model)
    x.show()
    return x


def gloveSimilarity(model, a, b):
    return model.similarity(a, b)


def wordnetSimilarity(model, a, b):
    best = -float('inf')
    bestWords = ''
    for x in model.synsets(a):
        if x.name().split('.')[0] == a:
            for y in model.synsets(b):
                #if y.name().split('.')[0] == b:
                try:
                    similarity = x.wup_similarity(y)
                    if similarity is None:
                        similarity = y.wup_similarity(x)
                    if similarity > best:
                        best = similarity
                        bestWords = x.name() + ", " + y.name()
                except:
                    pass
    return f"{best:.4}  {bestWords}"

#model = api.load("glove-wiki-gigaword-50")
#model = Model(model, gloveSimilarity)

model = Model(wn, wordnetSimilarity)

app = QApplication(sys.argv)
x = makeDisplay(model)
sys.exit(app.exec_())