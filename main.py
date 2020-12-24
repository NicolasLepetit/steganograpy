from argparse import ArgumentParser
from image import inputImage
from message import Message
from simpleMaker import simpleMaker

__author__ = 'Nicolas.L'
__version__ = "0.0.0"
__date__ = '12/2020'
module_name = 'SteganograPy: a Python module to hide Messages in Images'


def main():
    parser = ArgumentParser(description=f'{module_name} ({__version__})')
    parser.add_argument('-v', '--version', action='version', version=f'(v{__version__} made on {__date__})', help='Display version of SteganograPy')
    parser.add_argument('--image', '-i',  dest="image", help='Path to image file', default='')
    parser.add_argument('--message', '-m', dest="message", help='Message to hide', default='')
    args = parser.parse_args()
    new_img = simpleMaker(inputImage(args.image), Message(args.message))
    new_img.make()
    new_img.new_Image()
if __name__ == '__main__':
    main()