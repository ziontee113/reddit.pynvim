import dataclasses
from typing import Optional

from mynvim import MyNvim
import pynvim
from pynvim.api import Buffer, Window


@dataclasses.dataclass
class Split:
    nvim: pynvim.Nvim
    mynvim: MyNvim
    win: Optional[Window] = dataclasses.field(default=None)
    buf: Optional[Buffer] = dataclasses.field(default=None)

    def test_notify(self):
        self.mynvim.notify(f"Current buffer number: {self.buf.number}")  # type: ignore
        self.mynvim.notify(f"Current window number: {self.win.number}")  # type: ignore
