from __future__ import annotations
from typing import TYPE_CHECKING, Any

from pynvim.api import Buffer

if TYPE_CHECKING:
    from .nvim import MyNvim


class MyBuffer(Buffer):
    def __init__(self, nvim: MyNvim, buffer: Buffer):
        self.buf = buffer
        self.nvim = nvim

    def __getattr__(self, attr):
        return getattr(self.buf, attr)

    def set(self, option: str, value: Any):
        self.nvim.api.buf_set_option(self.buf.handle, option, value)
