import pathlib

import pyglottography


class Dataset(pyglottography.Dataset):
    dir = pathlib.Path(__file__).parent
    id = "walker2011bayesian"
