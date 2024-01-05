from rplugin.python3.mypynvim.nvim import MyNvim
from enum import Enum


class SubredditTimeFilter(Enum):
    HOUR = "hour"
    DAY = "day"
    WEEK = "week"
    MONTH = "month"
    YEAR = "year"
    ALL = "all"


class SortSubredditBy(Enum):
    HOT = "hot"
    NEW = "new"
    TOP = "top"
    CONTROVERSIAL = "controversial"
    RISING = "rising"


class SubredditNvim:
    def __init__(
        self,
        nvim: MyNvim,
        subreddit_name: str,
        sort_by: str = "TOP",
        time_filter: str = "WEEK",
        limit: int = 25,
    ):
        self.nvim = nvim
        self.subreddit_instance_info = {
            "name": subreddit_name,
            "sort_by": SortSubredditBy[sort_by].value,
            "time_filter": SubredditTimeFilter[time_filter].value,
            "limit": limit,
        }
