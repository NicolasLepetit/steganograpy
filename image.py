from PIL import Image
import numpy as np

class inputImage:
    def __init__(self, file_path: str = ''):
        self._file_path = file_path
        try:
            self._img = np.array(Image.open(self._file_path))
        except NameError:
            print(f'Can not open {self._file_path}')

    def __repr__(self):
        return f'inputImage({self._file_path})'

    def __str__(self):
        return f'inputImage({self._file_path})'

    def image_info(self):
        return f'image: {self._file_path}, shape: {self._img.shape}, size: {self._img.size}'

    @property
    def file_path(self)->str:
        return self._file_path

    @property
    def img(self)->np.ndarray:
        return self._img