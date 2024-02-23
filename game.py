import pygame
import threading
import pickle
import os

class data():
    def lanksave(data):
        with open("./gamepile/lank.pkl", "wb") as f:
            pickle.dump(data, f)
    def lanklode():
        with open("./gamepile/lank.pkl", "rb") as f:
            data = pickle.load(f)
            return data

if __name__ == "__main__":
    print(data.lanklode())