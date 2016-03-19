import urllib2
import json
import praw

# Checks if a commenter wants help from ud_bot
# if they start a line with @ud_bot, everything
# else on that line will be parsed as a UD query
def wants_def(c):
    lines = c.body.split('\n')
    for ln in lines:
        ln = ln.strip()
        if ln.startsWith("@ud_bot "):
            return True
    return False

def bot_reply(c):
    term = "yeltsin"
    term = term.replace(" ", "%20")
    req = json.load(urllib2.urlopen("http://api.urbandictionary.com/v0/define?term=" + term))["list"]
    if len(req) > 0:
        print req[0]
    else:
        print "No results found!"

def main():
    username, password = open("login.txt").read().split('\n')
    r = praw.Reddit("Urban Dictionary Bot by /u/officialdovahkiin")
    r.login(username, password, disable_warning=True)

    for c in praw.helpers.comment_stream(r, 'all'):
        if wants_def(c):
            bot_reply(c)

if __name__ == '__main__':
    main()