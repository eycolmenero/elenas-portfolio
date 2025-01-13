print("Who is your super character?")
print("Answer the following questions to find out your superhero!")
ans=input("hero(h) or villian(v)?")
if ans =="h":
    ans=input("day(d) or night(n)?")
    if ans == "d":
        ans=input("silver(s) or gold(g)?")
        if ans == "s":
            print("You're Captain America!")
        else:
            print("You're Iron Man!")
    if ans == "n":
        ans=input("black(bk) or blue(bl)?")
        if ans == "bk":
            print("You're Batman!")
        else:
            print("You're Superman!")
if ans =="v":
    ans=input("sunrise(sr) or sunset(ss)?")
    if ans == "sr":
        ans=input("white(w) or green(g)?")
        if ans == "g":
            print("You're Poison Ivy")
        else:
            print("You're Scarlett Witch")
    if ans == "ss":
        ans=input("red(r) or purple(p)?")
        if ans == "r":
            print("You're Harley Quinn!")
        else:
            print("You're The Jonkler!-Why so serious?")
