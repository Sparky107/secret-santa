from tkinter import *
import tkinter.font as font
from names import names_

class SecretSanta(Frame):
    def __init__(self, master):
        super(SecretSanta, self).__init__(master)

        self.default_font = font.nametofont('TkDefaultFont')
        self.default_font.configure(family = 'Arial', size = 30)

        self.grid(row=0)

        self.box_width = 20
        self.box_height = 3

        self.namez = names_
        self.assigned = []
        self.read_names()

        self.create_widgets()

    def read_names(self):
        text_file = open('Python\\Misc\\SecretSanta\\names_list.txt', 'r')
        self.assigned = text_file.readlines()
        for i in range(len(self.assigned)):
            j = self.assigned[i].rstrip('\n')
            self.assigned[i] = j

        text_file.close()
    
    
    def create_widgets(self):
        '''Create widgets.'''
        Button(self, text= 'Bjarmi', command= lambda: self.find_name(0), width=self.box_width, height=self.box_height).grid(row=0, column=0, sticky=NS)
        Button(self, text= 'Benjamin', command= lambda: self.find_name(1), width=self.box_width, height=self.box_height).grid(row=0, column=1, sticky=NS)
        Button(self, text= 'Elias', command= lambda: self.find_name(2), width=self.box_width, height=self.box_height).grid(row=1, column=0, sticky=NS)
        Button(self, text= 'Helgi', command= lambda: self.find_name(3), width=self.box_width, height=self.box_height).grid(row=1, column=1, sticky=NS)

        self.name_txt = Text(self, height=3, width= round(self.box_width/2), font = ('Arial', 30))
        self.name_txt.grid(row=2, column=0, columnspan=2, sticky=NSEW)
        self.name_txt.tag_configure('center_text', justify= 'center')
        

        Button(self, text= 'CLEAR', command= lambda: self.name_txt.delete(0.0, END), height=self.box_height).grid(row=3, column=0, columnspan=2, sticky=NSEW)
    
    def find_name(self, num):
        self.name_txt.insert(0.0, '\n' + self.assigned[num])
        self.name_txt.tag_add('center_text', 0.0, END)

    

root = Tk()
root.title('Secret Santa Drawing')

frame1 = SecretSanta(root)

root.mainloop()