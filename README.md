# Welcome to clean_plot
> The library simplifies cleaning text files for creation of embeddings and making plots from it


## Install

The easiest way to install the library is to simply do a `pip` install. 

```
pip install clean-plot
```

Another way to install the library would be to build from source. It is more likely that the released version may contain bugs. The source would get updated more often. If you plan to add features to `clean_plot` yourself, or want to be on the cutting edge, you can use an editable install.

```
git clone https://github.com/deven367/clean_plot.git
cd clean_plot
pip install -e . 
```

## How to use

The library contains easy to use methods for cleaning text, tokenizing and lemmatizing sentences. These sentences can then be easily fed to a sentence encoder to create sentence embeddings.

```
fname = '../files/dummy.txt'
text = get_data(fname)
print(text)
```

    MARLEY was dead: to begin with. There is no doubt
    whatever about that. The register of his burial was
    signed by the clergyman, the clerk, the undertaker,
    and the chief mourner. Scrooge signed it: and
    Scrooge's name was good upon 'Change, for anything he
    chose to put his hand to. Old Marley was as dead as a
    door-nail.
    
    Mind! I don't mean to say that I know, of my
    own knowledge, what there is particularly dead about
    a door-nail. I might have been inclined, myself, to
    regard a coffin-nail as the deadest piece of ironmongery
    in the trade. But the wisdom of our ancestors
    is in the simile; and my unhallowed hands
    shall not disturb it, or the Country's done for. You
    will therefore permit me to repeat, emphatically, that
    Marley was as dead as a door-nail.


```
sentences = make_sentences(text)
```

```
sentences
```




    ['MARLEY was dead: to begin with.',
     'There is no doubt whatever about that.',
     'The register of his burial was signed by the clergyman, the clerk, the undertaker, and the chief mourner.',
     "Scrooge signed it: and Scrooge's name was good upon 'Change, for anything he chose to put his hand to.",
     'Old Marley was as dead as a door-nail.',
     'Mind!',
     "I don't mean to say that I know, of my own knowledge, what there is particularly dead about a door-nail.",
     'I might have been inclined, myself, to regard a coffin-nail as the deadest piece of ironmongery in the trade.',
     "But the wisdom of our ancestors is in the simile; and my unhallowed hands shall not disturb it, or the Country's done for.",
     'You will therefore permit me to repeat, emphatically, that Marley was as dead as a door-nail.']



```
no_punctuations = []
for sentence in sentences:
    new_sentence = remove_punctuations(sentence)
    no_punctuations.append(new_sentence)
```

```
no_punctuations
```




    ['MARLEY was dead to begin with',
     'There is no doubt whatever about that',
     'The register of his burial was signed by the clergyman the clerk the undertaker and the chief mourner',
     'Scrooge signed it and Scrooge s name was good upon Change for anything he chose to put his hand to',
     'Old Marley was as dead as a door nail',
     'Mind',
     'I don t mean to say that I know of my own knowledge what there is particularly dead about a door nail',
     'I might have been inclined myself to regard a coffin nail as the deadest piece of ironmongery in the trade',
     'But the wisdom of our ancestors is in the simile and my unhallowed hands shall not disturb it or the Country s done for',
     'You will therefore permit me to repeat emphatically that Marley was as dead as a door nail']



## Contributing

This library has come into existence because of [nbdev](https://nbdev.fast.ai/) (one of many amazing tools made by [fast.ai](https://www.fast.ai/)). PRs and Issues are encouraged. 

After you clone this repository, please run `nbdev_install_git_hooks` in your terminal. This sets up git hooks, which clean up the notebooks to remove the extraneous stuff stored in the notebooks (e.g. which cells you ran) which causes unnecessary merge conflicts.

Before submitting a PR, check that the local library and notebooks match. The script `nbdev_diff_nbs` can let you know if there is a difference between the local library and the notebooks.

If you made a change to the notebooks in one of the exported cells, you can export it to the library with `nbdev_build_lib` or `make clean_plot`.

If you made a change to the library, you can export it back to the notebooks with `nbdev_update_lib`.
