import random
def story():
    print("Hi there this little program will randomly show you your motor racing story.")
    name = input("So first of all what is your name?")
    print("Here is your racing career:")
    print("\t", name,"'s career\n")
    karting()
    f2()
    f1()
    f1betterteam()
    future()

def karting():
    fate = random.randint(1,5)

    if fate == 1:
        print("You had a terrible carting career you have never got into bigger racing")
        exit()
    else:
        print("You had a great carting career and you have moved onto better series like Formula-4")
        print("You went all the way up to Formula-2")
        return

def f2():
    fate = random.randint(1,3)
    
    if fate == 1:
        print("You had won the Formula-2 championship by a big margin and you have definitely piqued some Formula-1 teams interest")
        return
    elif fate == 2:
        print("You came fourth in Formula-2 and no F1 team offered you contract so you tried again in F2")
        f2()
    elif fate == 3:
        print("You had a lot of crashes but you ended in the middle field at 10th place")
        print("No F1 and F2 team offered you contract so you went back to Formula-3 but you couldn't deliver any preformance so you were kicked out")
        print("You went to a university learned and got a job outside of racing")
        exit()

def f1():
    teams = ["Alpine","Mclaren","Haas","Williams","Alfa Romeo","AlphaTauri"]
    print("You start your Formula-1 career at ",teams[random.randint(0,len(teams)-1)])

    fate = random.randint(1,4)
    if fate == 1:
        print("You had a great start as a rookie you had beaten your teammate and you were avoiding crashes")
        print("Because of this preformance you stay one more year at that team and you had the same preformance")
        print("You had got the chance to move to a better team")
        return
    elif fate == 2:
        print("You have had some crashes you couldn't beat your teammate but you were close to him")
        print("You've got a second chance from your team")
        secondchace()
        f1()
    elif fate == 3:
        print("You had a lot of crashes but because of your parents money you can stay one more year")
        secondchace()
        f1()
    elif fate == 4:
        print("You had a lot of crashes and you showed terrible driving so you couldn't get a second chance in F1")
        print("You moved back to F2 and you will drive there until the end of your career")
        exit()

def secondchace():
    fate = random.randint(1,3)
    if fate == 1:
        print("You had a great second year and you finally beaten your teammate")
        print("Because of this preformance you stay one more year at that team and you had the same preformance")
        print("You had got the chance to move to a better team")
        return
    elif fate == 2:
        print("You had the same preformace as before so you stay at the team for some years but then a rookie replaces you and you will drive at F2 forever")
        exit()
    elif fate == 3:
        print("You had a terribble second year you were kicked out of the team and you're passion fades for racing and choose to be in a another career")
        exit()

def f1betterteam():
    teams = ["Red Bull","Mercedes","Ferrari","Aston Martin"]
    team = teams[random.randint(0,len(teams)-1)]
    print("You got a contract for ",team)
    print("Turns out ",team," has the best car on the grid")

    fate = random.randint(1,3)
    if fate == 1:
        print("You had a great season you just missed the championship win by a little and hope that next year you can win it")
        nextyear(team)
        return
    elif fate == 2:
        print("You've came 4th in the championship stay with ",team)
        nextyear(team)
        return
    elif fate == 3:
        print("You had a lot of crashes the team drops you and you couldn't get a seat for next year")
        print("You went back to F2 and you will drive there until the end of your career")
        exit()

def nextyear(team):
    fate = random.randint(1,3)
    if fate == 1:
        print("You had won the Formula-1 championship!!!!")
        print("Stay with your team and you will see what the future holds for you")
        return
    elif fate == 2:
        print("You couldn't beat your teammate again and you stay the second driver in the team until you retire")
        exit()
    elif fate == 3:
        print("You couldn't meet the expectation of your team but a lot of team is interested in you")
        newteam(team)

def newteam(team):
    teams = ["Alpine","Mclaren","Haas","Williams","Alfa Romeo","AlphaTauri","Red Bull","Mercedes","Ferrari","Aston Martin"]
    teams.remove(team)
    newteam = teams[random.randint(0,len(teams)-1)]
    print("You get a contract for ",newteam)
    print("You will drive for them until you retire but you will not win a championship with them")
    exit()

def future():
    fate = random.randint(1,2)

    if fate == 1:
        print("You won a astonishing 5 championship with your team and retire after your 5th win to be with your family")
        exit()
    elif fate == 2:
        print("You became/stayed the second driver in the team and after yopu got replaced you retired to be with you family")
        exit()

def main():
    story()

main()
