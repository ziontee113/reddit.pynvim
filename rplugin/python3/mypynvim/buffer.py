from __future__ import annotations
from typing import TYPE_CHECKING

from pynvim.api import Buffer

if TYPE_CHECKING:
    from .nvim import MyNvim


class MyBuffer(Buffer):
    def __init__(self, nvim: MyNvim, buffer: Buffer):
        self.buf = buffer
        self.nvim = nvim

    def __getattr__(self, attr):
        return getattr(self.buf, attr)
