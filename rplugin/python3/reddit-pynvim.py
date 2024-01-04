import pynvim
from mypynvim.nvim import MyNvim


@pynvim.plugin
class RedditNvimPlugin(object):
    def __init__(self, nvim: pynvim.Nvim):
        self.nvim = MyNvim(nvim)

    @pynvim.command("RedditPynvim")
    def reddit_pynvim(self):
        split = self.nvim.split("v")
        split.buf.append("# Hello World!")
