#Code forked from ReplyBot.py by /u/GoldenSights

'''USER CONFIGURATION'''

USERNAME  = ""
#This is the bot's Username. In order to send mail, he must have some amount of Karma.
PASSWORD  = ""
#This is the bot's Password. 
USERAGENT = ""
#This is a short description of what the bot does. For example "/u/GoldenSights' Newsletter bot"
SUBREDDIT = "GoldTesting"
#This is the sub or list of subs to scan for new posts. For a single sub, use "sub1". For multiple subreddits, use "sub1+sub2+sub3+..."
PARENTSTRING = ["phrase 1", "phrase 2", "phrase 3", "phrase 4"]
#These are the words you are looking for
REPLYSTRING = "Hi hungry, I'm dad"
#This is the word you want to put in reply
MAXPOSTS = 100
#This is how many posts you want to retrieve all at once. PRAW can download 100 at a time.
WAIT = 20
#This is how many seconds you will wait between cycles. The bot is completely inactive during this time.


print "Starting WouldReadAgainBot"
print "Loading libraries"
import traceback
import praw # simple interface to the reddit API, also handles rate limiting of requests
import time
'''All done!'''

print "Logging in"
r = praw.Reddit(USERAGENT)
r.login(USERNAME, PASSWORD) 
print "Done!"

def scanSub():
    print "Searching "+ SUBREDDIT
    subreddit = r.get_subreddit(SUBREDDIT)
    posts = subreddit.get_comments(limit=MAXPOSTS)
    firstpost = null
    for post in posts:
        pid = post.id
        if firstpost == null: firstpost = pid
        if pid == lastpost: break
        try:
            pauthor = post.author.name #will throw an error if comment is deleted, so that we can ignore the post
            pbody = post.body.lower()
            if any(key.lower() in pbody for key in PARENTSTRING):
                if pauthor.lower() != USERNAME.lower():
                    print('Replying to ' + pid + ' by ' + pauthor)
                    parentid = post.parent_id
                    if parentid.split(_)[0] == 't1': #if the parent is also a comment
                        parent = r.get_info(thing_id=parentid)
                        parentbody = parent.body.split( )[:50]
                        replytext = "Here you go!\n >"+parentbody+"\n I'm a bot"
                        #post.reply(replytext)
                        print replytext
                else:
                    print "Will not reply to self"
        except AttributeError:
            #Author is deleted. We don't care about this
            pass
    lastpost = firstpost

lastpost = null
while True:
    try:
        scanSub()
    except Exception as e:
        traceback.print_exc()
    print('Running again in %d seconds \n' % WAIT)
    time.sleep(WAIT)

    
