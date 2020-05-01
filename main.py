from tkinter import Tk, Label, Button, Entry, Frame
from PIL import Image, ImageTk

'''Take in raw number(grade before compaction), calculate according to 25% compaction per inch, 
and return converted grade (in tenths of inches)'''


def calcGrade(numbers):
    num = int(numbers)
    if (num >= 15):
        convGrade = ((num / 4) + num) / 10
        return round(convGrade, 1)

    if (num == 0):
        return 0

    else:
        convGrade = ((num / 4) + num) - 1
        return round(convGrade, 1)


'''Take in raw value(equivalent grades in tenths of inches), calculate and return depth conversion 
in inches'''


def convertToInches(number):
    num = int(number) * 1.2
    return round(num, 1)


'''Take in raw value(square feet required to calculate tonnage), and convert/return value as square yards'''


def ftToYards(number):
    num = int(number) / 9
    return round(num, 1)


'''Take in raw value(square yards required to reverse calculate distance remaining via tonnage), and convert/return value as square feet'''


def ydsToFt(number):
    num = int(number) * 9
    return round(num, 1)


class Root(Tk):

    def __init__(self):
        super().__init__()
        font1 = ("helvetica", 12, "bold")  # font designated for larger title text
        font2 = ("helvetica", 8, "bold")  # font designate for smaller descriptory text
        photo = Image.open("paving.png")  # image specified for header of application
        render = ImageTk.PhotoImage(photo)
        picFrame = Frame(self)
        picFrame.pack()  # set image to Frame to properly render and adjust spacing
        self.title_label = Label(picFrame, image=render)
        self.title_label.image = render
        self.title_label.pack()
        self.title_label = Label(self,
                                 text="\n\nPaving Calculation Assistant\n\nUse this tool to perform quick calculations\n\nUse the toggle buttons to select your conversions\n\n")
        self.title_label["bg"] = "PeachPuff"
        self.title_label.configure(font=font1)
        self.title_label.pack()
        frame = Frame(self)
        frame.pack()
        self.button = Button(frame, text="Convert(sqft-sqyds)",
                             command=self.convertToYds)  # button created to activate convertToYds function
        self.button.configure(font=font2)
        self.button.pack(side="left")
        self.button = Button(frame, text="Convert(sqyds-sqft",
                             command=self.convertToFt)  # button created to activate convertToFt function
        self.button.configure(font=font2)
        self.button.pack(side="left")
        self.button = Button(frame, text="Compute Grade Equivalent",
                             command=self.convertGrade)  # button created to activate convertGrade function
        self.button.configure(font=font2)
        self.button.pack(side="left")
        self.button = Button(frame, text="Click to convert units to standard inches.",
                             command=self.convertButton)  # button created to activate converToInches function
        self.button.configure(font=font2)
        self.button.pack(side="left")
        self.label = Label(self, text="\n")
        self.label["bg"] = "PeachPuff"
        self.label.pack()
        entryFrame = Frame(self)
        entryFrame.pack()
        self.entry = Entry(entryFrame)
        self.entry.pack()
        self.entry.insert(0, 0)
        self.label = Label(self, text="\n")
        self.label["bg"] = "PeachPuff"
        self.label.pack()
        self.title_label.pack()
        self.title_label = Label(self, text="\n\n\nCopyright\n\nNick Pisor\nLakeside Industries")
        self.title_label["bg"] = "PeachPuff"
        self.title_label.pack()

    def convertGrade(self):
        self.label.configure(text=(str(calcGrade(self.entry.get())) + " units."))

    def convertButton(self):
        self.label.configure(text=(str(convertToInches(calcGrade(self.entry.get()))) + " inches."))

    def convertToYds(self):
        self.label.configure(text=(str(ftToYards(self.entry.get()))) + " yards.")

    def convertToFt(self):
        self.label.configure(text=(str(ydsToFt(self.entry.get()))) + " feet.")


root = Root()
root["bg"] = "PeachPuff"
root.mainloop()
