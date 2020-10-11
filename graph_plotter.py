import tkinter as tk
import csv
import matplotlib.pyplot as plt
import numpy as np

from tkinter import filedialog

root = tk.Tk()
root.withdraw()
list_x=[]
list_y=[]
file_path = filedialog.askopenfilename()

print(file_path)

with open(file_path, newline='') as f:
    reader_target = csv.reader(f, delimiter=';')
    list = list(reader_target)
    for i in range (0,len(list)):
        row=list[i]
        list_x.append(float(row[0].replace(',','.')))
        list_y.append(float(row[1].replace(',','.')))

    plt.plot(list_x,list_y)

    #plt.yticks(np.arange(100, 170, 5))
    plt.ylabel('some numbers')
    plt.show()

def printgr(x,y):
    plt.plot(x,y)
    plt.ylabel('some numbers')
    plt.show()