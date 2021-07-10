from tkinter import *






THEME_COLOR = "#375362"


class QuizInterface:


    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzes")
        self.window.config(padx = 20,pady =20,bg = THEME_COLOR )
        self.score_label =  Label(text = "Score : 0",bg = THEME_COLOR,pady = 10,fg = "white")
        self.score_label.grid(row= 0,column=1)

        self.canvas = Canvas(width = 300, height =250,bg = 'white')
        self.question_text = self.canvas.create_text(150,125,text = "Some Question",fill =THEME_COLOR,font = ('Arial',20,'italic'))
        self.canvas.grid(row=1,column=0,columnspan=2,pady = 50)
        true_image = PhotoImage(file='images/true.png')
        self.true_button = Button(image=true_image,highlightthickness= 0)
        self.true_button.grid(row=2,column = 0)

        self.window.mainloop()

QuizInterface()