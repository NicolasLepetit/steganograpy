class Message:
    def __init__(self, message: str = ''):
        self._message = message

    def __repr__(self):
        return f'Message({self._message})'

    def __str__(self):
        return f'Message({self._message})'

    @property
    def message(self):
        return self._message

    def bytesLength(self):
        return len(self._message)

    def binaryLength(self):
        return 8*self.bytesLength()