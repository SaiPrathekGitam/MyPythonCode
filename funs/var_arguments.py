# Program to create a function that takes a mandatory message followed by names of the persons


def msgname(msg, *names):
    print(f"Message = {msg}")
    for i in names:
        print(f"Name = {i}")
