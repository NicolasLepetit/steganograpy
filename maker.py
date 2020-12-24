import numpy as np
from image import inputImage
from message import Message


class imageMaker:
    def __init__(self, input_image: inputImage, message: Message):
        self._inputImage = input_image
        self._message = message
        self._new_image = self._inputImage.img.flatten()

    def __repr__(self):
        return f'imageMaker({self._inputImage}, {self._message})'

    def __str__(self):
        return f'imageMaker({self._inputImage}, {self._message})'

    def make(self):
        pass
