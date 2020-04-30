from Model.Model import Model

import gensim.downloader as api


class GensimModel(Model):
    def __init__(self, name):
        super().__init__()

        self.model = api.load(name)

    def similarity(self, a: str, b: str):
        return self.model.similarity(a, b)


def gloveSimilarity(model, a, b):
    return model.similarity(a, b)


def makeGloveWikiGiga50():
    model = GensimModel("glove-wiki-gigaword-50")
    return model
