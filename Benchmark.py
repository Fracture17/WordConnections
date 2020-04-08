from Model.Model import Model
from Model.TruthModel import TruthModel

from Model.WordnetModel import WordnetModel


def benchmark(truth: TruthModel, pred: Model):
    score = 0
    empty = 0
    for (a, b) in truth.pairs():
        try:
            x = truth.similarity(a, b)
            y = pred.similarity(a, b)
            score += abs(x - y)
        except:
            empty += 1

    score /= (len(truth.pairs()) - empty)
    return score, len(truth.pairs()) - empty, empty


truth = TruthModel('connections.txt')
pred = WordnetModel()

x = benchmark(truth, pred)

print(x)