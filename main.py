from argparse import ArgumentParser

__author__ = 'Nico'
__version__ = "0.0.0"
module_name = 'SteganograPy: a Python module to hide messages in images'


def run():
    print('WTF')
    parser = ArgumentParser(description=f'{module_name} (Version {__version__}) made by {__author__}')
    parser.add_argument("--version", help="Display version information.")
    parser.add_argument('--image', action='store', required=True, type=str)



if __name__ == '__main__':
    run()