import sys
from Model.Model import Model
from Model.WordnetModel import WordnetModel
from PySide2.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QGridLayout, QDialog, QFrame, QRadioButton, QButtonGroup, QSizePolicy, QLineEdit
from Display import makeDisplay, wordnetSimilarity
import gensim.downloader as api
from nltk.corpus import wordnet as wn



#model = api.load("glove-wiki-gigaword-50")
#model = Model(model, gloveSimilarity)

model = WordnetModel()

app = QApplication(sys.argv)
x = makeDisplay(model)
sys.exit(app.exec_())
