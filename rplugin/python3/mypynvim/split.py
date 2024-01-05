from __future__ import annotations
from typing import TYPE_CHECKING, Optional

from mypynvim.buffer import MyBuffer

if TYPE_CHECKING:
    from .nvim import MyNvim


class Split:
    def __init__(self, nvim: MyNvim):
        self.nvim = nvim

    def __call__(self, direction: str = "v", size: Optional[int] = None):
        self.nvim.command("norm! 0")
        self.nvim.command(f"{direction}split")
        if size:
            if direction == "v":
                self.nvim.current.window.width = size
            else:
                self.nvim.current.window.height = size

        self.buf = self.nvim.current_buf()
        return self

    def new_buffer(self, filetype: str = "", restore_cursor: bool = False):
        new_buffer = self.nvim.api.create_buf(False, True)
        self.nvim.api.win_set_buf(self.nvim.current.window.handle, new_buffer)
        self.buf = MyBuffer(self.nvim, new_buffer)
        self.buf.set("filetype", filetype)
        if restore_cursor:
            self.nvim.move_cursor_to_previous_window()
        return self
