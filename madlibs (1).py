#12/9/24
#functions
def madLibs():
    print("""Welcome to Mad Libs!
          Enter the prompted type of word to fill in the story!
          The theme of the story is The Race""")
    animal1= input("Animal:")
    adjective = input("Adjective:")
    animal2 = input("Different Animal:")
    skill = input("Skill:")
    print("A "+animal1+" mocked a "+adjective+"-moving "+animal2+" and challenged him to a race. Confident in his "+skill+" skills, the "+animal1+" took a nap midway, while the "+animal2+" kept going steadily. When the "+animal1+" woke up, the "+animal2+" was almost at the finish line, and despite his "+skill+" skills, the "+animal1+" couldn't catch up in time.")
#main
madLibs()
