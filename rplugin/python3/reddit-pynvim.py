import pynvim
from mynvim import MyNvim
from split import Split


@pynvim.plugin
class RedditNvimPlugin(object):
    def __init__(self, nvim: pynvim.Nvim):
        self.nvim = nvim
        self.mynvim = MyNvim(nvim)

    @pynvim.command("RedditPynvim")
    def reddit_pynvim(self):
        split = Split(mynvim=self.mynvim, nvim=self.nvim)
