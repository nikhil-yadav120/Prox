from instapy import InstaPy
user = input("Enter username: ")
pass1 = input("Enter password: ")
session = InstaPy(username=user, password=pass1)
session.login()
