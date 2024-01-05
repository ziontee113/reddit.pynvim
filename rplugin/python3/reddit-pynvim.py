import os

from dotenv import load_dotenv
import praw

import pynvim
from mypynvim.nvim import MyNvim
from subreddit import SubredditNvim

# instantiate Reddit instance
load_dotenv()
reddit = praw.Reddit(**os.environ)


# register plugin
@pynvim.plugin
class RedditNvimPlugin(object):
    def __init__(self, nvim: pynvim.Nvim):
        self.nvim = MyNvim(nvim)
        self.nvim._mapping_command = "RedditPynvimMapping"

    @pynvim.command("RedditPynvim", nargs="*")
    def reddit_pynvim(self, args):
        subreddit_instance = SubredditNvim(reddit, self.nvim, *args)
        subreddit_instance.run()

        # split = self.nvim.split("v")
        # split.new_buffer("markdown")
        #
        # split.buf.map(
        #     "subreddit_browser",
        #     "n",
        #     "o",
        #     lambda: (
        #         self.nvim.notify("nobody"),
        #         self.nvim.notify("but you"),
        #     ),
        # )
        # split.buf.map("subreddit_browser", "n", "q", ":q<CR>")
        #
        # subreddit_name = "neovim"
        # limit = 20
        # time_filter = "week"
        #
        # subreddit = reddit.subreddit(subreddit_name)
        # top_submissions = subreddit.top(limit=limit, time_filter=time_filter)
        #
        # renderer = SubredditRenderer(self.nvim, split.buf, top_submissions)
        # renderer.render()

    @pynvim.command("RedditPynvimMapping", nargs="*")
    def my_command(self, args):
        if len(args) == 2:
            context, mapping = args
            self.nvim.mapper.execute(context, mapping)
        if len(args) == 3:
            context, mapping, bufnr = args
            self.nvim.mapper.execute(context, mapping, bufnr)
