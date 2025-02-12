import pygame
import cmpt120image as img
#import draw
import random

###############################################################
# Keep this block at the beginning of your code. Use caution before you modify.
# If you want to hardcode to speed up development, you can do so

# For example, set just ENV = "v" if coding in VS Code.
# You'll need to uncomment before submission!

def initEnv():
    print("\nWelcome! Before we start...")
    env = input("Are you using VS Code (v), Replit (r) or IDLE (i)? ").lower()
    while env not in "vri":
        print("Environment not recognized, type again.")
        env = input("Are you using VS Code (V), Replit (r) or IDLE (i)? ").lower()
    print("Great! Have fun!\n")
    env='i'
    return env

# Use the playSound() function below to play sounds. 
# soundfilename does not include the .wav extension, 
# e.g. playSound(apples,ENV) plays apples.wav
def playSound(soundfilename,ENV):
    if ENV == "v" or ENV == "i":
        pygame.mixer.init()
        pygame.mixer.music.load("sounds/"+soundfilename+".wav")
        pygame.mixer.music.play()
    elif env == "r":
        from replit import audio
        audio.play_file("sounds/"+soundfilename+".wav")
ENV = initEnv()
###############################################################

amount= 3
images=[]
with open ('blackfoot.csv','r') as file:
    file.readline()
    for i in file:
        i=i.strip('\n')
        images.append(i)


def mainmenu():
    print('Main Menu')
    print('1. Learn - Word Flashcards')
    print('2. Play - Seek and Find Flashcards')
    print('3. Settings - Change Difficulty')
    print('4. Exit')

def setting(amount):
        print('the current no.of images shown:', amount)
        question=input('would you like to change the amount of images shown? yes(y) or no(n)')
        if question in 'yes':
            amount=int(input('choose the amount of images (number should be between 3 and 12):'))
            while (amount>12) or (amount<3):
                print ('enter a number between 3 and 12')
                amount=int(input('choose the amount of images (number should be between 3 and 12):'))
        else:
            pass

def learn():
    i=0
    while i<=(amount-1):
        photo=images[i]
        my_image = img.get_image("images/"+ photo + ".png")
        canvas=img.get_black_image(350,350)
        draw.distribute_items(canvas,my_image,1)
        img.show_image(canvas)
        playSound(photo,ENV)
        input("Please enter to continue..")
        i+=1
        
    
def play():
    pass
    
def option():
        option=int(input('enter your option no.:'))
        if (option<1) or (option>4):
            print ('enter a correct option no.')
            option=int(input('enter your option no.:'))
        else:
            if option == 3:
                setting(amount)
            elif option==1:
                learn()
            elif option==2:
                play()
            elif option==4:
                exit()
        

while True:
    mainmenu()
    option()
    
 

    
                
        
    

      






