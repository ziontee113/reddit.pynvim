import pynvim


@pynvim.plugin
class RedditNvimPlugin(object):
    def __init__(self, nvim: pynvim.Nvim):
        self.nvim = nvim

    def notify(self, msg: any):
        def format_msg(msg):
            if type(msg) is str:
                msg = msg.split("\n")
                msg = str(msg)
                msg = "{" + msg[1:-1] + "}"
            else:
                msg = f"'{msg}'"
            return msg

        formatted_msg = format_msg(msg)
        self.nvim.exec_lua(f'vim.notify({formatted_msg}, "info")')

    @pynvim.command("RedditPynvim")
    def just_testing(self):
        self.notify("Hello from Python!")
