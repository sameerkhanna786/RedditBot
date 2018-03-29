import pronouncing
import random

def rhyme(r, comment):
    print "String found in comment " + comment.id
    if comment.id in comment_replied:
        print "Skipping comment; already replied to."
    #Now, check to make sure we are not replying to ourselves!
    #elif comment.author == r.user.me():
        #print "Skipping; this is our own comment!"
    else:
        words = comment.body.split()
        index = 0
        for word in words:
            if "!rhyme" in word:
                break
            index = index + 1
        rhyme_word = words[index + 1]
        rhymes = pronouncing.rhymes(rhyme_word)
        if len(rhymes) > 0:
            reply = rhyme_word + " rhymes with " + random.choice(rhymes)
            reply += "\nThank you so much for using me!\n"
            reply += "Say hi to me by typing !hibot\n"
            reply += "Normal use: Type !rhyme followed by a word you wish to rhyme!\n"
            reply += "Secret command: To hear a Chuck Norris joke, comment !chucknorrisjoke anywhere in this subreddit!"

            comment.reply(reply)
            #Mark this comment as replied to!
            comment_replied.append(comment.id)
            print "Comment" + comment.id + " replied to!"
                        
            #Now write this comment to our text file so we dont
            #reply to it in our next run
            with open("replied_comments.txt", "a") as output:
                output.write(comment.id + "\n")
