# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/00_utils.ipynb (unless otherwise specified).

__all__ = ['get_data', 'load_pmi', 'loader', 'foo', 'normalize']

# Cell
import pickle
import numpy as np
from pathlib import Path
from fastcore.foundation import L
from fastcore.xtras import globtastic
import pathlib
import glob
from glob import glob

# Cell
def get_data(
    fname: (str, pathlib.Path) # path to the file
    )->str: # returns content of the file
    "Reads from a txt file"
    with open(fname, 'r') as f:
        all_text = f.read()
    return all_text

# Cell
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

# Cell
def loader(
    path: [str, pathlib.Path],  # path to a given folder,
    extension: str,  # extension of the file you want
) -> L:  # returns `L`
    "Given a Path and an extension, returns all files with the extension in the path"
    files = L([Path(f) for f in globtastic(path, file_glob=f'*{extension}')])

    return files

# Cell
def foo(
    x: int,  # num
) -> int:  # returns num
    "returns num itself"
    return x

# Cell
def normalize(
    data: np.ndarray,  # input array
) -> np.ndarray:  # normalized array
    """
    Given an input array, return normalized array
    """
    return (data - np.min(data)) / (np.max(data) - np.min(data))