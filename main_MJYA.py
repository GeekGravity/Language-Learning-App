#Final Project
#Mathews Jaison - 301576857
#Yogya Agarwal - 301590908
#December 2, 2023


#Importing Modules
import pygame
import cmpt120image as img
import draw
import random

#Welcome message
def initEnv():
    print("\nWelcome! Before we start...")
    env = input("Are you using VS Code (v), Replit (r) or IDLE (i)? ").lower()
    while env not in "vri":
        print("Environment not recognized, type again.")
        env = input("Are you using VS Code (v), Replit (r) or IDLE (i)? ").lower()
    print("Great! Have fun!")
    return env
env = "v"

#Defining the sound play function
def playSound(soundfilename,ENV):
    if ENV == "v" or ENV == "i":
        pygame.mixer.init()
        pygame.mixer.music.load("sounds/"+soundfilename+".wav")
        pygame.mixer.music.play()
    elif env == "r":
        from replit import audio
        audio.play_file("sounds/"+soundfilename+".wav")
ENV = initEnv()

#Initial setup
amount= 3
images=[]
with open ('blackfoot.csv','r') as file:
    names = file.readlines()
    for i in names:
        i=i.strip('\n')
        images.append(i)

#Defining the learn option
def learn():
    global amount
    i=0
    canvas=img.get_white_image(350,350)
    print (images[:amount])
    while i<=(amount-1):
        photo=images[i]
        my_image = img.get_image("images/"+ photo + ".png")
        canvas=draw.distribute_items(canvas,my_image,1)
        img.show_image(canvas)
        playSound(photo,ENV)
        input("Please enter to continue...")
        i+=1
        
#Defining the play option    
def play():
    global amount
    i=0
    actual_n = 0
    print(amount)
    rounds = int(input("How many rounds would you like to play? "))
    for _ in range(rounds):
        canvas=img.get_white_image(350,350)
        learntimages = images[:amount]
        playimages = random.sample(learntimages, 3)
        soundimages = random.sample(playimages, 1)
        sound = soundimages[0]
        print(playimages)
        for i in range(0, 3):
            photo=playimages[i]
            all_n = random.randint(1,4)
            my_image = img.get_image("images/"+ photo + ".png")
            random_r = random.randint(0, 205)
            random_g = random.randint(0, 205)
            random_b = random.randint(0, 205)
            my_image = draw.recolor_image(my_image, [random_r, random_g, random_b])
            number_1 = random.randint(0, 3)
            number_2 = random.randint(0, 3)
            if number_1 == 2:
                my_image = draw.minify(my_image)
            if number_2 == 2:
                my_image = draw.mirror(my_image)
            canvas=draw.distribute_items(canvas,my_image,all_n)
            img.show_image(canvas)
            if photo == sound:
                actual_n = all_n
            i+=1
        playSound(sound,ENV)
        user_number = int(input("How many did you find? "))
        if user_number == actual_n:
            print("Correct")
        else:
            print("Incorrect")

#Defining the settings
def setting():
    global amount
    print()
    print('the current no. of images shown:', amount)
    question=input('would you like to change the amount of images shown? yes(y) or no(n): ')
    if question in 'yes':
        amount=int(input('choose the amount of images (number should be between 3 and 12): '))
        while (amount>12) or (amount<3):
            print()
            print ('enter a number between 3 and 12')
            amount=int(input('choose the amount of images (number should be between 3 and 12): '))  

#Option function to allow user to select an option    
def option():
    print()
    option=int(input("enter your option no.: "))
    while (option<1) or (option>4):
        print()
        print ('enter a correct option no.')
        option=int(input('enter your option no.: '))
    else:
        if option == 3:
            setting()
        elif option==1:
            learn()
        elif option==2:
            play()
        elif option==4:
            exit()

#main menu print function
def mainmenu():
    print()
    print('Main Menu')
    print('1. Learn - Word Flashcards')
    print('2. Play - Seek and Find Flashcards')
    print('3. Settings - Change Difficulty')
    print('4. Exit')
    print("Amount of items to be learnt:",amount)     

while True:
    mainmenu()
    option()