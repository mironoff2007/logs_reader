import csv
import coordinates_converter as Converter

class Logs_reader:


    def __init__(self):
        self.lon0 = 0.0
        self.lat0 = 0.0

        self.lon1_hun = 0.0  # x0
        self.lon2_hun = 0.0

        self.lon1_tar = 0.0  # x0
        self.lon2_tar = 0.0

        self.lat1_hun = 0.0  # y0
        self.lat2_hun = 0.0

        self.lat1_tar = 0.0  # y0
        self.lat2_tar = 0.0

        self.alt_tar=0
        self.alt_hun=0

        self.x_coord0=0
        self.y_coord0=0
        self.lon_obj=0
        self.lat_obj=0
        self.sect=0

        self.t0=0

        self.coord_conv=Converter.Coordinates_converter

    def __setPosition(self):
        self.x_coord0 = self.coord_conv.CalcXCoord(self.lon1_hun,self.lat1_hun,self.lon1_tar,self.lat1_tar)
        self.y_coord0 = self.coord_conv.CalcYCoord(self.lon1_hun,self.lat1_hun,self.lon1_tar,self.lat1_tar)

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

            reader = csv.reader(f, delimiter=';')
            hunter_list = list(reader)

            hunter_lines_number=len(hunter_list)
            target_lines_number = len(target_lines)

            x_coord = 0.0
            y_coord = 0.0
            x_coord_tar = 0.0
            y_coord_tar = 0.0
            t=0.0

            mark=0

            is_not_first = False
            aim = False
            end_aim = False

            self.alt_hun = 0
            self.alt_tar=0

            i = 0;


        self.sect=1
        f_write = open(r'D:\section_1.csv', "w")

        ch=8#aim channel
        for l in range(0, min(len(hunter_list),len(target_lines)-1)):
            row_hunter = hunter_list[l]
            row_target = target_lines[l]

            if (hunter_list[l][0] == "RCIN"):
                ch_v = float(hunter_list[l][1 + ch])
            if  (ch_v > 1600):

                aim = True
            if((ch_v < 1600) and aim):

                print("next")
                aim = False

                self.sect = self.sect + 1

                f_write.close()
                f_write = open(r'D:\section_' + str(self.sect)+'.csv', "w")

                self.t0=float(hunter_list[l][1])/1000000

                is_not_first=False

                x_coord=0
                y_coord=0

                x_coord_tar=0
                y_coord_tar=0


            #logs fist line
            if (hunter_list[l][0] == "GPS")  and aim and not is_not_first:
                is_not_first = True

                self.lat1_hun = float(hunter_list[l][7])
                self.lon1_hun = float(hunter_list[l][8])

                self.lat1_tar = float(target_lines[l][7])
                self.lon1_tar = float(target_lines[l][8])

                self.__setPosition()#set target pos

                x_coord_tar = round(0 + self.x_coord0, 3)
                y_coord_tar = round(0 + self.y_coord0, 3)

                self.alt_tar = "{:.2f}".format(float(target_lines[l][9]))
                self.alt_hun = "{:.2f}".format(float(hunter_list[l][9]))

                #time
                mark = int(hunter_list[l][1])
                self.t0 = float(hunter_list[l][1]) / 1000000

                s1 = ''
                s1 = str(0).replace('.', ',') + ";" + str(0).replace('.', ',') + ";" + str(self.alt_hun).replace('.',',') + ";" + str(x_coord_tar).replace('.', ',') + ";" + str(y_coord_tar).replace('.', ',') + ";" + str(self.alt_tar).replace('.', ',') + ";" + str(0).replace('.', ',') + ";" + str(mark)
                f_write.write(s1)
                f_write.write('\n')

            elif (hunter_list[l][0] == "GPS") and aim and is_not_first:
            #hunter
                self.lat2_hun=float(hunter_list[l][7])
                self.lon2_hun=float(hunter_list[l][8])
                self.alt_hun="{:.2f}".format(float(hunter_list[l][9]))

                t_cur=float(hunter_list[l][1])/1000000
                t=round(t_cur-self.t0,3)

                mark = int(hunter_list[l][1])

                d_x = self.coord_conv.CalcXCoord(self.lon1_hun,self.lat1_hun,self.lon2_hun,self.lat2_hun)
                d_y = self.coord_conv.CalcYCoord(self.lon1_hun,self.lat1_hun,self.lon2_hun,self.lat2_hun)

                x_coord=round(x_coord+d_x,3)
                y_coord=round(y_coord+d_y,3)


            #target
                self.lat2_tar = float(target_lines[l][7])
                self.lon2_tar = float(target_lines[l][8])
                self.alt_tar ="{:.2f}".format(float(target_lines[l][9]))

                d_x_tar = self.coord_conv.CalcXCoord(self.lon1_tar, self.lat1_tar, self.lon2_tar, self.lat2_tar)
                d_y_tar = self.coord_conv.CalcYCoord(self.lon1_tar, self.lat1_tar, self.lon2_tar, self.lat2_tar)

                x_coord_tar = round(x_coord_tar + d_x_tar,3)
                y_coord_tar = round(y_coord_tar + d_y_tar,3)

                s1=''
                s1=str(x_coord).replace('.',',')+ ";"+ str(y_coord).replace('.',',')+ ";"+ str(self.alt_hun).replace('.',',')+";"+str(x_coord_tar).replace('.',',')+ ";"+str(y_coord_tar).replace('.',',')+";"+ str(self.alt_tar).replace('.',',')+";"+str(t).replace('.', ',')+";"+str(mark)

                print(s1)
                f_write.write(s1)
                f_write.write('\n')

                self.lon1_tar = self.lon2_tar
                self.lat1_tar = self.lat2_tar
                self.lon1_hun = self.lon2_hun
                self.lat1_hun = self.lat2_hun
    

            i=i+1























