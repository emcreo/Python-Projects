#
#Python 3.7.3
#
#Katherine Mazzolini
#
#Nice-Mean Game
#




def start(nice=0,mean=0,name=""): #both nice and mean = 0 & name is empty
    #get user's name              #to control the default vaules of them
    name = describe_game(name)#so far empty and when we get user's name it will be stored from the "return name" line
    nice,mean,name = nice_mean(nice,mean,name)
#passing info into and out of the function



def describe_game(name):
    """
        check if this is a new game or not.
        IF it is new, get the user's name.
        If it is not a new gaem, thank the player for
        playing again and continue with the game.
    """
    # meaning, if we don't already have this user's name,
    # then they are a new player and we need to get their name
    if name != "":
        print("\nThank you for playing again, {}.".format(name))
    else:
        stop = True   #only true if name is empty
        while stop:
            if name == "":
                name = input("\nWhat is your name? \n>>> ").capitalize() #at this point the name will not be empty
                if name != "": #the welcome messages get fired off because name no longer empty 
                    print("\nWelcome, {}!".format(name))
                    print("\nIn this game, you will be greeted \nby several different people.  \nYou can choose to be nice or mean,")
                    print("\nbut at the end of the game your fate \n will be sealed by your actions.")
                    stop = False  #now the variable stop is false so the loop stops
    return name

def nice_mean(nice,mean,name): #it starts with 0, 0, and person's name
    stop = True
    while stop:
        show_score(nice,mean,name)
        pick = input("\nA stranger approaches you for a \n conversation.  Will you be nice \nor mean? (N/M) \n>>>: ").lower()
        if pick == "n":
            print("\nThe stranger walks away smiling.")
            nice = (nice + 1) #0 + 1
            stop - False #shuts the loop off if they choose nice
        if pick == "m":
            print("\nThe stranger glares at you menancingly and storms off...")
            mean = (mean + 1)
            stop = False
    score(nice,mean,name) #pass the 3 variables to the score()


def show_score(nice,mean,name):
    print("\n{}, your current total: \n{}, Nice\n{}, Mean".format(name,nice,mean))



def score(nice,mean,name):
    # score function is being passed the values stored within their 3 variables
    if nice > 2: # if conditions is valid, call win function passing in the variables so it can use them
        win(nice,mean,name)
    if mean > 2:  # if conditions is valid, call win function passing in the variables so it can use them
        lose(nice,mean,name)
    else:         # else, call nice_mean function passing in the variable so it can use them
        nice_mean(nice,mean,name)

def win(nice,mean,name):
    # substitue the {} wildcards with our variable values
    print("\nNice job {}, you win! \nEveryone loves you and you've \nmade lots of friends along the way!".format(name))
    # call again function and pass in our variables
    again(nice,mean,name)


def lose(nice,mean,name):
    # substitute the {} wildcards with our variable values
    print("\nAhhh too bad, game over! \n{}, you live in a dirty beat-up \nby the river, whetched and alone!".format(name))
    # call again function and pass in our variables
    again(nice,mean,name)


def again(nice,mean,name):
    stop = True
    while stop:
        choice = input("\nDo you want to play again? (y/n):\n>>> ").lower()
        if choice == "y":
            stop = False
            reset(nice,mean,name)
        if choice == "n":
            print("\nOh, so sad, sorry to see you go!")
            stop = False
            quit()
        else:
            print("\nEnter (Y) for 'Yes', (N) for 'No':\n>>> ")

  
    
        
def reset(nice,mean,name):
    nice = 0
    mean = 0
    # Notice I don't reset the name varabile as that same user has elected to play again
    start(nice,mean,name)




    





if __name__ == "__main__":
    start()
