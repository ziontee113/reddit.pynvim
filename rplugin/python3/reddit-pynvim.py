import os

from dotenv import load_dotenv
import praw

import pynvim
from mypynvim.nvim import MyNvim
from renderers import SubredditRenderer

# instantiate Reddit instance
load_dotenv()
reddit = praw.Reddit(**os.environ)


# register plugin
@pynvim.plugin
class RedditNvimPlugin(object):
    def __init__(self, nvim: pynvim.Nvim):
        self.nvim = MyNvim(nvim)

    @pynvim.command("RedditPynvim")
    def reddit_pynvim(self):
        split = self.nvim.split("v")
        split.new_buffer("markdown")

        subreddit_name = "neovim"
        limit = 20
        time_filter = "week"

        subreddit = reddit.subreddit(subreddit_name)
        top_submissions = subreddit.top(limit=limit, time_filter=time_filter)

        renderer = SubredditRenderer(self.nvim, split.buf, top_submissions)
        renderer.render()
