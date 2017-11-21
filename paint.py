from tkinter import *
import numpy as np
import matplotlib.pyplot as plt

pic = np.zeros(784, dtype=np.float32).reshape(28,28)


class Paint(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.setUI()
        self.brush_size = 15
        self.brush_color = "black"

    def draw(self, event):

        pic[round(28*(event.y - 1)/265), round(28*(event.x - 1)/265)] = 1
        pic[round(28*(event.y - 1)/265) + 1, round(28*(event.x - 1)/265) + 1] = 1
        pic[round(28*(event.y - 1)/265) - 1, round(28*(event.x - 1)/265) + 1] = 1

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
        self.result.set(4)
        plt.figure()

        plt.imshow(np.asmatrix(pic.reshape(28, 28)), 'pink', animated=False)
        plt.show()

    def setUI(self):
        self.parent.title("MNIST")  # Устанавливаем название окна
        self.pack(fill=BOTH, expand=1)  # Размещаем активные элементы на родительском окне

        self.columnconfigure(6,
                             weight=1)  # Даем седьмому столбцу возможность растягиваться, благодаря чему кнопки не будут разъезжаться при ресайзе
        #self.rowconfigure(2, weight=1)  # То же самое для третьего ряда

        self.canv = Canvas(self, width=265, bg="white")  # Создаем поле для рисования, устанавливаем белый фон
        self.canv.grid(row=2, column=0, columnspan=2,
                       padx=5, pady=5,
                       sticky=E + W + S + N)  # Прикрепляем канвас методом grid. Он будет находится в 3м ряду, первой колонке, и будет занимать 7 колонок, задаем отступы по X и Y в 5 пикселей, и заставляем растягиваться при растягивании всего окна

        self.result = StringVar()

        result = Label(self, textvariable=self.result)
        result.grid(row=0, column=2, padx=5)


        self.canv.bind("<B1-Motion>", self.draw)

        result_btn = Button(self, text="Result",
                         width=10, command=lambda: self.show_result())  # Создание кнопки:  Установка текста кнопки, задание ширины кнопки (10 символов)


        result_btn.grid(row=0, column=1)  # Устанавливаем кнопку первый ряд, вторая колонка

        clear_btn = Button(self, text="Clear all", width=10, command=lambda: self.clear())
        clear_btn.grid(row=0, column=0, sticky=W)


def main():
    root = Tk()
    root.geometry("500x310+300+300")
    app = Paint(root)
    root.mainloop()


if __name__ == "__main__":
    main()