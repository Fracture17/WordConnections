from collections import defaultdict

from Model.Model import Model


class TruthModel(Model):
    def __init__(self, path: str):
        super().__init__()

        self.model = defaultdict(dict)
        self._pairs = []

        with open(path, 'r') as file:
            for line in file:
                a, b, connection = line[:-1].split()
                self._pairs.append((a, b))
                connection = float(connection)
                self.model[a][b] = connection
                self.model[b][a] = connection

    def similarity(self, a: str, b: str):
        return self.model[a][b]

    def pairs(self):
        return self._pairs
