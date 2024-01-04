from __future__ import annotations
from typing import Optional


class Split:
    import mypynvim.nvim

    def __init__(self, nvim: "mypynvim.nvim.MyNvim"):
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
