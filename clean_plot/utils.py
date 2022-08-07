# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_utils.ipynb.

# %% auto 0
__all__ = ['get_data', 'load_pmi', 'loader', 'foo', 'normalize']

# %% ../nbs/00_utils.ipynb 1
import pickle
import numpy as np
from pathlib import Path
from fastcore.foundation import L
from fastcore.xtras import globtastic
import pathlib
import glob
from glob import glob

# %% ../nbs/00_utils.ipynb 2
def get_data(
    fname: (str, pathlib.Path) # path to the file
    )->str: # returns content of the file
    "Reads from a txt file"
    with open(fname, 'r') as f:
        all_text = f.read()
    return all_text

# %% ../nbs/00_utils.ipynb 3
def load_pmi(
    fname: (str, Path)  # name of pmi file
) -> np.ndarray:  # pmi matrix
    """
    Loads the PMI matrix
    """
    file_ = loader(fname, '.npy')
    pmi = np.load(file_)
    print(f'Loaded {name}')
    return pmi

# %% ../nbs/00_utils.ipynb 4
def loader(
    path: [str, pathlib.Path],  # path to a given folder,
    extension: str,  # extension of the file you want
) -> L:  # returns `L`
    "Given a Path and an extension, returns all files with the extension in the path"
    files = L([Path(f) for f in globtastic(path, file_glob=f'*{extension}')])

    return files

# %% ../nbs/00_utils.ipynb 5
def foo(
    x: int,  # num
) -> int:  # returns num
    "returns num itself"
    return x

# %% ../nbs/00_utils.ipynb 6
def normalize(
    data: np.ndarray,  # input array
) -> np.ndarray:  # normalized array
    """
    Given an input array, return normalized array
    """
    return (data - np.min(data)) / (np.max(data) - np.min(data))
