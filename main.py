import feedparser
print ('Enter the URL: ')
url = input()
feed = feedparser.parse(url)
for item in feed['entries']:
    print (item['title']+ "\n" + item['link']+"\n" + item['description']+"\n")
