import sys
from Model.GensimModel import makeGloveWikiGiga50
from PySide2.QtWidgets import QApplication
from Display import makeDisplay


model = makeGloveWikiGiga50()

app = QApplication(sys.argv)
x = makeDisplay(model)
sys.exit(app.exec_())
