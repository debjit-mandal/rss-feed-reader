import feedparser
print ('Enter the URL: ')
url = input()
feed = feedparser.parse(url)
try:
    title = feed['feed']['title']
    print(title)

except:
    print('error')
for item in feed['entries']:
    print (item['title']+ "\n" + item['link']+"\n" + item['description']+"\n")
