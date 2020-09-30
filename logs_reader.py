import csv
import math
class Logs_reader:

    def __init__(self):
        self.lon0 = 0.0
        self.lat0 = 0.0
        self.time0 = 0.0
        self.x_coord0=0
        self.y_coord0=0
        self.lon_obj=0
        self.lat_obj=0

    def setCoord0(self,lon_obj,lat_obj):
        self.lon_obj = lon_obj
        self.lat_obj = lat_obj


    def __setPosition(self):
        self.x_coord0 = self.calcDist(self.lon_obj,self.lon0,0,0)
        self.y_coord0 = self.calcDist(0,0, self.lat_obj, self.lat0)

    def getLon0(self):
        return self.lon0

    def getLat0(self):
        return self.lat0

    def getSyncTime(self):
        return self.time0

    def calcDist(self,lon1,lon2,lat1,lat2):
        R = 6371000

        f1 = lat1 * math.pi / 180;
        f2 = lat2 * math.pi / 180;
        df = (lat2 - lat1) * math.pi / 180;
        dl = (lon2 - lon1) * math.pi / 180;  # x

        a = math.sin(df / 2) * math.sin(df / 2) + math.cos(f1) * math.cos(f2) * math.sin(dl / 2) * math.sin(dl / 2);

        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a));

        d = R * c
        return d

    def sync(self, target_file, hunter_file):
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
        with open(hunter_file, newline='') as f:
            reader_hunter = csv.reader(f, delimiter=';')
            list_hunter = list(reader_hunter)
            ch = 7
            line_number_hunter = 0
        for k in range(0, len(list_hunter)):
            row_target = list_hunter[k]

            if (list_target[k][0] == "RCIN"):
                ch7 = float(list_hunter[k][1 + ch])
                if (ch7 > 1600):
                    line_number_hunter = k
                    break
        # _______________________
        print(l,",",k)
        f = open(r'D:\target_sync.txt', "w")
        for ll in range(l, len(list_target)):
            row_target = list_target[ll]
            s1 = ''
            s1 = ';'.join(row_target)
            f.write(s1)
            f.write('\n')
        f.close()



    def readLog(self,s,ch):
        with open( s,  newline='') as f:

            reader = csv.reader(f, delimiter=';')
            your_list = list(reader)
            list_row = []
            x_coord = 0.0
            y_coord = 0.0
            is_not_first = False
            aim = False
            end_aim = False
            lat1 = 0.0  # y0
            lat2 = 0.0
            lon1 = 0.0  # x0
            lon2 = 0.0
            R = 6371000
            label = ""
            ch7 = 0;
            alt = 0
            # print(your_list[1])
            i = 0;
            # lat1=float(your_list[1][11])
            # lon1=float(your_list[1][12])

        for l in range(0, len(your_list)):
            list_row = your_list[l]

            if (your_list[l][0] == "RCIN"):
                ch7 = float(your_list[l][1 + ch])
            if  (ch7 > 1600):
            # print("Signal=",your_list[l][1+7])
                aim = True
            if((ch7 < 1600) and aim):
                end_aim = True

            if (ch7 > 1600 and end_aim):
                print("next")
                aim = False
                end_aim = False
            #logs fist line
            if (your_list[l][0] == "GPS")  and aim and not is_not_first:
                is_not_first = True
                lat1 = float(your_list[l][7])
                lon1 = float(your_list[l][8])

                self.time0=int (your_list[l][1])

                self.lon0 = lon1
                self.lat0 = lat1

            if (your_list[l][0] == "GPS") and aim and is_not_first:

                lat2=float(your_list[l][7])
                lon2=float(your_list[l][8])
                alt=your_list[l][9]

                f1 = lat1 * math.pi/180;
                f2 = lat2 * math.pi/180;
                df = (lat2-lat1) * math.pi/180;
                dl = (lon2-lon1) * math.pi/180;# x

                a_x =math.cos((f1+f2)/2) * math.cos((f1+f2)/2) *math.sin(dl/2) * math.sin(dl/2);
                a_y = math.sin(df/2) * math.sin(df/2) + math.cos(f1) * math.cos(f2) *math.sin(0) * math.sin(0);

                a = math.sin(df/2) * math.sin(df/2) + math.cos(f1) * math.cos(f2) *math.sin(dl/2) * math.sin(dl/2);

                c_x = 2 * math.atan2(math.sqrt(a_x), math.sqrt(1-a_x));
                c_y = 2 * math.atan2(math.sqrt(a_y), math.sqrt(1-a_y));

                c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a));


                d_x = R * c_x;
                if lon2<lon1 : d_x=-d_x
                d_y = R * c_y;
                if lat2<lat1 : d_y=-d_y

                x_coord=x_coord+d_x+self.x_coord0
                y_coord=y_coord+d_y+self.y_coord0

                d = R * c; #in meters


                print( x_coord,",",y_coord,",",alt)
                lon1=lon2
                lat1=lat2
    #print( round(d_x,3), round(d_y,3))

            i=i+1























