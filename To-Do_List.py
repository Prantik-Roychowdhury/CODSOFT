from tkinter import *
from tkinter import ttk
class todo:
    def __init__(self,root):
        self.root = root
        self.root.title('To-do-list')
        self.root.geometry('800x600+250+100')

        self.label = Label(self.root, text = "To-do-List",
        font="Times, 20 bold", width = 10,bd = 2, bg='cyan',fg='black')
        self.label.pack(side='top',pady=15, fill='both')

        self.label2 = Label(self.root, text = "Add Task",
        font="Times, 15", width = 13,bd = 2, bg='cyan',fg='black')
        self.label2.place(x=15,y=80)

        self.label3 = Label(self.root, text = "Task Log:",
        font="Times, 13", width = 13,bd = 2, bg='cyan',fg='black')
        self.label3.place(x=15,y=160)

        self.main_text = Listbox(self.root, height=11, bd=5, width= 20,font='ariel, 20')
        self.main_text.place(x=15, y=195)

        self.text = Text(self.root, bd=5, height=2, width=43,font="ariel, 10")
        self.text.place(x=15,y=110)


        def add():
            content = self.text.get(1.0,END)
            self.main_text.insert(END,content)
            with open('data.txt',"a") as file:
                file.write(content)
                file.seek(0)
                file.close()
            self.text.delete(1.0,END)
        
        def delete():
            delete = self.main_text.curselection()
            look = self.main_text.get(delete)
            with open('data.txt','r+') as file:
                newf = file.readlines()
                file.seek(0)
                for line in newf:
                    item = str(look)
                    if item not in line:
                        file.write(line)
                file.truncate()
            self.main_text.delete(delete)
        
        with open('data.txt','r') as file:
            read = file.readlines()
            for i in read:
                ready = i.split()
                self.main_text.insert(END, ready)
            file.close()
        
        self.button = Button(self.root, text = "Submit",font="sarif, 15 italic",
        width=10,bg="green",fg="black",command=add)
        self.button.place(x=350,y=110)

        self.button = Button(self.root, text = "Remove",font="sarif, 15 italic",
        width=10,bg="red",fg="black",command=delete)
        self.button.place(x=500,y=110)


def main():
    root = Tk()
    UI = todo(root)
    root.mainloop()

if __name__ =="__main__":
    main()