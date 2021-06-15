from instapy import InstaPy

session = InstaPy(username="nikhilyadav3844", password="yadavnikhil**")
session.login()

session.like_by_tags(["business","adventure","fashion"], amount=10)

session.set_do_follow(True, percentage=25)

session.set_do_comment(True, percentage=50)
session.set_comments("Nice Post!", "Love It!", "Spectacular Post!")

session.end()

