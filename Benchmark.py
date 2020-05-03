from Model.Model import Model
from Model.TruthModel import TruthModel
from Model.WordnetModel import makeWordnetModel
from Model.GensimModel import *
from Model.EnsembleModel import EnsembleModel
from Model.ConceptModel import makeConceptnetModel
from itertools import combinations
from Model.MaxEnsambleModel import MaxEnsembleModel


def benchmark(truth: TruthModel, pred: Model):
    score = 0
    empty = 0
    for (a, b) in truth.pairs():
        try:
            x = truth.similarity(a, b)
            y = pred.similarity(a, b)
            score += calcError(x, y)
        except:
            empty += 1

    score /= (len(truth.pairs()) - empty)
    return score, len(truth.pairs()) - empty, empty


def calcError(truth, pred):
    return abs(truth - pred)


def runAll(models: list, names: list):
    truth = TruthModel('connections.txt')
    with open('EnsambleResults.txt', 'w') as file:
        for i in range(len(models)):
            m = range(len(models))
            for x in combinations(m, r=i + 1):
                ensamble = EnsembleModel([models[j] for j in x])
                score = benchmark(truth, ensamble)
                print(', '.join([names[j] for j in x]))
                print(score)
                file.write(', '.join([names[j] for j in x]) + '\n')
                file.write(str(score) + "\n")


def runAllMax(models: list, names: list):
    truth = TruthModel('connections.txt')
    with open('MaxEnsambleResults.txt', 'w') as file:
        for i in range(len(models)):
            m = range(len(models))
            for x in combinations(m, r=i + 1):
                ensamble = MaxEnsembleModel([models[j] for j in x])
                score = benchmark(truth, ensamble)
                print(', '.join([names[j] for j in x]))
                print(score)
                file.write(', '.join([names[j] for j in x]) + '\n')
                file.write(str(score) + "\n")


runAllMax([makeGoogleModel(), makeGloveWikiGiga300(), makeTwitterModel200()], ['google', 'glove', 'twitter'])
#pred = makeGloveWikiGiga200()

#x = benchmark(truth, pred)

#print(x)