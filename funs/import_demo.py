def myfun():
    print(f"In {__name__}")


myfun()

if __name__ == "__main__":
    print("Running Module")
else:
    print("Importing Module")
