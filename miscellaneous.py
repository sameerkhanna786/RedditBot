import praw
import prawcore
import config
import time
import os
import requests
import pronouncing
import random
import upsidedown
import hottest
import delete

def login():
    print("Logging in!")
    r = praw.Reddit(username = config.username,
                password = config.password,
                client_id = config.client_id,
                client_secret = config.client_secret,
                user_agent = "Sameer Khanna's demo reddit bot v1.0")
    print("Logged in!")
    return r

def get_saved_comments():
    if os.path.isfile("replied_comments.txt"):
        comment_replied = []
        with open("replied_comments.txt", "r") as input:
            comment_replied = input.read()
            comment_replied = comment_replied.split("\n")
            comment_replied = filter(None, comment_replied)
        return comment_replied
    else:
        return []

def run_script(r):
    for comment in r.subreddit("all").stream.comments(pause_after=-1):
        delete.delete(r)
        if comment == None:
            continue
        comment_replied = get_saved_comments()
        if comment.archived != True:
            if "!chucknorrisjoke" in comment.body:
                print("Joke will be done")
                joke(r, comment, comment_replied)
            if "!hibot" in comment.body:
                print("Hi will be done")
                reply(r, comment, comment_replied)
            if "!rhyme" in comment.body:
                print("Rhyme will be done")
                try:
                    rhyme(r, comment, comment_replied)
                except:
                    print("Ignoring as rhyme was the last word")
            if "!upside-down" in comment.body:
                print("UpsideDown will be done")
                upside_down(r, comment, comment_replied)
            if "!upside down" in comment.body:
                print("UpsideDown will be done")
                upside_down(r, comment)
            if "!upsidedown" in comment.body:
                print("UpsideDown will be done")
                upside_down(r, comment)

def joke(r, comment, comment_replied):
    #Check that we have not already replied to this comment
    if comment.id in comment_replied:
        return
    #Now, check to make sure we are not replying to ourselves!
    elif comment.author == r.user.me():
        return
    #We can safely reply to this comment!
    else:
        reply =  "You have requested a Chuck Norris joke via the secret command! Here ya go:\n\n"
        joke = requests.get("http://api.icndb.com/jokes/random").json()['value']['joke']
        reply += ">" + joke
        reply += "\n\n" + "This joke came from [ICNDb.com](https://icndb.com/)!\n\n"
        reply += "Say hi to me by typing !hibot\n\n"
        reply += "Normal use: Type rhyme followed by a word you wish to rhyme!\n\n"
        reply += "Secret commands: To hear a Chuck Norris joke, comment !chucknorrisjoke anywhere in this subreddit!\n\n"
        reply += "Another command: To make your text !upside-down, say upside-down anywhere in your text!"
        comment.reply(reply)
        #Now write this comment to our text file so we dont
        #reply to it in our next run
        with open("replied_comments.txt", "a") as output:
            output.write(comment.id + "\n")

def reply(r, comment, comment_replied):
    #Check that we have not already replied to this comment
    if comment.id in comment_replied:
        return
    #Now, check to make sure we are not replying to ourselves!
    elif comment.author == r.user.me():
        return
    #We can safely reply to this comment!
    else:
        reply = "Hello!\n\n"
        reply += "This was an automated response.\n\n"
        reply += "Feel free to give suggestions too!\n\n"
        reply += "Say hi to me by typing !hibot\n\n"
        reply += "Normal use: Type !rhyme followed by a word you wish to rhyme! \n\n"
        reply += "Secret command: To hear a Chuck Norris joke, comment !chucknorrisjoke anywhere in this subreddit!\n\n"
        reply += "Another command: To make your text !upside-down, say upside anywhere in your text!"
        comment.reply(reply)              
        #Now write this comment to our text file so we dont
        #reply to it in our next run
        with open("replied_comments.txt", "a") as output:
            output.write(comment.id + "\n")

def rhyme(r, comment, comment_replied):
    #Check that we have not already replied to this comment
    if comment.id in comment_replied:
        return
    #Now, check to make sure we are not replying to ourselves!
    elif comment.author == r.user.me():
        return
    #We can safely reply to this comment!
    else:
        words = comment.body.split()
        index = 0
        for word in words:
            if "rhyme" in word:
                break
            index = index + 1
        rhyme_word = words[index + 1]
        rhymes = pronouncing.rhymes(rhyme_word)
        reply = ""
        if len(rhymes) > 0:
            reply += rhyme_word + " rhymes with " + random.choice(rhymes)
            reply += "\n\n"
            reply += "Thank you so much for using me!\n\n"
            reply += "Say hi to me by typing !hibot\n\n"
            reply += "Normal use: Type rhyme followed by a word you wish to rhyme!\n\n"
            reply += "Secret commands: To hear a Chuck Norris joke, comment !chucknorrisjoke anywhere in this subreddit!\n\n"
            reply += "Another command: To make your text !upside-down, say upside-down anywhere in your text!"
            comment.reply(reply)                     
            #Now write this comment to our text file so we dont
            #reply to it in our next run
            with open("replied_comments.txt", "a") as output:
                output.write(comment.id + "\n")

def upside_down(r, comment, comment_replied):
    #Check that we have not already replied to this comment
    if comment.id in comment_replied:
        return
    #Now, check to make sure we are not replying to ourselves!
    elif comment.author == r.user.me():
        return
    #We can safely reply to this comment!
    else:
        reply = "You activated a secret function of mine!\n\n"
        reply += "By saying upside-down, I will make your text BE upside down! Enjoy!\n\n"
        reply += ">" + upsidedown.flip(comment.body) + "\n\n"
        reply += "This bot is made to learn how to use APIs better; please give any feedback you deem fit.\n\n"
        reply += "Say hi to me by typing !hibot\n\n"
        reply += "Normal use: Type rhyme followed by a word you wish to rhyme!\n\n"
        reply += "Secret commands: To hear a Chuck Norris joke, comment !chucknorrisjoke anywhere in this subreddit!\n\n"
        reply += "Another secret command: To make your text !upside-down, say upside-down anywhere in your text!"
        comment.reply(reply)                   
        #Now write this comment to our text file so we dont
        #reply to it in our next run
        with open("replied_comments.txt", "a") as output:
            output.write(comment.id + "\n")
