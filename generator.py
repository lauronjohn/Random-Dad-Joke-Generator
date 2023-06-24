import tkinter as tk
import requests
import os

def generateJoke(canvas):
    url = "https://dad-jokes.p.rapidapi.com/random/joke"
    response = requests.get(url, headers=os.getenv("headers")).json()
    dad_joke = response['body'][0]['setup']
    punch_line = response['body'][0]['punchline']
    label1 = tk.Label(canvas, font = a, text = dad_joke)
    label1.pack()
    label2 = tk.Label(canvas, font = b, text = punch_line)
    label2.pack()
    button = tk.Button(canvas, text="Generate New Joke", command=button_clicked)
    button.pack()

def button_clicked():
    for widget in canvas.winfo_children():
        widget.destroy()
    generateJoke(canvas)

canvas = tk.Tk()
canvas.geometry("700x100")
canvas.title("Lauron's Random Dad Joke Generator")

a = ("sans-serif", 15, "bold")
b = ("sans-serif", 20, "bold")

generateJoke(canvas)
canvas.mainloop()
#print(dad_joke + "\n" + punch_line)