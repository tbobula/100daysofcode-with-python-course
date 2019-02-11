from collections import namedtuple
from pprint import pprint

import feedparser

# cached version to have predictable results for testing
FEED_URL = "http://bit.ly/2IkFe9B"

Game = namedtuple('Game', 'title link')

def get_games():
    """Parses Steam's RSS feed and returns a list of Game namedtuples"""
    game_list = []
    feeds = feedparser.parse(FEED_URL)
    for feed in feeds['entries']:
        entry = Game(feed['title'], feed['link'] )
        game_list.append(entry)
    return game_list

get_games()