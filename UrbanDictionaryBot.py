import urllib2
import json
import praw

start = "/u/ud_bot "

# Checks if a commenter wants help from ud_bot
# if they start a line with @ud_bot, everything
# else on that line will be parsed as a UD query
def wants_def(c):
    lines = c.body.split('\n')
    words = []
    defSeen = False
    for ln in lines:
        ln = ln.strip()
        if ln[:len(start)] == start:
            words.insert(len(words), ln[len(start):])
    if len(words) > 0:
        return words
    else:
        return None

def bot_reply(c, words):
    for ln in words:
        print ln
        term = "yeltsin"
        term = term.replace(" ", "%20")
        req = json.load(urllib2.urlopen("http://api.urbandictionary.com/v0/define?term=" + term))["list"]
        #if len(req) > 0:
            #print req[0]
        #else:
            #print "No results found!"

def main():
    username, password = open("login.txt").read().split('\n')
    r = praw.Reddit("Urban Dictionary Bot by /u/officialdovahkiin")
    r.login(username, password, disable_warning=True)

    for c in praw.helpers.comment_stream(r, 'all'):
        words = wants_def(c)
        if words is not None:
            bot_reply(c, words)

if __name__ == '__main__':
    main()