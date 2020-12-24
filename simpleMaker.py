from maker import imageMaker
from PIL import Image

class simpleMaker(imageMaker):
    def make(self):
        bin = ''.join(f'{ord(c):08b}' for c in self._message.message)
        if len(bin) > self._inputImage.size():
            print('The input message is too long for this image')
        else:
            print('Processing')
            for index, tmp_b in enumerate(bin):
                pixel_value_bin = f'{self._new_image[index]:08b}'
                new_pixel_value_bin = pixel_value_bin[:-1] + tmp_b
                self._new_image[index] = int(new_pixel_value_bin, 2)

    def new_Image(self):
        tmp = self._new_image.reshape(self._inputImage.img.shape)
        pil_image = Image.fromarray(tmp)
        pil_image.save('test.png')