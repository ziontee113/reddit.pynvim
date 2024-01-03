import pynvim


@pynvim.plugin
class RedditNvimPlugin(object):
    def __init__(self, nvim: pynvim.Nvim):
        self.nvim = nvim

    @pynvim.command("RedditPynvim", nargs="1")
    def copilotChat(self, args: list[str]):
        buf = self.nvim.current.buffer
        # self.nvim.notify("ok reddit.nvim", "info")
        self.nvim.api.nvim_notify("This is a test notification", 1, {})
