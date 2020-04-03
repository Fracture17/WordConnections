import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QGridLayout, QDialog, QFrame, QRadioButton, QButtonGroup, QSizePolicy, QLineEdit
from random import shuffle


class Display(QDialog):
    def __init__(self, parent, words):
        super().__init__()

        self.wordDisplays = []
        self.iterationsRemaining = 10
        self.wordLayout = None
        self.words = words
        self.suggestion = None
        self.makeDisplay()
        self.setWords(words)

    def getSuggestion(self):
        self.iterationsRemaining -= 1
        self.save()
        self.suggestionBox.setText('')
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

        self.setLayout(layout)

    def setWords(self, words):
        for i, word in enumerate(words):
            self.wordDisplays[i].reset(word)


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

        for i in range(6):
            scoreButton = QPushButton(self, text=str(i))
            scoreButton.setCheckable(True)
            if i == 0:
                scoreButton.setChecked(True)
            scoreButton.setMaximumWidth(40)
            group.addButton(scoreButton, i)
            layout.addWidget(scoreButton, 1, i)
            self.buttons.append(scoreButton)

        self.setLayout(layout)

    def getScore(self):
        score = int(self.group.checkedButton().text())
        return score / 5


def getRandomWords(n):
    words = getWordPool()
    shuffle(words)
    words = words[:n]
    return [word[:-1] for word in words]


def getWordPool():
    with open('game_wordpool.txt', 'r') as file:
        words = file.readlines()
    return words


def makeDisplay():
    words = getRandomWords(25)
    x = Display(app, words)
    x.show()
    return x


app = QApplication(sys.argv)
x = makeDisplay()
sys.exit(app.exec_())