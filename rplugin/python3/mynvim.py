from typing import Iterable, Any, Union

import pynvim


class MyNvim:
    def __init__(self, nvim: pynvim.Nvim):
        self.nvim = nvim

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
