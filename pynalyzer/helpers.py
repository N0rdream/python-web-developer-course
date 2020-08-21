import os


def get_filepaths(path, ext):
    for dirpath, dirs, files in os.walk(path, topdown=True):
        for file in files:
            if file.endswith(ext):
                yield os.path.join(dirpath, file)

def get_words_from_snake_case(phrase):
    return (word for word in phrase.split('_') if word)