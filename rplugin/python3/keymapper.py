from __future__ import annotations
from typing import TYPE_CHECKING, Union, Callable, Optional

if TYPE_CHECKING:
    from mypynvim.nvim import MyNvim


class Keymapper:
    def __init__(self, nvim: MyNvim):
        self.nvim = nvim
        self._buffer_callback_library = {}

    def buf_set(
        self,
        bufnr: int,
        context: str,
        mode: str,
        lhs: str,
        rhs: Union[str, Callable],
    ):
        if callable(rhs):
            if not context in self._buffer_callback_library:
                self._buffer_callback_library[context] = {}
                self._buffer_callback_library[context][lhs] = {}

            self._buffer_callback_library[context][lhs][str(bufnr)] = rhs
            rhs = f"<cmd>{self.nvim._mapping_command} {context} {lhs} {bufnr}<CR>"

        self.nvim.api.buf_set_keymap(bufnr, mode, lhs, rhs, {"noremap": True})

    def execute(self, context: str, mapping: str, bufnr: Optional[int] = None):
        if bufnr is not None:
            callback = self._buffer_callback_library[context][mapping][bufnr]
            if callable(callback):
                callback()
