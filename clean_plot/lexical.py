# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/03_lexical.ipynb (unless otherwise specified).

__all__ = ['interpolate', 'load_pmi', 'load_dictionary', 'write_to_file_lexical', 'process_v2']

# Cell
#all_slow
import re
from clean_plot import *
import os
import unidecode
from collections import OrderedDict
from fastcore.all import *

# Cell
def interpolate(lex, removed_indices = []):
    """
    Method does interpolation based on the removed indices.
    Substitutes the missing values based on the previous value in the array
    """
    for index in removed_indices:
        if index < len(lex):
            lex = np.insert(lex, index, lex[index - 1])
    return lex

# Cell
def load_pmi(path):
    pmi = np.load(path)
    return pmi


# Cell
def load_dictionary(path):
    fname = open(path, 'rb')
    data = pickle.load(fname)
    return data

# Cell
def write_to_file_lexical(sentences, fname):
    with open(fname[:-4]+'_lexical.txt', 'w') as f:
        for line in sentences:
            f.write(line + '\n')
    f.close()

# Cell
def process_v2(fname):
    all_data = get_data(fname)
    all_data = unidecode.unidecode(all_data)
    sentences = make_sentences(all_data)
    clean_sentences = []
    removed_sentences = []
    for i, sentence in enumerate(sentences):
        t = remove_punc_clean(sentence)
        if len(t) > 0:
            clean_sentences.append(t)
        else:
            removed_sentences.append(i)

    write_to_file_lexical(clean_sentences, fname)
    print('Done processing', fname)
    return removed_sentences