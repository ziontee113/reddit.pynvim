import pynvim
from mynvim import MyNvim
from split import Split


@pynvim.plugin
class RedditNvimPlugin(object):
    def __init__(self, nvim: pynvim.Nvim):
        self.nvim = nvim
        self.mynvim = MyNvim(nvim)

    @pynvim.command("RedditPynvim")
    def just_testing(self):
        win = self.nvim.current.window
        buf = self.nvim.current.buffer

        split = Split(mynvim=self.mynvim, nvim=self.nvim, win=win, buf=buf)
        split.test_notify()
