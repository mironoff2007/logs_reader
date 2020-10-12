import tkinter as tk
import csv
import matplotlib.pyplot as plt
import numpy as np

from tkinter import filedialog

root = tk.Tk()
root.withdraw()
list_x=[]
list_y=[]

list_x2=[]
list_y2=[]

list_z1=[]
list_z2=[]

list_i=[]

file_path = filedialog.askopenfilename()

print(file_path)

with open(file_path, newline='') as f:
    reader_target = csv.reader(f, delimiter=';')
    list = list(reader_target)
    for i in range (0,len(list)):
        row=list[i]
        list_x.append(float(row[0].replace(',','.')))
        list_y.append(float(row[1].replace(',','.')))

        list_x2.append(float(row[3].replace(',', '.')))
        list_y2.append(float(row[4].replace(',', '.')))

        list_z1.append(float(row[2].replace(',', '.')))
        list_z2.append(float(row[5].replace(',', '.')))
        list_i.append(i)

    plt.plot(list_x,list_y,label="hunter")
    plt.plot(list_x2,list_y2,label="target")
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left',ncol=2, mode="expand", borderaxespad=0.)
    #plt.yticks(np.arange(100, 170, 5))
    plt.ylabel('XY coordinates')
    plt.figure(0)

    plt.plot(list_i,list_z1,label="hunter")
    plt.plot(list_i, list_z2, label="target")
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left', ncol=2, mode="expand", borderaxespad=0.)
    plt.ylabel('Altitude')
    plt.figure(1)


    plt.show()

def printgr(x,y):
    plt.plot(x,y)
    plt.ylabel('some numbers')
    plt.show()