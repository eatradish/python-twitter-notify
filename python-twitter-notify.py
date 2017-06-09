import time
import twitter
import notify2
import json
import urllib

api = twitter.Api(consumer_key='consumer_key',
                      consumer_secret='consumer_secret',
                      access_token_key='access_token',
                      access_token_secret='access_token_secret')
a = 0
notify2.init("twitter@mention")
while True:
    mentions = api.GetMentions()
    if a != mentions[0]:
        b = json.loads(str(mentions[0]))
        urllib.request.urlretrieve('https://twitter.com/' + b['user']['screen_name'] + '/profile_image?size=bigger', os.path.abspath('.') + '/twitter-notify.jpg')
        twitter_notify = notify2.Notification(b['user']['screen_name'], b['text'], os.path.abspath( '.') + '/twitter-notify.jpg'
        twitter_notify.show()
        a = mentions[0]
    time.sleep(15)
