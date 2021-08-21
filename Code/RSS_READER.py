"""Quick attempt, not functional"""
import feedparser
Feed = feedparser.parse("https://www.moretonbay.qld.gov.au/feed.rss?listname=MBRC%20News")
print('Number of RSS posts :'), len(Feed.entries)

entry = Feed.entries[1]
print('Post Title :'), entry.title