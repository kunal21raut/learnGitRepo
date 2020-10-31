
import tkinter as t
import random
win=t.Tk()




number=random.randint(0,50)
player_name=str(input("HEllO !What is your name?"))

entry=t.Entry(win)

entry.grid(row=0,column=0,padx=8,pady=8)
no_of_guesses=0
print(player_name,", I am guessing the number between 0 to 50")

while no_of_guesses<5:
    guess=int(input("Guess the number :"))
    no_of_guesses +=1
    if guess< number:
        print("Your guess is to low")
    elif guess> number:
        print("Your guess is too high")
    elif guess==number:
        break
if guess==number:
    print("You guess the number in",no_of_guesses," tries.")
else:
    print("you didn't guessed the number in",no_of_guesses,"tries. The number was",number)


win.mainloop()
