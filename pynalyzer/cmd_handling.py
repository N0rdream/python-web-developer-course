import argparse


def get_cmd_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--url',
        type=str,
        help='Github link'
    )
    parser.add_argument(
        '--path',
        type=str,
        help='Code directory'
    )
    parser.add_argument(
        '--lang',
        type=str,
        default='python',
        help='Language'
    )
    parser.add_argument(
        '--fast',
        type=str,
        default='fnames',
        choices=['vnames', 'fnames'],
        help='Part of code'
    )
    parser.add_argument(
        '--pos',
        type=str,
        default='verbs',
        choices=['verbs', 'nouns'],
        help='Part of speech'
    )
    parser.add_argument(
        '--out',
        type=str,
        default='console',
        choices=['console', 'csv', 'json'],
        help='Output format'
    )
    return parser.parse_args()