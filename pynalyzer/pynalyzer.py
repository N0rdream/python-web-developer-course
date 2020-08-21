import sys
import os
from helpers import get_filepaths, get_words_from_snake_case
from cmd_handling import get_cmd_args
from git import Repo
from collections import Counter
from language_processors import is_verb, is_noun
from itertools import chain
from output_formats import create_csv, create_json
from python_processors import get_tree, get_funcnames_ast, get_varnames_from_funcs_ast


def main():
    
    cargs = get_cmd_args()

    if cargs.path is None:
        sys.exit('Select directory pls.')

    if not os.path.exists(cargs.path):
        sys.exit(f'Directory <{cargs.path}> does not exist.')

    if cargs.url is not None:
        Repo.clone_from(cargs.url, cargs.path)

    if cargs.lang == 'python':
        files = get_filepaths(cargs.path, '.py')
        trees = filter(lambda x: x is not None, map(get_tree, files))
        
        if cargs.fast == 'fnames':
            ast_func = get_funcnames_ast
        if cargs.fast == 'vnames':
            ast_func = get_varnames_from_funcs_ast

        names = chain.from_iterable(map(ast_func, trees))
    else:
        sys.exit('Only python is supported now.')

    names = chain.from_iterable(map(get_words_from_snake_case, names))

    if cargs.pos == 'verbs':
        pos_func = is_verb
    if cargs.pos == 'nouns':
        pos_func = is_noun

    parts = filter(pos_func, names)
    result = Counter(parts)

    if cargs.out == 'console':
        print(result.most_common())
    if cargs.out == 'csv':
        create_csv(result)
    if cargs.out == 'json':
        create_json(result)


if __name__ == '__main__':
    main()















