import ConfigParser
import getopt
import os
import sys
import time
import queue
import twitter

api = twitter.Api(consumer_key='mqU6iYHbfYetiwdW3U0jjRyeh',
                  consumer_secret='8N50IWJZ8a5DNguK7KNftjtudd6y5T3PgSIpoVf8BoqCjT3iLQ' ,
                  access_token_key='830602856348647424-pJu8aqCJ8FGf4egQMehjxDZOuZoURhZ',
                  access_token_secret='X6rqtfBFt1WZ7HxpVIsOJHSqVJdGqzcfV2jGF0fMpTG20')
                  
try:
    q = queue.Queue()
    q.put(556366535)
    
    while (not q.empty()):
        
        new_id = q.get()
        
        status = api.GetFollowerIDs(user_id=new_id, screen_name=None, cursor=None, stringify_ids=False, count=None, total_count=None)
    
        for each in status:
            q.put(each)
            try:
                api.CreateFriendship(user_id=each, screen_name=None, follow=True)
                print 'Followed ' + str(each)
                time.sleep(6)
            except twitter.error.TwitterError:
                print "Follow didn't work."
        
        to_unfollow = api.GetFriends()
        to_unfollow.reverse()
        for i in range(0, 4):
            time.sleep(20)
            api.DestroyFriendship(user_id=to_unfollow[i].AsDict()['id'], screen_name=None)
            print 'Unfollowed ' + str(to_unfollow[i].AsDict()['id'])
        
    
except UnicodeDecodeError:
    print "Your message could not be encoded.  Perhaps it contains non-ASCII characters? "
    print "Try explicitly specifying the encoding with the --encoding flag"
    sys.exit(2)