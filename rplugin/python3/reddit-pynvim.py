import os

from dotenv import load_dotenv
import praw

import pynvim
from mypynvim.nvim import MyNvim
from subreddit_instance import SubredditInstance

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
        self.subreddit_instance = SubredditInstance(reddit, self.nvim, *args)
        self.subreddit_instance.run()

    @pynvim.command("RedditPynvimMapping", nargs="*")
    def my_command(self, args):
        if len(args) == 2:
            context, mapping = args
            self.nvim.mapper.execute(context, mapping)
        if len(args) == 3:
            context, mapping, bufnr = args
            self.nvim.mapper.execute(context, mapping, bufnr)
