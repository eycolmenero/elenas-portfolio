#elena colmenero
#import
import random
from PIL import Image
import requests
from io import BytesIO
#functions
#1. The Lego Batman Movie Image and Description Accessed via https://www.imdb.com/title/tt4116284/
#2. The Dark Knight Image and Description Accessed via https://www.imdb.com/title/tt0468569/
#3. Batman vs Superman Image and Description Accessed via https://www.imdb.com/title/tt2975590/
#4. The Batman Image and Description Accessed via https://www.imdb.com/title/tt1877830/
#5. Batman: Under the Red Hood Image and Description Accessed via https://www.imdb.com/title/tt1569923/
batmanmovies = ["https://tinyurl.com/3dfj3k8v", "https://tinyurl.com/mr2ehymh" , "https://tinyurl.com/5h3wk7bm", "https://tinyurl.com/9zzp29dr", "https://tinyurl.com/4ths6rdx"]
def open_image(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img.show()
def randomBatman():
    print("Welcome to random Batman movie generator! Would you like a recommendation for a Batman movie?")
    choice = input("Please type 'Y' for Yes or 'N' for No: ")
    if choice == "Y":
        randomMovie = random.randint(0,4)
        if randomMovie == 0:
            open_image(batmanmovies[0])
            print("A cooler-than-ever Bruce Wayne must deal with the usual suspects as they plan to rule Gotham City, while discovering that he has accidentally adopted a teenage orphan who wishes to become his sidekick.")
        elif randomMovie == 1:
            open_image(batmanmovies[1])
            print("When a menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman, James Gordon and Harvey Dent must work together to put an end to the madness.")
        elif randomMovie == 2:
            open_image(batmanmovies[2])
            print("Batman is manipulated by Lex Luthor to fear Superman. Superman´s existence is meanwhile dividing the world and he is framed for murder during an international crisis. The heroes clash and force the neutral Wonder Woman to reemerge.")
        elif randomMovie == 3:
            open_image(batmanmovies[3])
            print("When a sadistic serial killer begins murdering key political figures in Gotham, the Batman is forced to investigate the city's hidden corruption and question his family's involvement.")
        elif randomMovie == 4:
            open_image(batmanmovies[4])
            print("There's a mystery afoot in Gotham City, and Batman must go toe-to-toe with a mysterious vigilante, who goes by the name of Red Hood. Subsequently, old wounds reopen and old, once buried memories come into the light.")
    if choice == "N":
        print("Thank you for trying!")
#main
randomBatman()
