words= ['Mango','Apple','gun','floor','fan','game','hello']

def wordSlider():
    global count,sliderWords
    text = "Welcome to typing speed increaser game  "
    if(count >= len(text)):
        count = 0
        sliderWords = ""
    sliderWords +=text[count]
    count += 1  
    fontlabel.configure(text= sliderWords)
    fontlabel.after(180,wordSlider)  



def startGame(event):
    
    global score,miss
    if timeleft == 60:
        time()
    gamePlayDetailLabel.configure(text = "")

    if(wordEntry.get() == wordLabel["text"]):
        score+=1
    else:
        miss+=1
    random.shuffle(words) 
    wordLabel.configure(text = words[0])   
    wordEntry.delete(0,END)
    scoreLabelCount.configure(text = score)

def time():
    global timeleft,score,miss
    if timeleft > 0:
        timeleft -= 1
        timeLabelCount.configure(text = timeleft)
        timeLabelCount.after(1000,time)
        
    else:
        gamePlayDetailLabel.configure(text = "Hit = {} | Miss = {} | Total Score = {}".format(score,miss,score-miss))        
        rr = messagebox.askretrycancel('Notification','for Play again enter retry button')
        if rr == True:
            score = 0
            miss = 0
            timeleft = 60
            timeLabelCount.configure(text = timeleft)
            wordLabel.configure(text = words[0])
            scoreLabelCount.configure(text = score)








from  tkinter import *
from tkinter import messagebox
import random
root = Tk()
root.geometry("800x600+400+100")
root.configure(bg = "light blue")
root.title("Typing Speed Increaser Game")
root.iconbitmap("Awicons-Vista-Artistic-Folder-my-pictures.ico")

score = 0
timeleft = 60
count = 0
sliderWords = ''
miss = 0

fontlabel  = Label(root,width = 40,text = "",font = ("arial",25,"italic bold"),bg = "light blue",fg = "green")
fontlabel.place(x = 30, y = 10)
wordSlider()

random.shuffle(words)
wordLabel = Label(root,bg = "light blue",text = words[0],font = ("arial",25,"italic bold"))
wordLabel.place(x = 350, y = 200)

wordEntry = Entry(root,font = ("arial",25,"italic bold"),bd = 10,justify = "center")
wordEntry.place(x = 225,y = 300)
wordEntry.focus_set()

scoreLabel = Label(root,text="Your Score : ",font = ("arial",25,"italic bold"),bg = "light blue",fg = "blue")
scoreLabel.place(x = 10,y =100)

scoreLabelCount =  Label(root,text=score,font = ("arial",25,"italic bold"),bg = "light blue",fg = "blue")
scoreLabelCount.place(x =80 , y =140)


timerLabel  = Label(root,text="Time Left : ",font = ("arial",25,"italic bold"),bg = "light blue",fg = "blue")
timerLabel.place(x= 600,y = 100)

timeLabelCount =  Label(root,text=timeleft,font = ("arial",25,"italic bold"),bg = "light blue",fg = "blue")
timeLabelCount.place(x =680 , y =140)

gamePlayDetailLabel = Label(root,text = "Type word and hit enter button",font = ("arial",25,"italic bold"),bg = "light blue",fg = "blue")
gamePlayDetailLabel.place(x = 180,y = 450)







root.bind("<Return>",startGame)
root.mainloop()