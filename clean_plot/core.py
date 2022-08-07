# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_core.ipynb.

# %% auto 0
__all__ = ['get_data', 'load_pmi', 'load_dictionary', 'loader']

# %% ../nbs/00_core.ipynb 3
import pickle
import numpy as np
from pathlib import Path
from fastcore.foundation import L

# %% ../nbs/00_core.ipynb 4
from typing import Callable, Iterator, Union, Optional, List
import pathlib
import glob
from glob import glob

# %% ../nbs/00_core.ipynb 6
def get_data(fname: Union[str, pathlib.Path]) -> str:
    """
    Reads from a txt file
    """
    with open(fname, 'r') as f:
        all_text = f.read()
    return all_text

# %% ../nbs/00_core.ipynb 7
def load_pmi(fname: Union[str, pathlib.Path]) -> np.ndarray:
    """
    Loads the PMI matrix
    """
    file_ = loader(fname, '.npy')
    pmi = np.load(file_)
    print(f'Loaded {name}')
    return pmi


# %% ../nbs/00_core.ipynb 8
def load_dictionary(fname):
    """
    Given a fname, function loads a `pkl` dictionary
    from the current directory

    Args:
        fname ([str]): Enter the filename

    Returns:
        [dict]: Returns the loaded pkl file as a
                dict
    """
    fname = open(fname, 'rb')
    data = pickle.load(fname)
    return data

# %% ../nbs/00_core.ipynb 9
def loader(path: Union[str, pathlib.Path], extension: str) -> Union[None, L]:
    """
    Given a Path and an extension, returns all files with the extension in the path
    """
    #`Note` Recursive not supported yet
    p = Path(path)
    files = L()
    for file_ in p.glob(f'*{extension}'):
        files.append(file_)
    
    if files == []:
        print(f'Directory does not contain files ending in {extension}')
        return
    
    return files
    
    
    
