# this program asks for the username and password until the user gets it right or has tried too many times
username = "python"
password = "rules"
i = 0

while i <= 4:
    username_tried = input("Give a username: ")
    password_tried = input("Give a password: ")
    if username == username_tried and password_tried == password:
        print("welcome!")
        break
    else:
        print("Access denied.")
    i += 1

