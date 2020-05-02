from nltk.corpus import wordnet as wn

from Model.Model import Model


class WordnetModel(Model):
    def __init__(self, similarityFunc=wn.wup_similarity):
        super().__init__()

        self.model = wn

        self.similarityFunc = similarityFunc

    def similarity(self, a: str, b: str):
        a = wn.synsets(a)[0]
        b = wn.synsets(b)[0]
        return self.similarityFunc(a, b)


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


def makeWordnetModel():
    return WordnetModel()