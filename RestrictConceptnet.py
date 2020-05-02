from gensim.models import KeyedVectors
import gensim.downloader as api
import numpy as np


def restrict(model: KeyedVectors):
    new_vectors = []
    new_vocab = {}
    new_index2entity = []
    new_vectors_norm = []

    for i in range(len(model.vocab)):
        if i % 10000 == 0:
            print(i)
        word = model.index2entity[i]
        vec = model.vectors[i]
        vocab = model.vocab[word]
        vec_norm = model.vectors_norm[i]
        if word.startswith('/c/en/') and '_' not in word:
            word = word[6:]
            vocab.index = len(new_index2entity)
            new_index2entity.append(word)
            new_vocab[word] = vocab
            new_vectors.append(vec)
            new_vectors_norm.append(vec_norm)

    model.vocab = new_vocab
    model.vectors = np.array(new_vectors)
    model.index2entity = np.array(new_index2entity)
    model.index2word = np.array(new_index2entity)
    model.vectors_norm = np.array(new_vectors_norm)


model = api.load("conceptnet-numberbatch-17-06-300")
print(model.most_similar('/c/en/test'))
restrict(model)
print(len(model.vectors))
print(model['test'])
print(model.most_similar('test'))
model.save_word2vec_format("Culled-Conceptnet")
