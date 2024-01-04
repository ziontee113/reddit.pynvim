from pynvim.api import Window


class MyWindow(Window):
    def __init__(self, window: Window):
        self.win = window

    def __getattr__(self, attr):
        return getattr(self.win, attr)

    # def set_buf(self, buf: MyBuffer):
    #     self.nvim.win_set_buf(self.win.handle, buf.buf)
