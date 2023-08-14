import os
import numpy as np
from sklearn.model_selection import train_test_split

directory = 'data/raw'

songs = []

for filename in os.scandir(directory):
    if filename.is_file():
        songFile = open(filename.path, "r")
        songData = songFile.read()
        songsFromFile = songData.split('\n')
        songs += songsFromFile

songsFormatted = []
for song in songs:
    songsFormatted += ["<<bst>>" + song + "<<est>>"]

train, eval = train_test_split(songsFormatted)

np.savetxt("data/train.csv", train, delimiter=",", fmt='%s', encoding="UTF-8")
np.savetxt("data/eval.csv", eval, delimiter=",", fmt='%s', encoding="UTF-8")
