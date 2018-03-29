# Find the hottest post right now and congratulate the user.
import praw
import config
import time
import os
import requests
import pronouncing
import random
import upsidedown

def get_saved_submissions():
    if os.path.isfile("replied_submissions.txt"):
        submission_replied = []
        with open("replied_submissions.txt", "r") as input:
            submission_replied = input.read()
            submission_replied = submission_replied.split("\n")
            submission_replied = filter(None, submission_replied)
        return submission_replied
    else:
        return []

def find_front_comments(reddit):
    submission_replied = get_saved_submissions()
    print(submission_replied)
    for submission in reddit.subreddit('all').hot(limit=None):
        if not (submission.id in submission_replied):
            reply = "Congrats on your post making it to the hottest 100 on the front page!\n\n"
            reply += "This is an automated message.\n\n"
            reply += "Say hi to me by typing !hibot\n\n"
            reply += "Normal use: Type rhyme followed by a word you wish to rhyme!\n\n"
            reply += "Secret commands: To hear a Chuck Norris joke, comment !chucknorrisjoke anywhere in this subreddit!\n\n"
            reply += "Another command: To make your text upside-down, say upside-down anywhere in your text!"
            submission.reply(reply)
    
            with open("replied_submissions.txt", "a") as output:
                output.write(submission.id + "\n")
