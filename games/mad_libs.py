# Mad Libs!!!

choice = int(input("Enter A Number Between 1 And 10 : "))


def one():
    color = input("Enter a color: ")
    pluralNoun = input("Enter a plural noun: ")
    celebrity = input("Enter a celebrity: ")

    print("Roses are", color)
    print(pluralNoun + " are blue")
    print("I love", celebrity)


if choice == 1:
    one()
