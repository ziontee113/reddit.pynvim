from __future__ import annotations
from typing import TYPE_CHECKING, Any, Union, Callable

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

    def map(self, context: str, mode: str, lhs: str, rhs: Union[str, Callable]):
        self.nvim.mapper.buf_set(self.buf.handle, context, mode, lhs, rhs)
