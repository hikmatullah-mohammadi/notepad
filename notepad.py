# import required libraries

import tkinter as tk
from tkinter import filedialog
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter import colorchooser
from datetime import datetime


today = datetime.today()

# create the main window
root = tk.Tk()
root.geometry('920x500')
root.minsize(450, 300)
root.config(bg='gray75')
root.resizable(False, False)
root.title('Untitled!')
try:
    root.iconbitmap('notepad_icon.ico')
except:
    pass

# create the welcoming message
w_l = tk.Label(root, text='', font=('Ariel', 80), bg='white', pady=200)
w_l.pack(fill='both')

def a():
    w_l.config(text='W', fg='blue')
def b():
    w_l.config(text='WE', fg='black')
def c():
    w_l.config(text='WEL', fg='red')

def d():
    w_l.config(text='WELC', fg='green')
def e():
    w_l.config(text='WELCO', fg='orange')
def f():
    w_l.config(text='WELCOM', fg='gray')
def g():
    w_l.config(text='WELCOME', fg='blue')
def bl():
    w_l.config(text='WELCOME', fg='black')
def re():
    w_l.config(text='WELCOME', fg='red')
def gr():
    w_l.config(text='WELCOME', fg='green')

def end():
    w_l.pack_forget()
    root.resizable(True, True)

    #define functions to change the font type and size
    def change_font(e):
        text_box.config(font=(font_name.get(), font_size.get()))
    def change_font_size(e):
        text_box.config(font=(font_name.get(), font_size.get()))

    font_list = [
        'Calibri',
        'Monotype Corsiva',
        'Courier',
        'Arial',
        'Agency FB',
        'Engravers MT',
        'Times New Roman',
        'Imprint MT Shadow',
        'G2 Geometr885 BT'
    ]

    font_size_range = [str(num) for num in range(8, 36)]

    # change font and its size
    font_name = tk.StringVar()
    font_name.set(font_list[0])
    fonts_names = tk.OptionMenu(root, font_name, *font_list, command=change_font)
    fonts_names.place(x=5, y=1)

    font_size = tk.StringVar()
    font_size.set(font_size_range[3])
    font_size_ = tk.OptionMenu(root, font_size, *font_size_range, command=change_font_size)
    font_size_.place(x = 100, y=1)


# here after 0.2 second, it will call function "a" ...
w_l.after(200, a)
w_l.after(400,b)
w_l.after(600,c)
w_l.after(700,d)
w_l.after(800,e)
w_l.after(900,f)
w_l.after(1000,g)
w_l.after(1100,bl)
w_l.after(1700,re)
w_l.after(2300,gr)
w_l.after(3400,end)



opened_file = False
# define a function to open a file
def open_new_file(e):
    global file_address, opened_file, content
    try:
        in_file = filedialog.askopenfile(mode='r', initialdir='.\\', filetypes=(('txt files', '*.txt'), ('All files', '*.*')))
        content = in_file.read()

    except:
        pass
    else:
        if opened_file:
            if content != text_box.get(1.0, 'end-2c'):
                choice = messagebox.askyesnocancel(title='Warning',\
                                                   message='Your current content might be lost! \nDo you want to update \n'+file_address)
                if choice==0:
                    text_box.delete(1.0, 'end')
                    text_box.insert(1.0, content)
                    opened_file = True
                    file_address = in_file.name
                    root.title(file_address)

                elif choice == 1:
                    save_file(None)
                    text_box.delete(1.0, 'end')
                    text_box.insert(1.0, content)
                    opened_file = True
                    file_address = in_file.name
                    root.title(file_address)
                else:
                    pass
            else:
                text_box.delete(1.0, 'end')
                text_box.insert(1.0, content)
                opened_file = True
                file_address = in_file.name
                root.title(file_address)

        else:
            if len(text_box.get(1.0, 'end-1c')) != 0:
                choice = messagebox.askyesno(title='Warning', message='Your current content will be lost!\nDo you want to save it?')
                if choice == 1:
                    save_as(None)
                    text_box.delete(1.0, 'end')
                    text_box.insert(1.0, content)
                    opened_file = True
                    file_address = in_file.name
                    root.title(file_address)
                elif choice == 0:
                    text_box.delete(1.0, 'end')
                    text_box.insert(1.0, content)
                    opened_file = True
                    file_address = in_file.name
                    root.title(file_address)
                else:
                    pass
            else:
                text_box.delete(1.0, 'end')
                text_box.insert(1.0, content)
                opened_file = True
                file_address = in_file.name
                root.title(file_address)

            in_file.close()



# define a function to create a new file
def create_new_file(e):
    global opened_file

    if opened_file:
        if content != text_box.get(1.0, 'end-2c'):
            choice = messagebox.askyesnocancel(title='Warning', \
                                               message='Your current content might be lost! \nDo you want to update \n' + file_address)
            if choice==0:
                text_box.delete(1.0, 'end')
                opened_file = False
                root.title('Untitled!')
            elif choice == 1:
                save_file(None)
                text_box.delete(1.0, 'end')
                opened_file = False
                root.title('Untitled!')
            else:
                pass
        else:
            text_box.delete(1.0, 'end')
            root.title('Untitled!')
            opened_file = False

    else:
        if len(text_box.get(1.0, 'end-1c')) != 0:

            choice = messagebox.askyesnocancel(title='Warning',\
                                               message='Your current content will be lost! \nDo you want to save it?')
            if choice==0:
                text_box.delete(1.0, 'end')
                opened_file = False
                root.title('Untitled!')
            elif choice == 1:
                save_as(None)
                text_box.delete(1.0, 'end')
                opened_file = False
                root.title('Untitled!')
            else:
                pass



