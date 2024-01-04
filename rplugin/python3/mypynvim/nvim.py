from typing import Iterable, Any, Union, Optional

import pynvim
from split import Split

from mypynvim.window import MyWindow
from mypynvim.buffer import MyBuffer


class MyNvim(pynvim.Nvim):
    def __init__(self, nvim: pynvim.Nvim):
        self.nvim = nvim

    def __getattr__(self, attr):
        return getattr(self.nvim, attr)

    # native api methods

    def notify(self, msg: Union[str, Iterable[Any]], level: str = "info"):
        def format_msg(msg):
            if type(msg) is str:
                msg = msg.split("\n")
                msg = str(msg)
                msg = "{" + msg[1:-1] + "}"
            else:
                msg = f"'{msg}'"
            return msg

        formatted_msg = format_msg(msg)
        self.nvim.exec_lua(f"vim.notify({formatted_msg}, '{level}')")

    # custom api methods

    def split(self, direction: str = "v", size: Optional[int] = None) -> Split:
        return Split(self)(direction, size)

    # window methods

    def win(self, winnr: int) -> MyWindow:
        return MyWindow(self.nvim.windows[winnr])

    def current_win(self) -> MyWindow:
        return MyWindow(self.nvim.current.window)

    # buffer methods

    def buf(self, bufnr: int) -> MyBuffer:
        return MyBuffer(self.nvim.buffers[bufnr])

    def current_buf(self) -> MyBuffer:
        return MyBuffer(self.nvim.current.buffer)
