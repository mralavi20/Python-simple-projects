from tkinter import messagebox
import requests
from bs4 import BeautifulSoup
from tkinter import *

def find_movie ():
    movie_name = movie_name_input.get ()

    movie_name = movie_name.lower ()
    movie_full_name = movie_name
    movie_name = movie_name.split ()

    movie_name_adress = ""
    for i in range (len (movie_name)):
        if (i < len (movie_name) - 1):
            movie_name_adress = movie_name_adress + movie_name[i] + "+"
        else:
            movie_name_adress = movie_name_adress + movie_name[i]

    site_adress = "https://www.movie-map.com/" + movie_name_adress

    try:
        res = requests.get (site_adress)

        soup = BeautifulSoup (res.text, "html.parser")

        movies = soup.find_all ("a", attrs={"class": "S"})

        if (len (movies) == 0):
            raise Exception

        for i in range (len(movies)):
            movies[i] = movies[i].text

        file = open ("Desktop/movies_for_" + movie_full_name + ".txt", "w")

        movie_full_name = movie_full_name.capitalize ()

        file.write ("Similar movies for " + movie_full_name + ":\n")
        for i in range (len (movies)):
            if (movies[i] == movie_full_name):
                continue
            file.write (movies[i] + "\n")
        file.close ()

        messagebox.showinfo ("Saved", "Saved in a text file")

    except:
        messagebox.showerror ("Error", "Error happend try again")


window = Tk ()
 
window.geometry ("300x400")

window.title ("Find similar movies")


label = Label (window, text="Enter movie name:")
label.pack ()

movie_name_input = Entry (window)
movie_name_input.pack ()

Button (window, text="Find", command=find_movie).pack ()

window.mainloop ()
