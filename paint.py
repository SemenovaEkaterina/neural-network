from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
from detect import detect

pic = np.zeros(784, dtype=np.float32).reshape(28,28)


class Paint(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.setUI()
        self.brush_size = 15
        self.brush_color = "black"

    def draw(self, event):

        for i in range(-1, 2):
            for j in range(-1, 2):
                pic[round(27*(event.y)/265 + i), round(27*(event.x)/265) + j] = 1

        self.canv.create_oval(event.x - self.brush_size,
                              event.y - self.brush_size,
                              event.x + self.brush_size,
                              event.y + self.brush_size,
                              fill=self.brush_color, outline=self.brush_color)

    def clear(self):
        global pic
        pic = np.zeros(784, dtype=np.float32).reshape(28, 28)
        self.canv.delete("all")

    def show_result(self):
        global pic
        a = detect(pic.reshape(1,784)[0])

        self.result.set(a)
        plt.figure()

        plt.imshow(np.asmatrix(pic.reshape(28, 28)), 'pink', animated=False)
        plt.show()

    def setUI(self):
        self.parent.title("MNIST")
        self.pack(fill=BOTH, expand=1)

        self.columnconfigure(6,
                             weight=1)

        self.canv = Canvas(self, width=265, bg="white")
        self.canv.grid(row=2, column=0, columnspan=2,
                       padx=5, pady=5,
                       sticky=E + W + S + N)

        self.result = StringVar()

        result = Label(self, textvariable=self.result)
        result.grid(row=0, column=2, padx=5)


        self.canv.bind("<B1-Motion>", self.draw)

        result_btn = Button(self, text="Result",
                         width=10, command=lambda: self.show_result())

        result_btn.grid(row=0, column=1)

        clear_btn = Button(self, text="Clear all", width=10, command=lambda: self.clear())
        clear_btn.grid(row=0, column=0, sticky=W)


def main():
    root = Tk()
    root.geometry("500x310+300+300")
    app = Paint(root)
    root.mainloop()


if __name__ == "__main__":
    main()