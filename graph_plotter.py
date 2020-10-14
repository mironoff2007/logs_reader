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
list_t=[]

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
        list_t.append(float(row[6].replace(',', '.')))

    plt.figure(0)
    plt.plot(list_x,list_y,label="hunter")
    plt.plot(list_x2,list_y2,label="target")
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left',ncol=2, mode="expand", borderaxespad=0.)
    #plt.yticks(np.arange(100, 170, 5))
    plt.grid(color='k', linestyle='-', linewidth=1)
    plt.ylabel('XY coordinates')

    #plt.figure(1)
    #plt.plot(list_t,list_z1,label="hunter")
    #plt.plot(list_t, list_z2, label="target")
    #plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left', ncol=2, mode="expand", borderaxespad=0.)
    #plt.grid(color='k', linestyle='-', linewidth=1)
    #plt.ylabel('Altitude')

    plt.figure(2)
    plt.plot(list_t, list_x, label="hunter x(t)")
    plt.plot(list_t, list_x2, label="target x(t)")
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left', ncol=2, mode="expand", borderaxespad=0.)
    plt.ylabel('X(t)')
    plt.grid(color='k', linestyle='-', linewidth=1)

    plt.figure(3)
    plt.plot(list_t, list_y, label="hunter y(t)")
    plt.plot(list_t, list_y2, label="target y(t)")
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left', ncol=2, mode="expand", borderaxespad=0.)
    plt.ylabel('Y(t)')
    plt.grid(color='k', linestyle='-', linewidth=1)

    plt.figure(4)
    plt.plot(list_t, list_z1, label="hunter H(t)")
    plt.plot(list_t, list_z2, label="target H(t)")
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left', ncol=2, mode="expand", borderaxespad=0.)
    plt.ylabel('H(t)')
    plt.grid(color='k', linestyle='-', linewidth=1)

    plt.show()

def printgr(x,y):
    plt.plot(x,y)
    plt.ylabel('some numbers')
    plt.show()