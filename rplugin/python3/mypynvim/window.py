from __future__ import annotations
from typing import TYPE_CHECKING

from pynvim.api import Window
from .buffer import MyBuffer

if TYPE_CHECKING:
    from .nvim import MyNvim


class MyWindow(Window):
    def __init__(self, nvim: MyNvim, window: Window):
        self.win = window
        self.nvim = nvim

    def __getattr__(self, attr):
        return getattr(self.win, attr)

    def set_buf(self, buf: MyBuffer):
        self.nvim.win_set_buf(self.win.handle, buf.buf)
