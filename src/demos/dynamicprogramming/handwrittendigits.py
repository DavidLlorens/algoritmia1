#coding: latin1

#< full
from tkinter import *
from algoritmia.problems.sequencecomparison.dtw import DynamicTimeWarper

class OnLineHandwritting(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()
        self.stroke_lines = []
        self.mode = 'learning'
        self.digits = []
        self.ask_for_digit(0)
        self.DTW = DynamicTimeWarper()

    def create_widgets(self):
        self.drawing_area = Canvas(self, width=200, height=200, bg='white')
        self.drawing_area.grid()
        self.message_area = Label(self, bg='yellow')
        self.message_area.grid(sticky=E+W)
        self.quit_button = Button ( self, text="Quit", command=self.quit )
        self.quit_button.grid()
        self.drawing_area.bind('<Button-1>', self.on_button)
        self.drawing_area.bind('<ButtonRelease-1>', self.on_release_button)

    def ask_for_digit(self, i):
        self.message_area.configure(text='Escribe el dígito %d' % i)

    def report_digit(self, i):
        self.message_area.configure(text='Has escrito un %d' % i)

    def on_button(self, event):
        self.x0, self.y0 = event.x, event.y
        self.stroke = [(0, 0)]
        for line in self.stroke_lines: self.drawing_area.delete(line)
        self.stroke_lines = []
        self.drawing_area.bind('<Motion>', self.on_motion)

    def on_release_button(self, event):
        self.drawing_area.unbind('<Motion>')
        if self.mode == 'learning':
            self.digits.append(self.stroke)
            self.ask_for_digit(len(self.digits))
            if len(self.digits) == 10:
                self.mode = 'recognizing'
                self.message_area.configure(text='Escriba dígitos')
        elif self.mode == 'recognizing':
            self.report_digit(self.classify(self.digits))

    def on_motion(self, event):
        x1, y1 = self.stroke[-1]
        self.stroke.append( (event.x-self.x0, event.y-self.y0) )
        self.stroke_lines.append(
            self.drawing_area.create_line(event.x, event.y, x1+self.x0, y1+self.y0))

    def distortion(self, digit):
        return self.DTW.distortion(self.stroke, digit)/(len(self.stroke)+len(digit))
     
    def classify(self, stroke):
        distortions = [self.distortion(digit) for digit in self.digits]
        return distortions.index(min(distortions))

app = OnLineHandwritting()
app.master.title("On-line handwritting")
app.mainloop() 
#> full