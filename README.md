# Welcome to clean_plot
> The library simplifies cleaning text files for creation of embeddings and making plots from it


## Install

`pip install clean-plot`

## How to use

The library contains easy to use methods for cleaning text, tokenizing and lemmatizing sentences. These sentences can then be easily fed to a sentence encoder to create sentence embeddings.

```python
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


```python
sentences = make_sentences(text)
```

```python
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



```python
no_punctuations = []
for sentence in sentences:
    new_sentence = remove_punctuations(sentence)
    no_punctuations.append(new_sentence)
```

```python
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


