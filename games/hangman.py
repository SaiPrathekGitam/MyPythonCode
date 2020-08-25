def cls():
    print("\n" * 50)


movie = ""  # Enter movie before running
gmovie = []
guess = ""
chance = 1
glist = []
n = 10
win = 0

man = (
    """
    -----
    |   |
    |
    |
    |
    |
    |
    |
    |
    --------
    """,
    """
    -----
    |   |
    |   0
    |
    |
    |
    |
    |
    |
    --------
    """,
    """
    -----
    |   |
    |   0
    |  -+-
    |
    |
    |
    |
    |
    --------
    """,
    """
    -----
    |   |
    |   0
    | /-+-
    |
    |
    |
    |
    |
    --------
    """,
    """
    -----
    |   |
    |   0
    | /-+-\ 
    |
    |
    |
    |
    |
    --------
    """,
    """
    -----
    |   |
    |   0
    | /-+-\ 
    |   | 
    |
    |
    |
    |
    --------
    """,
    """
    -----
    |   |
    |   0
    | /-+-\ 
    |   | 
    |   | 
    |
    |
    |
    --------
    """,
    """
    -----
    |   |
    |   0
    | /-+-\ 
    |   | 
    |   | 
    |  |
    |
    |
    --------
    """,
    """
    -----
    |   |
    |   0
    | /-+-\ 
    |   | 
    |   | 
    |  | 
    |  | 
    |
    --------
    """,
    """
    -----
    |   |
    |   0
    | /-+-\ 
    |   | 
    |   | 
    |  | | 
    |  | 
    |
    --------
    """,
    """
    -----
    |   |
    |   0
    | /-+-\ 
    |   | 
    |   | 
    |  | | 
    |  | | 
    |
    --------
    """)


def hang(ch):
    if ch is 1:
        print(man[1])
    if ch is 2:
        print(man[2])
    if ch is 3:
        print(man[3])
    if ch is 4:
        print(man[4])
    if ch is 5:
        print(man[5])
    if ch is 6:
        print(man[6])
    if ch is 7:
        print(man[7])
    if ch is 8:
        print(man[8])
    if ch is 9:
        print(man[9])
    if ch is 10:
        print(man[10])


def vowels():
    checkm = 'AaEeIiOoUu '
    global win
    for i in range(len(movie)):
        if movie[i] in checkm and movie[i] != " ":
            gmovie.insert(i, movie[i])
            print(movie[i], end="")
            glist.append(movie[i])
            win += 1
        elif movie[i] == " ":
            glist.append(movie[i])
            win += 1
            gmovie.insert(i, "/")
            print("/", end="")
        else:
            gmovie.insert(i, "_")
            print("_", end="")
        print(" ", end="")


def check(name):
    global win
    for i in range(len(movie)):
        if name in movie[i]:
            gmovie.insert(i, movie[i])
            gmovie.pop(i + 1)
            if name not in glist:
                win += 1


print("Guess The Letters In The Movie ", end=" ")
vowels()

guess = input(f"\n\nChance Number 1 : ")
while chance < n:
    if guess in movie:
        check(guess)
        if len(movie) == win:
            print(f"YAY! The Movie Was '{movie}' indeed")
            break
        elif guess in glist:
            print(f"The Letter '{guess}' Is Already In The Movie ", end=" ")
        else:
            print(f"The Letter '{guess}' Is In The Movie ", end=" ")
        hang(chance)
        for l in range(len(gmovie)):
            print(gmovie[l], end=" ")
        print()

        glist.append(guess)
        guess = input(f"Chance Number {chance} : ")
    else:
        glist.append(guess)
        print(f"Sorry!Guess Again.{n - chance} chances left")
        chance += 1
        hang(chance)
        guess = input(f"Chance Number {chance} : ")

else:
    print(f"Sorry! The Movie Was '{movie}'")
