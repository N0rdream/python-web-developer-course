import sys
import argparse


def get_cmd_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--app',
        type=str,
        help='Path to Blueberry instance. For example: "my_app.app".'
    )
    return parser.parse_args()


def get_instance(path):
    if path is None:
        sys.exit('Missing path to Blueberry instance.')
    try:
        module_name, instance_name = path.split('.')
    except ValueError:
        sys.exit('Invalid input. Expected "my_app.app" format.')
    __import__(module_name)
    module = sys.modules[module_name]
    return getattr(module, instance_name)