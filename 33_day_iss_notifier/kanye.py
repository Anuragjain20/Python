from tkinter import *
import requests


def get_quote():
    response = requests.get(url = 'https://api.kanye.rest/')
    response.raise_for_status()
    data = response.json()
    quote = data['quote']
    #Write your code here.
    canvas.itemconfig(quote_text,text = quote)



window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=500, height=514)
background_img = PhotoImage(file="background.png")
canvas.create_image(350, 307, image=background_img)
quote_text = canvas.create_text(350, 307, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()