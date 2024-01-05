import os

from dotenv import load_dotenv
import praw

import pynvim
from mypynvim.nvim import MyNvim

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
        results = subreddit.top(limit=limit, time_filter=time_filter)

        for submission in results:
            split.buf.append(submission.title)
            split.buf.append(submission.url)
            split.buf.append("")
