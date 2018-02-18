"""
Application: Youtube Player with choice to show desired number of results.
Creator: Bibek Bhandari
Date: 2018/02/17
Licence: Open Source 
"""

from tkinter import *
from crawler import crawl, final_name, final_url
import tkinter.messagebox
import webbrowser
# building the window
class Application:
    def __init__(self, master):
        self.master = master

        # menubar
        menubar = Menu(master)
        # create a pulldown menu, and add it to the menu bar
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Open")
        filemenu.add_command(label="Save")
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=master.quit)
        menubar.add_cascade(label="File", menu=filemenu)

        master.config(menu=menubar)
        # heading
        self.heading = Label(master, text="Youtube Player", font=("verdana 25 bold"), bg='#FF0000', fg='white')
        self.heading.place(x=330, y=0)

        # labels and entries for the window
        # ask
        self.video_title = Label(master, text="Enter Video Name: ", font=("arial 10"), bg='#FF0000', fg='white')
        self.video_title.place(x=0, y=38)

        # entries
        self.name = StringVar()
        self.ent = Entry(master, width=25, textvariable=self.name)
        self.ent.place(x=150, y=40)

        # ask2
        self.resn = Label(master, text="No. of desired results", font=("arial 10"), bg='#FF0000', fg='white')
        self.resn.place(x=0, y=80)

        # ent2
        result = StringVar()
        self.w = Entry(master, width=8, textvariable=result)
        self.w.place(x=150, y=80)

        # BUTTONS AND INSTRUCTIONS
        self.btn = Button(master, text="Search Videos", command=self.find)
        self.btn.place(x=10, y=110)

        self.ins = Label(master, text="1. Search May take some time depending on your internet speed.", font=('arial 10'), bg='#FF0000',fg='white')
        self.ins.place(x=0, y=170)

        self.ins2 = Label(master, text="2. More number of desired results, More time it takes.", font=('arial 10'), bg='#FF0000',fg='white')
        self.ins2.place(x=0, y=200)

        self.ins2 = Label(master, text="3. High Number of results might lead to 'NOT RESPONDING', which is ok.", font=('arial 10'), bg='#FF0000',fg='white')
        self.ins2.place(x=0, y=230)

        # search results box and label
        self.r = Label(master, text="Search Results", font=("arial 10 bold"), bg='#FF0000', fg='white')
        self.r.place(x=400, y=40)

        # List Box
        self.listbox = Listbox(master, width=50)
        self.listbox.place(x=400, y=60)

        self.label = Label(master, text="",bg='#FF0000')
        self.label.place(x=250, y=110)
    def youtube(self, *args, **kwargs):
        selected = self.listbox.curselection()
        webbrowser.open(final_url[selected[0]])

    def clear_results(self):
        self.listbox.delete(0, END)
        del(final_name[:])
        del(final_url[:])
    def find(self, *args, **kwargs):

        if (self.listbox.size()) == 0:
            if int(self.w.get()) <= 10:
                # loading screen
                self.label.config(text = "Searching Youtube", fg='white', bg='#FF0000')
                self.label.update_idletasks()
                # crawling ht esite
                crawl(self.ent.get(), int(self.w.get()))
                self.label.config(text = "Completed", fg='white', bg='#FF0000')

                # buttons
                self.op = Button(self.master, text="Open Video", command=self.youtube)
                self.op.place(x=720, y=60)
                    
                self.op2 = Button(self.master, text="Clear Results", command=self.clear_results)
                self.op2.place(x=720, y=100)

                for item in range(len(final_name)):
                    self.listbox.insert(END, final_name[item])
            else:
                tkinter.messagebox.showinfo("Limit Exceeded", "You can get results only upto 10")


        else:
            tkinter.messagebox.showinfo("Warning", "Please clear the previous results.")

root = Tk()
obj = Application(root)
root.title("Youtube Player")
root.geometry("900x270")
root.resizable(False, False)
root.configure(background='#FF0000')
root.mainloop()