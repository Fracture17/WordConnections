from Model.Model import Model


class EnsembleModel(Model):
    def __init__(self, models: list):
        super().__init__()

        self.models = models

    def similarity(self, a: str, b: str):
        similarities = []
        for model in self.models:
            similarities.append(model.similarity(a, b))
        return sum(similarities) / len(self.models)
