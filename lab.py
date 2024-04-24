import customtkinter 
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import database

app = customtkinter.CTk()
app.title('Inventory Management System')
app.geometry('800x680')
app.config(bg='#0A0B0C')
app.resizable(False,False)

font1 = ('Arial',25,'bold')
font2 = ('Arial',18,'bold')
font3 = ('Arial',13,'bold')

title_label = customtkinter.CTkLabel(app,font=font1,text = 'Product Details',text_color ='#fff',bg_color='#0A0B0C')
title_label.place(x=35,y=15)

frame = customtkinter.CTkFrame(app,bg_color = '#0A0B0C',fg_color='#1B1B21',corner_radius=10,border_width=2,border_color='#fff',width=200,height=370)
frame.place(x=25,y=45)

image1 = PhotoImage(file="1.png")#isme add krna hai pic
image1_label=Label(frame,image=image1,bg='#1B1B21')
image1_label.place(x=65,y=5)

id_label = customtkinter.CTkLabel(frame,font=font2,text='Coffee ID:',text_color='#fff',bg_color='#1B1B21')
id_label.place(x=60,y=75)

id_entry = customtkinter.CTkEntry(frame,font=font2,text_color='#000',fg_color='#fff',boder_color='#B2016C',border_width=2,width=160)
id_entry.place(x=20,y=105)

name_label = customtkinter.CTkLabel(frame,font=font2,text='Coffee Name:',text_color='#fff',bg_color='#1B1B21')
name_label.place(x=50,y=140)

name_entry = customtkinter.CTkEntry(frame,font=font2,text_color='#000',fg_color='#fff',border_color='#B2016C',border_width=2,width=160)
name_entry.place(x=20,y=175)

stock_label = customtkinter.CTkLabel(frame,font=font2,text='In stock:',text_color='#fff',bg_color='#1B1B21')
stock_label.place(x=60,y=205)

stock_entry = customtkinter.CTkEntry(frame,font=font2,text_color='#000',fg_color='#fff',border_color='#B2016C',border_width=2,width=160)
stock_entry.place(x=20,y=240)

add_button=customtkinter.CTkButton(frame,font=font2,text_color='#fff',text='Add',fg_color='#047E43',hover_color='#025B30',bg_color='#1B1B21',curor='hand2',corner_radius=8,width=80)
add_button.place(x=15,y=280)

clear_button=customtkinter.CTkButton(frame,font=font2,text_color='#fff',text='New',fg_color='#E93E05',hover_color='#A82A00',bg_color='#1B1B21',curor='hand2',corner_radius=8,width=80)
clear_button.place(x=108,y=280)

update_button=customtkinter.CTkButton(frame,font=font2,text_color='#fff',text='Update',fg_color='#047E43',hover_color='#025B30',bg_color='#1B1B21',curor='hand2',corner_radius=8,width=80)
update_button.place(x=15,y=320)

delete_button=customtkinter.CTkButton(frame,font=font2,text_color='#fff',text='Delete',fg_color='#047E43',hover_color='#025B30',bg_color='#1B1B21',curor='hand2',corner_radius=8,width=80)
delete_button.place(x=108,y=280)

style = ttk.Style(app)

style.theme_use('clam')
style.configure('Treeview',font=font3,foreground='#fff',background='#A0B0C',fieldbackground='#1B1B21')
style.map('Treeview',background=[('selected','#AA04a7')])

tree = ttk.Treeview(app,height=10)
tree['columns']=('ID','Name','In Stock')

tree.column('#0',width=0,stretch=NO)
tree.column('ID',anchor=tk.CENTER,width=150)
tree.column('Name',anchor=tk.CENTER,width=150)
tree.column('In Stock',anchor=tk.CENTER,width=150)

tree.heading('ID',text='ID')
tree.heading('Name',text='Name')
tree.heading('In Stock',text='In Stock')

tree.place(x=300,y=45)




app.mainloop()
