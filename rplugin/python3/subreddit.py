from rplugin.python3.mypynvim.nvim import MyNvim
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
        subreddit_name: str,
        sort_by: str = "TOP",
        time_filter: str = "WEEK",
        limit: int = 25,
    ):
        self.reddit = reddit
        self.nvim = nvim
        self.parameters = {
            "name": subreddit_name,
            "sort_by": SortBy[sort_by],
            "time_filter": TimeFilter[time_filter],
            "limit": limit,
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
        sort_args = {
            "limit": self.parameters["limit"].get(),
        }
        if self.parameters["sort_by"] in [SortBy.TOP, SortBy.CONTROVERSIAL]:
            sort_args["time_filter"] = self.parameters["time_filter"].get()
        self.fetched_posts = sort_methods[self.parameters["sort_by"]](**sort_args)
