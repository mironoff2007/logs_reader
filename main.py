from logs_reader import Logs_reader
import tkinter as tk
from tkinter import filedialog
#
reader_volk = Logs_reader()
file_target_path = filedialog.askopenfilename( title = "Select target file")
file_hunter_path =   filedialog.askopenfilename( title = "Select hunter file")

reader_volk.sync(file_target_path,file_hunter_path)

#
# print("distance_lon_X=",reader_volk.calcDist(reader_volk.getLat0(),target_reader.getLat0(),0,0))
# print("distance_lat_Y=",reader_volk.calcDist(0,0,reader_volk.getLon0(),target_reader.getLon0()))
# print("delta_time=",(reader_volk.getSyncTime()-target_reader.getSyncTime()))