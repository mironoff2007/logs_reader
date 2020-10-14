import csv
import math

import coordinates_converter as Converter
class Logs_reader:


    def __init__(self):
        self.lon0 = 0.0
        self.lat0 = 0.0
        self.time0 = 0.0
        self.x_coord0=0
        self.y_coord0=0
        self.lon_obj=0
        self.lat_obj=0
        self.sect=0
        self.coord_conv=Converter.Coordinates_converter

    def setCoord0(self,lon_obj,lat_obj):
        self.lon_obj = lon_obj
        self.lat_obj = lat_obj


    def __setPosition(self):
        self.x_coord0 = self.coord_conv.calcDist(self.lon_obj,0,self.lon0,0)
        self.y_coord0 = self.coord_conv.calcDist(0, self.lat_obj,0, self.lat0)

    def getLon0(self):
        return self.lon0

    def getLat0(self):
        return self.lat0

    def getSyncTime(self):
        return self.time0

    def sync(self, target_file, hunter_file):
        prev_rcin=False
        #search target sync line
        with open(target_file, newline='') as f:
            reader_target = csv.reader(f, delimiter=';')
            list_target = list(reader_target)
            ch=6
            line_number_target=0
        for l in range(0, len(list_target)):
                row_target = list_target[l]

                if (list_target[l][0] == "RCIN"):
                    ch7 = float(list_target[l][1 + ch])
                    if (ch7 > 1600):
                        line_number_target=l
                        break
        # _______________________
        # search hunter sync line
        with open(hunter_file, newline='') as file_to_read_hunter:
            reader_hunter = csv.reader(file_to_read_hunter, delimiter=';')
            list_hunter = list(reader_hunter)
            ch = 7
            line_number_hunter = 0
        for k in range(0, len(list_hunter)):
            row_hunter = list_hunter[k]

            if (list_hunter[k][0] == "RCIN"):
                ch7 = float(list_hunter[k][1 + ch])
                if (ch7 > 1600):
                    line_number_hunter = k
                    break
        # _______________________
        print(line_number_target,",",line_number_hunter)
        f = open(r'D:\target_sync.csv', "w")
        for ll in range(line_number_target, len(list_target)):
            row_target = list_target[ll]
            if ((list_target[ll][0] == "RCIN" and not prev_rcin) or list_target[ll][0] == "GPS" ):
                s1 = ''
                s1 = ';'.join(row_target)
                f.write(s1)
                f.write('\n')
                if (list_target[ll][0] == "RCIN"): prev_rcin = True
                else: prev_rcin=False
        f.close()

        prev_rcin=False
        f_hunter = open(r'D:\hunter_sync.csv', "w")
        for kk in range(k, len(list_hunter)):
            row_hunter = list_hunter[kk]
            if ((list_hunter[kk][0] == "RCIN" and not prev_rcin) or list_hunter[kk][0] == "GPS"):
                s1 = ''
                s1 = ';'.join(row_hunter)
                f_hunter.write(s1)
                f_hunter.write('\n')
                if (list_hunter[kk][0] == "RCIN"): prev_rcin = True
                else: prev_rcin=False
        f_hunter.close()

        self.readLog(r'D:\target_sync.csv',r'D:\hunter_sync.csv',8)


    def readLog(self,s_target,s,ch):
        with open( s,  newline='') as f:

            file_target=open(s_target,'r')
            target_reader=csv.reader(file_target, delimiter=';')
            target_lines=list(target_reader)
            target_lines_number=len(target_lines)

            reader = csv.reader(f, delimiter=';')
            your_list = list(reader)

            hunter_lines_number=len(your_list)
            list_row = []
            x_coord = 0.0
            y_coord = 0.0
            x_coord_tar = 0.0
            y_coord_tar = 0.0
            t=0.0
            t0=0.0
            mark=0

            is_not_first = False
            aim = False
            end_aim = False
            lat1 = 0.0  # y0
            lat2 = 0.0
            lon1 = 0.0  # x0
            lon2 = 0.0
            lat1_tar = 0.0  # y0
            lat2_tar = 0.0
            lon1_tar = 0.0  # x0
            lon2_tar = 0.0
            R = 6371000
            label = ""
            ch7 = 0;
            alt = 0
            alt_tar=0
            # print(your_list[1])
            i = 0;
            # lat1=float(your_list[1][11])
            # lon1=float(your_list[1][12])

        self.sect=1
        f_write = open(r'D:\section_1.csv', "w")
        f_write_gps = open(r'D:\section_1_gps.csv', "w")

        ch=8
        for l in range(0, min(len(your_list),len(target_lines)-1)):
            row_hunter = your_list[l]
            row_target = target_lines[l]
            sect=1

            if (your_list[l][0] == "RCIN"):
                ch_v = float(your_list[l][1 + ch])
            if  (ch_v > 1600):
            # print("Signal=",your_list[l][1+7])
                aim = True
            if((ch_v < 1600) and aim):
                end_aim = True

            if (ch_v > 1600 and end_aim):
                print("next")
                aim = False
                end_aim = False
                self.sect = self.sect + 1

                f_write.close()
                f_write = open(r'D:\section_' + str(self.sect)+'.csv', "w")

                f_write_gps.close()
                f_write_gps = open(r'D:\section_' + str(self.sect) + '_gps.csv', "w")

                t0=t


            #logs fist line
            if (your_list[l][0] == "GPS")  and aim and not is_not_first:
                is_not_first = True
                lat1 = float(your_list[l][7])
                lon1 = float(your_list[l][8])

                lat1_tar = float(target_lines[l][7])
                lon1_tar = float(target_lines[l][8])

                self.time0=int (your_list[l][1])

                self.lon0 = lon1
                self.lat0 = lat1

                mark = int(your_list[l][1])
                t0=float(your_list[l][1])/1000000


            if (your_list[l][0] == "GPS") and aim and is_not_first:
            #hunter
                lat2=float(your_list[l][7])
                lon2=float(your_list[l][8])
                alt="{:.2f}".format(float(your_list[l][9]))
                t_cur=float(your_list[l][1])/1000000
                t=t_cur-t0
                mark = int(your_list[l][1])

                d_x = self.coord_conv.CalcXCoord(lon1,lat1,lon2,lat2)
                d_y = self.coord_conv.CalcYCoord(lon1,lat1,lon2,lat2)

                x_coord=round(x_coord+d_x,3)
                y_coord=round(y_coord+d_y,3)


            #target
                lat2_tar = float(target_lines[l][7])
                lon2_tar = float(target_lines[l][8])
                alt_tar ="{:.2f}".format(float(target_lines[l][9]))

                d_x_tar = self.coord_conv.CalcXCoord(lon1_tar, lat1_tar, lon2_tar, lat2_tar)
                d_y_tar = self.coord_conv.CalcYCoord(lon1_tar, lat1_tar, lon2_tar, lat2_tar)

                x_coord_tar = round(x_coord_tar + d_x_tar + self.x_coord0,3)
                y_coord_tar = round(y_coord_tar + d_y_tar + self.y_coord0,3)
                s1=''
                s1=str(x_coord).replace('.',',')+ ";"+ str(y_coord).replace('.',',')+ ";"+ str(alt).replace('.',',')+";"+str(x_coord_tar).replace('.',',')+ ";"+str(y_coord_tar).replace('.',',')+";"+ str(alt_tar).replace('.',',')+";"+str(t).replace('.', ',')+";"+str(mark)
                s2 = ''
                s2 = str(lon2).replace('.', ',') + ";" + str(lat2).replace('.', ',') + ";" +  str(alt).replace('.',',')+";"+str(lon2_tar).replace('.',',')+ ";"+str(lat2_tar).replace('.',',')+";"+ str(alt_tar).replace('.',',')

                print(s1)
                f_write.write(s1)
                f_write.write('\n')
                f_write_gps.write(s2)
                f_write_gps.write('\n')

                lon1_tar=lon2_tar
                lat1_tar=lat2_tar
                lon1 = lon2
                lat1 = lat2
    #print( round(d_x,3), round(d_y,3))

            i=i+1























