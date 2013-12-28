#!/usr/bin/python -tt

import pickle

def save(_object, path):
    pickle.dump(_object, path, 2)
