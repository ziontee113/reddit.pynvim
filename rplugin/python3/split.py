from mynvim import MyNvim
import pynvim


class Split:
    def __init__(self, nvim: pynvim.Nvim, mynvim: MyNvim):
        self.nvim = nvim
        self.mynvim = mynvim
