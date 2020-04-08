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
