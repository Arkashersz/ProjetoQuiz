import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import PhotoImage
import pandas as pd
import random

readQ = pd.read_excel('questions.xlsx')
questions = readQ.sample(n=5).values.tolist()


tela = tk.Tk()
tela.title('Quiz')
tela.geometry("500x550")



#Cores do projeto
background_color = "#F5FFFA"
text_color = "#1C1C1C"
button_color = "#4CAF50"

tela.config(bg=background_color)
tela.option_add('*Font', 'Arial')

# Logo
app_logo = PhotoImage(file="logo.png")
new_width, new_height = 200, 150
app_logo = app_logo.subsample(int(app_logo.width() / new_width), int(app_logo.height() / new_height))
app_label = tk.Label(tela, image=app_logo, bg=background_color)
app_label.pack(pady=10)

tela.mainloop()

