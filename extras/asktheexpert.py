from tkinter import Tk,simpledialog,messagebox
print('Ask the Expert - Capital Cities of the World')
root = Tk()
root.withdraw()
the_world = {}
def read_file():
    with open("ask.txt") as file:
        for line in file:
            line = line.rstrip('\n')
            country,city = line.split('/')
            the_world[country] = city
def write_f(country_name,city_name):
    with open("ask.txt","a") as file:
        file.write("\n" + country_name + "/" + city_name)
            
read_file()
while True:
    query = simpledialog.askstring('Country', 'Type the name of a country : ')
    query = query.capitalize()
    if query in the_world:
        result = the_world[query]
        messagebox.showinfo('Answer','The capital city of ' + query +' is ' + result +' ! ')
    else:
        new_city = simpledialog.askstring("Teach me","I don't know!" + " What is the capital of " + query + " ?")
        the_world[query] = new_city
        write_f(query,new_city)

root.mainloop()           