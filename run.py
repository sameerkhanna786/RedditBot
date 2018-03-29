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
import traceback
import miscellaneous
#increase number of actions depending on how much karma the bot currently has

def low_karma(r, counter):
    #for bots with 0 karma or little to no karma
    #will run until the bot reaches 500 karma
    try:
        miscellaneous.run_script(r)
        #Sleep for 1 minute
        time.sleep(60)
        if counter == 10:
            hottest.find_front_comments(r)
    except prawcore.exceptions.Forbidden as e:
        #This occurs when the bot tries to comment on something that it isn't allowed to
        #Print the exception + type and just ignore it
        print(e)
        print(type(e))
        print(traceback.extract_stack())
    except praw.exceptions.APIException as e:
        #This occurs when the bot tries to comment on something that is too old
        #Print the exception + type and just ignore it
        print(e)
        print(type(e))
        print(traceback.extract_stack())
    except Exception as e:
        #catch a rate limit exception
        #cooldown for a little bit so that the bot can run unhindered
        print(e)
        print(type(e))
        print(traceback.extract_stack())
        print ("Need to cooldown for 20 minutes.")
        print ("Will auto-start after cooldown period.")
        #Let praw cooldown for 20 minutes
        time.sleep(1200)
        
        #Relogin in case the exception was due to a dissconnect issue.
        r = miscellaneous.login()
    return r

def med_karma(r, counter):
    #for bots with relatively little karma
    #will run until the bot reaches 1500 karma
    #decrease waiting time
    try:
        miscellaneous.run_script(r)
        #Sleep for 1 minute
        time.sleep(60)
        if counter == 10:
            hottest.find_front_comments(r)
    except prawcore.exceptions.Forbidden as e:
        #This occurs when the bot tries to comment on something that it isn't allowed to
        #Print the exception + type and just ignore it
        print(e)
    except praw.exceptions.APIException as e:
        #This occurs when the bot tries to comment on something that is too old
        #Print the exception + type and just ignore it
        print(e)
    except Exception as e:
        #catch a rate limit exception
        #cooldown for a little bit so that the bot can run unhindered
        print(e)
        print ("Need to cooldown for 10 minutes.")
        print ("Will auto-start after cooldown period.")
        #Let praw cooldown for 10 minutes
        time.sleep(600)
        
        #Relogin in case the exception was due to a dissconnect issue.
        r = miscellaneous.login()
    return r

def high_karma(r, counter):
    #for bots with decent amount karma
    #will run after bot reaches 1500 karma
    # have no sleeping time unless rate-limit exception occurs
    try:
        miscellaneous.run_script(r)
        #Sleep for 1 minute
        time.sleep(60)
        if counter == 10:
            hottest.find_front_comments(r)
    except prawcore.exceptions.Forbidden as e:
        #This occurs when the bot tries to comment on something that it isn't allowed to
        #Print the exception + type and just ignore it
        print(e)
    except praw.exceptions.APIException as e:
        #This occurs when the bot tries to comment on something that is too old
        #Print the exception + type and just ignore it
        print(e)
    except Exception as e:
        #catch a rate limit exception
        #cooldown for a little bit so that the bot can run unhindered
        print(e)
        print ("Need to cooldown for 5 minutes.")
        print ("Will auto-start after cooldown period.")
        #Let praw cooldown for 5 minutes
        time.sleep(300)
        
        #Relogin in case the exception was due to a dissconnect issue.
        r = miscellaneous.login()
        counter = 0
    return r
            
miscellaneous.get_saved_comments()
r = miscellaneous.login()
counter = 0
while True:
    user = r.user.me()
    karma = user.comment_karma + user.link_karma
    if karma <= 500:
        r = low_karma(r, counter)
    elif karma <= 1500:
        r = med_karma(r, counter)
    else:
        r = high_karma(r, counter)
    if counter == 10:
        counter = 0
    else:
        counter = counter + 1
