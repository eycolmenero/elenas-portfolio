#Elena Colmenero
#init
# List of Tetris scores
largestNum=0
lowestNum=100000000000000
scoreList = [
    3600460, 1388900, 5435960, 4222920, 8063900, 1362703, 6529560, 2043580, 1390000, 1696224,
    1372600, 2535840, 2605320, 2275996, 11966100, 1472600, 1390780, 1768400, 1333731, 1317580,
    1777456, 4899280, 2790920, 1626880, 1476400, 29486164, 4570640, 1649100, 4890220, 6492500,
    1614120, 5157860, 1582980, 1357480, 2382340, 1532660, 2378832, 1316520, 2529080, 13793540,
    1386260, 1352620, 1442340, 1406260, 1705680, 12409180, 2281848, 3222400, 1349060, 2302480,
    1571120, 3067100, 3740500, 1606732, 2153480, 2011360, 1344740, 1371060, 1345420, 2373940,
    1702940, 2077552, 2108820, 1322485, 1404800, 2555620, 1405580, 4213540, 3835120, 6563440,
    1350742, 1537800, 1657560, 1333995, 1632505, 2743060, 1509751, 1554880, 1316540, 1323680,
    2433160, 1340460, 1659860, 1608500, 7220241, 1834120, 7081880, 1483360, 16700760, 1435280,
    1702640, 1371040, 1316900, 2114180, 1374100, 1412260, 1379220, 1319573, 1623160, 6787420
]
#functions
#shows user highest score
def highestScore():
    global largestNum
    for number in scoreList:
        if number >= largestNum:
            largestNum = number
    return (largestNum)
#shows user lowest score
def lowestScore():
    global lowestNum
    for number in scoreList:
        if number <= lowestNum:
            lowestNum = number
    return(lowestNum)
#shows user average score
def averageScore():
    total = 0
    for i in range(len(scoreList)):
        total = total + scoreList[i]
    total = total/100
    print(total)
#allows user to add new score
def newScore():
    new=input("Please enter a score: ")
    new = int(new)
    if new > highestScore():
        print("Wow you got the newest high score!")
        scoreList.append(new)
        scoreList.remove(lowestScore())
    elif new > lowestScore():
        print("Score added!")
        scoreList.append(new)
        scoreList.remove(lowestScore())
    elif new <= lowestScore():
        print("Sorry, score could not be added!")
#puts all functions together
def tetrisAnalysis():
    print("Welcome to Tetris Analyzer!")
    while True:
        print("Please choose an option!")
        print("1. See Highest Score")
        print("2. See Lowest Score")
        print("3. See Average Score")
        print("4. Add New Score")
        print("5. Quit")
        option = int(input("1-5: "))
        if option == 1:
            highestScore()
            print(highestScore())
        elif option == 2:
            lowestScore()
            print(lowestScore())
        elif option == 3:
            averageScore()
        elif option ==4:
            newScore()
        elif option==5:
            print("Thank you for using Tetris Analyzer!")
            break
#main
tetrisAnalysis()