# define a function to save a file
def save_file(e):
    if opened_file:
        temporary_file = open(file_address, 'w')
        temporary_file.write(text_box.get(1.0, 'end-1c'))
        temporary_file.close()
        messagebox.showinfo(title='Info', message='Saved!')
    else:
        save_as(None)



# define a function to save as new file
def save_as(e):
    global file_address, opened_file, content
    try:
        out_file = filedialog.asksaveasfile(mode='w', initialdir='.\\', filetypes=(('txt file', '*.txt'), ('All files', '*.*')))
        out_file.write(text_box.get(1.0, 'end-1c'))
        file_address = out_file.name
        root.title(file_address)
        opened_file = True
        content = text_box.get(1.0, 'end-2c')
    except:
        pass
    else:
        out_file.close()


# define a function to ask exit or not?
def exit_program(e):
    if opened_file:
        if content != text_box.get(1.0, 'end-2c'):
            choice = messagebox.askyesnocancel(title='Warning', message='Your current content might be lost! \nDo you want to update \n{}'.format(file_address))
            if choice==0:
                root.destroy()
            elif choice == 1:
                save_file(None)
                root.destroy()
            else:
                pass
        else:
            root.destroy()
    else:

        if len(text_box.get(1.0, 'end-1c')) != 0:
            choice = messagebox.askyesnocancel('Exit?', 'The contents will be lost\nDo you want to save it?')
            if choice == 1:
                save_as(None)
                root.destroy()
            elif choice == 0:
                root.destroy()
            else:
                pass
        else:
            root.destroy()



# define a function for 'about_us'
def about_us():
    messagebox.showinfo(title='About Us!', message='Software Developers!!!!!!!!')

# define a function for 'about_app'
def about_app():
    messagebox.showinfo(title='About App!', message='This is an extraordinary Notepad!!!!!!!')

# define a function to set/change background color
def change_bg_c():
    bg_c = colorchooser.askcolor(title='Choose Background Color')
    text_box.config(bg=bg_c[1])#0000ff
# define a function to set/change font color
def change_font_c():
    fg_c = colorchooser.askcolor(title='Choose Font Color')
    text_box.config(fg=fg_c[1])#ffffff

# date and time
def insert_time(e):
    text_box.insert('end', str(today.today())[11:19])

def insert_date(e):
    text_box.insert('end', str(today.today())[:10])
def insert_dt(e):
    text_box.insert('end', str(today.today())[:19])



# create the textbox
text_box = scrolledtext.ScrolledText(root, bg='white', undo=True, fg='black', width=300, height=50, font=('Calibri', 14))
text_box.pack(padx=10, pady=30)
text_box.config(bd=5, relief='sunken')



# create the menu
my_menu = tk.Menu(root)
root.config(menu=my_menu)


# define the file menu
file_menu = tk.Menu(my_menu, tearoff=0, font=('Ariel', 8))
my_menu.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='New    Ctrl+N', command=lambda: create_new_file(None))
file_menu.add_separator()
file_menu.add_command(label='Open    Ctrl+O', command=lambda: open_new_file(None))
file_menu.add_separator()
file_menu.add_command(label='Save    Ctrl+S', command=lambda: save_file(None))
file_menu.add_separator()
file_menu.add_command(label='Save as    Alt+S', command=lambda: save_as(None))
file_menu.add_separator()
file_menu.add_command(label='Exit    Alt+F4', command=lambda: exit_program(None), activebackground='red')


# define the setting menu
setting_menu = tk.Menu(my_menu, tearoff=0, font=('Ariel', 8))
my_menu.add_cascade(menu=setting_menu, label='Setting')
setting_menu.add_command(label='Font Color', command=change_font_c)
setting_menu.add_separator()
setting_menu.add_command(label='Background Color', command=change_bg_c)

# define the edit menu
edit_menu = tk.Menu(my_menu, tearoff=0, font=('Ariel', 8))
my_menu.add_cascade(menu=edit_menu, label='Edit')
edit_menu.add_command(label='Insert time    Ctrl+T', command=lambda: insert_time(None))
edit_menu.add_separator()
edit_menu.add_command(label='Insert date    Ctrl+D', command=lambda: insert_date(None))
edit_menu.add_separator()
edit_menu.add_command(label='Insert time and date   F5', command=lambda: insert_dt(None))

# define the about menu
about_menu = tk.Menu(my_menu, tearoff=0, font=('Ariel', 8))
my_menu.add_cascade(label='About', menu=about_menu)
about_menu.add_command(label='About Us!', command=about_us)
about_menu.add_separator()
about_menu.add_command(label='About App', command=about_app)


# shortcuts
text_box.bind('<Control-n>', create_new_file)
text_box.bind('<Control-s>', save_file)
text_box.bind('<Alt-s>', save_as)
text_box.bind('<Control-o>', open_new_file)
text_box.bind('<Alt-F4>', exit_program)

text_box.bind('<Control-t>', insert_time)
text_box.bind('<Control-d>', insert_date)
text_box.bind('<F5>', insert_dt)


root.mainloop()
