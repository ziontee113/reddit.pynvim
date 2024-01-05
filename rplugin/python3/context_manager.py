from __future__ import annotations
from typing import TYPE_CHECKING
from enum import Enum

if TYPE_CHECKING:
    from mypynvim.nvim import MyNvim


class Context(Enum):
    UNINITIALIZED = 0
    SUBREDDIT_BROWSER = 1
    POST_VIEWER = 2


class ContextManager:
    def __init__(self, nvim: MyNvim):
        self.nvim = nvim
        self.context = Context.UNINITIALIZED

    def switch(self, context: Context):
        self.context = context
