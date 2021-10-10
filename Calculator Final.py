#Brian Clark
#6 Nov 18
#Calculator Final

from tkinter import *

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)  
        self.grid()
        self.display_str = ""
        self.create_widgets()

    def create_widgets(self):
        self.screen_txt = Text(self, height = 2, width = 28, wrap=WORD)
        self.screen_txt.grid(row = 0, columnspan = 4)
        #value columnspan = 2 makes super wide button arrangement
        #also value of width makes it go wonky, had to adjust both why
        self.screen_txt.tag_config("right_align", justify='right')
        
        #Button number 1
        Button(self,
               text = "1",
               command = self.clicked_1,
               bg = "red",
               height = 2,
               width = 6               
              ).grid(row = 5,
                     column = 0,
                     sticky = W,
                     padx = 3,
                     pady = 3)

        #Button number 2
        Button(self,
               text = "2",
               command = self.clicked_2,
               bg = "red",
               height = 2,
               width = 6
              ).grid(row = 5,
                     column = 1,
                     sticky = W,
                     padx = 3,
                     pady = 3)

        #Button number 3
        Button(self,
               text = "3",
               command = self.clicked_3,
               bg = "red",
               height = 2,
               width = 6
              ).grid(row = 5,
                     column = 2,
                     sticky = W,
                     padx = 3,
                     pady = 3)

        #Button number 4
        Button(self,
               text = "4",
               command = self.clicked_4,
               bg = "blue",
               fg = "white",
               height = 2,
               width = 6
              ).grid(row = 4,
                     column = 0,
                     sticky = W,
                     padx = 3,
                     pady = 3)
        #Button 5
        Button(self,
               text = "5",
               command = self.clicked_5,
               bg = "blue",
               fg = "white",
               height = 2,
               width = 6
               ).grid(row = 4,
                      column = 1,
                      sticky = W,
                      padx = 3,
                      pady = 3)
        #button 6
        Button(self,
               text = "6",
               command = self.clicked_6,
               bg = "white",
               height = 2,
               width = 6
               ).grid(row = 4,
                      column = 2,
                      sticky = W,
                      padx = 3,
                      pady = 3)
        #button 7
        Button(self,
               text = "7",
               command = self.clicked_7,
               bg = "blue",
               fg = "white",
               height = 2,
               width = 6
               ).grid(row = 3,
                      column = 0,
                      sticky = W,
                      padx = 3,
                      pady = 3)
        #button 8
        Button(self,
               text = "8",
               command = self.clicked_8,
               bg = "blue",
               fg = "white",
               height = 2,
               width = 6
               ).grid(row = 3,
                      column = 1,
                      sticky = W,
                      padx = 3,
                      pady = 3)
        #button 9
        Button(self,
               text = "9",
               command = self.clicked_9,
               bg = "red",
               height = 2,
               width = 6
               ).grid(row = 3,
                      column = 2,
                      sticky = W,
                      padx = 3,
                      pady = 3)
        #button 0
        Button(self,
               text = "0",
               command = self.clicked_0,
               bg = "white",
               height = 2,
               width = 6
               ).grid(row = 6,
                      column = 1,
                      sticky = W,
                      padx = 3,
                      pady = 3)
        #Clr button
        Button(self,
               text = "Clr",
               command = self.clicked_Clr,
               bg = "white",
               height = 2,
               width = 6
               ).grid(row = 6,
                      column = 0,
                      sticky = W,
                      padx = 3,
                      pady = 3)
        #decimal button
        Button(self,
               text = ".",
               command = self.clicked_11,
               bg = "white",
               height = 2,
               width = 6
               ).grid(row = 6,
                      column = 2,
                      sticky = W,
                      padx = 3,
                      pady = 3)
        #evaluate '=' button
        Button(self,
               text = "=",
               command = self.clicked_12,
               bg = "red",
               height = 2,
               width = 6
               ).grid(row = 7,
                      column = 3,
                      sticky = W,
                      padx = 3,
                      pady = 3)
        #+ button
        Button(self,
               text = "+",
               command = self.clicked_13,
               bg = "white",
               height = 2,
               width = 6
               ).grid(row = 6,
                      column = 3,
                      sticky = W,
                      padx = 3,
                      pady = 3)
        #- button
        Button(self,
               text = "-",
               command = self.clicked_14,
               bg = "red",
               height = 2,
               width = 6
               ).grid(row = 5,
                      column = 3,
                      sticky = W,
                      padx = 3,
                      pady = 3)
        #* button
        Button(self,
               text = "*",
               command = self.clicked_15,
               bg = "white",
               height = 2,
               width = 6
               ).grid(row = 4,
                      column = 3,
                      sticky = W,
                      padx = 3,
                      pady = 3)
        #/ button
        Button(self,
               text = "/",
               command = self.clicked_16,
               bg = "red",
               height = 2,
               width = 6
               ).grid(row = 3,
                      column = 3,
                      sticky = W,
                      padx = 3,
                      pady = 3)
        #Sq button
        Button(self,
               text = "Sq",
               command = self.clicked_Sq,
               bg = "red",
               height = 2,
               width = 6
               ).grid(row = 7,
                      column = 0,
                      sticky = W,
                      padx = 3,
                      pady = 3)
        #Sqrt button
        Button(self,
               text = "Sqrt",
               command = self.clicked_Sqrt,
               bg = "red",
               height = 2,
               width = 6
               ).grid(row = 7,
                      column = 1,
                      sticky = W,
                      padx = 3,
                      pady = 3)
        #% button
        Button(self,
               text = "%",
               command = self.clicked_17,
               bg = "red",
               height = 2,
               width = 6
               ).grid(row = 7,
                      column = 2,
                      sticky = W,
                      padx = 3,
                      pady = 3)
    # Mos Def
    def clicked_1(self):
        self.display_str += "1"
        self.screen_txt.delete(0.0, END)
        self.screen_txt.insert(0.0, self.display_str, "right_align")
    def clicked_Clr(self):
        self.screen_txt.delete(0.0, END)
        self.display_str = ""
    def clicked_2(self):
        self.display_str += "2"
        self.screen_txt.delete(0.0, END)
        self.screen_txt.insert(0.0, self.display_str, "right_align")
    def clicked_3(self):
        self.display_str += "3"
        self.screen_txt.delete(0.0, END)
        self.screen_txt.insert(0.0, self.display_str, "right_align")
    def clicked_4(self):
        self.display_str += "4"
        self.screen_txt.delete(0.0, END)
        self.screen_txt.insert(0.0, self.display_str, "right_align")
    def clicked_5(self):
        self.display_str += "5"
        self.screen_txt.delete(0.0, END)
        self.screen_txt.insert(0.0, self.display_str, "right_align")
    def clicked_6(self):
        self.display_str += "6"
        self.screen_txt.delete(0.0, END)
        self.screen_txt.insert(0.0, self.display_str, "right_align")
    def clicked_7(self):
        self.display_str += "7"
        self.screen_txt.delete(0.0, END)
        self.screen_txt.insert(0.0, self.display_str, "right_align")
    def clicked_8(self):
        self.display_str += "7"
        self.screen_txt.delete(0.0, END)
        self.screen_txt.insert(0.0, self.display_str, "right_align")
    def clicked_8(self):
        self.display_str += "8"
        self.screen_txt.delete(0.0, END)
        self.screen_txt.insert(0.0, self.display_str, "right_align")
    def clicked_9(self):
        self.display_str += "9"
        self.screen_txt.delete(0.0, END)
        self.screen_txt.insert(0.0, self.display_str, "right_align")
    def clicked_0(self):
        self.display_str += "0"
        self.screen_txt.delete(0.0, END)
        self.screen_txt.insert(0.0, self.display_str, "right_align")
    def clicked_11(self):
        self.display_str += "."
        self.screen_txt.delete(0.0, END)
        self.screen_txt.insert(0.0, self.display_str, "right_align")
    def clicked_13(self):
        self.display_str += "+"
        self.screen_txt.delete(0.0, END)
        self.screen_txt.insert(0.0, self.display_str, "right_align")
    def clicked_14(self):
        self.display_str += "-"
        self.screen_txt.delete(0.0, END)
        self.screen_txt.insert(0.0, self.display_str, "right_align")
    def clicked_15(self):
        self.display_str += "*"
        self.screen_txt.delete(0.0, END)
        self.screen_txt.insert(0.0, self.display_str, "right_align")
    def clicked_16(self):
        self.display_str += "/"
        self.screen_txt.delete(0.0, END)
        self.screen_txt.insert(0.0, self.display_str, "right_align")
    def clicked_12(self):
        value = self.screen_txt.get(0.0, END)        
        try:
            answer = eval(value)
            self.screen_txt.delete(0.0, END)            
            self.screen_txt.insert(0.0, answer, "right_align")
        except:
            self.screen_txt.delete(0.0, END)
            self.screen_txt.insert(0.0, "Invalid!", "right_align")
        self.display_str = ""
    def clicked_17(self):
        value = self.screen_txt.get(0.0, END)
        percent = (float(value)/100)
        self.screen_txt.delete(0.0,END)
        self.screen_txt.insert(0.0, percent, "right_align")
        self.display_str = ""
    def clicked_Sq(self):
        value = self.screen_txt.get(0.0, END)
        square = (float(value)*float(value))
        self.screen_txt.delete(0.0, END)
        self.screen_txt.insert(0.0, square, "right_align")
        self.display_str = ""
    def clicked_Sqrt(self):
        value = self.screen_txt.get(0.0, END)
        square_root = (float(value)**(1/2))
        self.screen_txt.delete(0.0, END)
        self.screen_txt.insert(0.0, square_root, "right_align")
        self.display_str = ""
        
    

#main
root = Tk()
root.title("'Merica")
app = Application(root)
root.mainloop()
