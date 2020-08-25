from random import randint

print("The Game : "
      "\n1. Choose Difficulty Level According To Your Capability."
      "\n2. Enter The Name of The Card In The Format ('Face' of 'Suit')."
      "\n   For Example: 7 of Spades"
      "\n3.If The Right Face/Suit Is Guessed, Continue To Enter The Card Name In Full."
      "\n  For Example: If Card Is '7 of Spades' And Guess Is '7 of Hearts', Enter '7 of Spades' In your Next Turn."
      "\n4.Guess The Right Card In The Chosen Number Of Moves"
      "\n5.Good Luck!!!\n\n")

d = int(input("Enter The Number Of Moves You Want : "))


class Cards:
    def __init__(self):
        pass

    def card_gen(self):
        # card = "none"
        n = randint(1, 13)
        m = randint(1, 4)
        lst = [n, m]
        return lst


c = Cards()
f = c.card_gen()

if f[0] == 1:
    num = "Ace"
elif f[0] == 11:
    num = "Jack"
elif f[0] == 12:
    num = "Queen"
elif f[0] == 11:
    num = "King"
else:
    num = f[0]

if f[1] == 1:
    face = "Hearts"
elif f[1] == 2:
    face = "Spades"
elif f[1] == 3:
    face = "Clubs"
elif f[1] == 4:
    face = "Diamonds"
guess = ""
card = f"{num} of {face}"
cardl = card.split(" ")
guess = ["__", "of", "__"]
# print(f"Guess The Card {guess[0]} of {guess[2]} ")
# print(card)
for i in range(d + 1):
    if guess == cardl:
        print(f"YAY!! The card was {card} indeed")
        break
    if i == 0:
        continue
    else:
        print("Your Guess : ", end="")
        for j in guess:
            print(j, end=" ")
        print()
    n = input("Enter The Card Name (face of suit): ")
    n = n.split(" ")
    n[0] = n[0].capitalize()
    n[2] = n[2].capitalize()
    # print(n)
    if n[0] == cardl[0]:
        print("You got the Face right!!")
        guess[0] = n[0]
    else:
        print("You got the Face wrong!!")

    if n[2] == cardl[2]:
        print("You got the Suit right!!")
        guess[2] = n[2]
    else:
        print("You got the Suit wrong!!")
else:
    print(f"OOPS!! You Lost. The Card Was {card}")
# for i in range(10):
#     if cardl[0] == "9":
#         print(True)
#     else:
#         print(False)
