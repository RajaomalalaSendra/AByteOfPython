# creation of the text story behind
storyBehind = '''
Guido van Rossum, the creator of the Python language, named the language
after the BBC show "Monty Python’s Flying Circus". He doesn’t particularly like
snakes that kill animals for food by winding their long bodies around them and
crushing them.
'''
know = True
__author__ = ["Guido van Rossum","Guido", "Rossum", "Guido v Rossum", "Guido v. Rossum"]
__media__ = "BBC"
__show__ = "Monty Python's Flying Circus"
__likes__ = "snakes"
def doAgain():
    print("It is not true.\nYou must do it again.")

print('This is the story behind Python:\n{0}'.format(storyBehind))

# Our while loop for the quiz of 4 questions
while know:
    author = input("Who is the inventor of Python? ")
    if author.lower() == __author__[0].lower():
        print("That's true")
        show = input("What is the title of the show he likes? ")
        if show.lower() == __show__.lower():
            print("That's also true")
            media = input("What is the name of the media he sees it? ")
            if media.lower() == __media__.lower():
                print("Great :-)!!!\nNow we enter to the next question:")
                likes = input("What is the animal he doesn't like? ")
                if likes.lower() == __likes__.lower():
                    print("Oh!! You are so so great!!\nThank you ;-)\nThat's all for today.")
                    break
                else:
                    doAgain()
            else:
                doAgain()
        else:
            doAgain()
    else:
       doAgain()