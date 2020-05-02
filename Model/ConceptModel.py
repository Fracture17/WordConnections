from Model.Model import Model

from gensim.models import KeyedVectors


class ConceptnetModel(Model):
    def __init__(self):
        super().__init__()

        self.model = KeyedVectors.load_word2vec_format("Culled-Conceptnet")

    def similarity(self, a: str, b: str):
        return self.model.similarity(a, b)


def gloveSimilarity(model, a, b):
    return model.similarity(a, b)


def makeConceptnetModel():
    model = ConceptnetModel()
    return model
