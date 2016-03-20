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
            words.insert(len(words), ln[len(start):].strip())
    if len(words) > 0:
        return words
    else:
        return None

def bot_reply(c, words):
    reply = ""
    for ln in words:
        term = ln.replace(" ", "%20")
        req = json.load(urllib2.urlopen("http://api.urbandictionary.com/v0/define?term=" + term))["list"]
        reply += "[**" + ln + "**](https://www.urbandictionary.com/define.php?term=" + term + ")\n\n"
        if len(req) > 0:
            defn = req[0]
            reply += defn["definition"] + '\n\n*' + defn["example"] + '*\n\n'
        else:
            reply += "No definitions found! How about you [submit one](https://www.urbandictionary.com/?modal_url=%2Fadd.modal.php)?\n\n"
        reply += "---\n"
    reply += "^(I'm a bot! Check out /r/ud_bot for info.)"
    c.reply(reply)

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