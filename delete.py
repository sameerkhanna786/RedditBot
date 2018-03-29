#delete comments the bot makes that are not liked; do not want to have a negative impact on Reddit
def delete(r):
    User = r.user.me()
    comments = User.comments.new()
    for c in comments:
        if c.score <= 0:
            c.edit("#")
            c.delete()
