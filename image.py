from PIL import Image
import numpy as np


class inputImage:
    def __init__(self, file_path: str = ''):
        self._file_path = file_path

    def __repr__(self):
        return f'inputImage({self._file_path})'

    def __str__(self):
        return f'inputImage({self._file_path})'