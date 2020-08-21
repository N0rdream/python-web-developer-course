from nltk import pos_tag


def is_verb(word):
    if not word:
        return False
    tags = ['VB', 'VBZ', 'VBN', 'VBG', 'VBD', 'VBP']
    pos_info = pos_tag([word])
    return pos_info[0][1] in tags

def is_noun(word):
    if not word:
        return False
    tags = ['NN', 'NNP', 'NNS']
    pos_info = pos_tag([word])
    return pos_info[0][1] in tags