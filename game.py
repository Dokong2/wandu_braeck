import pygame
import threading
import pickle

class data():
    def lanksave(data):
        with open("./gamepile/lank.pkl", "wb") as f:
            pickle.dump(data, f)
    def lanklode(data):
        with open("./gamepile/lank.pkl", "rb") as f:
            data = pickle.load(f)
            return data

def start():
    pygame.display