from pynvim.api import Buffer


class MyBuffer(Buffer):
    def __init__(self, buffer: Buffer):
        self.buf = buffer

    def __getattr__(self, attr):
        return getattr(self.buf, attr)
