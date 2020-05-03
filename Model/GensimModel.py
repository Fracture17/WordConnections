from Model.Model import Model

import gensim.downloader as api


class GensimModel(Model):
    def __init__(self, name):
        super().__init__()

        self.model = api.load(name)

    def similarity(self, a: str, b: str):
        s = self.model.similarity(a, b)
        return s


def gloveSimilarity(model, a, b):
    return model.similarity(a, b)


def makeGloveWikiGiga50():
    model = GensimModel("glove-wiki-gigaword-50")
    return model

def makeGloveWikiGiga100():
    model = GensimModel("glove-wiki-gigaword-100")
    return model

def makeGloveWikiGiga200():
    model = GensimModel("glove-wiki-gigaword-200")
    return model

def makeGloveWikiGiga300():
    model = GensimModel("glove-wiki-gigaword-300")
    return model

def makeFastTextModel():
    model = GensimModel("fasttext-wiki-news-subwords-300")
    return model

def makeTwitterModel25():
    model = GensimModel("glove-twitter-25")
    return model

def makeTwitterModel50():
    model = GensimModel("glove-twitter-50")
    return model

def makeTwitterModel100():
    model = GensimModel("glove-twitter-100")
    return model

def makeTwitterModel200():
    model = GensimModel("glove-twitter-200")
    return model

def makeGoogleModel():
    model = GensimModel("word2vec-google-news-300")
    return model