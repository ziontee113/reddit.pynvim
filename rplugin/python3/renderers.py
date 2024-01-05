from mypynvim.buffer import MyBuffer
from mypynvim.nvim import MyNvim


class SubredditRenderer:
    def __init__(self, nvim: MyNvim, buf: MyBuffer, submissions):
        self.nvim = nvim
        self.buf = buf
        self.submissions = submissions

    def render(self):
        self.buf.clear()
        for submission in self.submissions:
            self.buf.append(submission.title)
            self.buf.append(submission.url)
            self.buf.append("")
