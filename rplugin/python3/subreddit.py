from mypynvim.nvim import MyNvim
from enum import Enum
from praw import Reddit


class TimeFilter(Enum):
    HOUR = "hour"
    DAY = "day"
    WEEK = "week"
    MONTH = "month"
    YEAR = "year"
    ALL = "all"


class SortBy(Enum):
    HOT = "hot"
    NEW = "new"
    TOP = "top"
    CONTROVERSIAL = "controversial"
    RISING = "rising"


class SubredditNvim:
    def __init__(
        self,
        reddit: Reddit,
        nvim: MyNvim,
        subreddit_name: str = "neovim",
        sort_by: str = "top",
        time_filter: str = "week",
        limit: int = 25,
    ):
        self.reddit = reddit
        self.nvim = nvim
        self.parameters = {
            "name": subreddit_name,
            "sort_by": SortBy(sort_by),
            "time_filter": TimeFilter(time_filter),
            "limit": int(limit),
        }
        self.fetched_posts = []

    def fetch(self):
        subreddit = self.reddit.subreddit(self.parameters["name"])
        sort_methods = {
            SortBy.HOT: subreddit.hot,
            SortBy.NEW: subreddit.new,
            SortBy.RISING: subreddit.rising,
            SortBy.CONTROVERSIAL: subreddit.controversial,
            SortBy.TOP: subreddit.top,
        }
        sort_args = {"limit": self.parameters["limit"]}
        if self.parameters["sort_by"] in [SortBy.TOP, SortBy.CONTROVERSIAL]:
            sort_args["time_filter"] = self.parameters["time_filter"].value
        self.fetched_posts = sort_methods[self.parameters["sort_by"]](**sort_args)

    def run(self):
        self.fetch()
        for post in self.fetched_posts:
            self.nvim.notify(post.title)
