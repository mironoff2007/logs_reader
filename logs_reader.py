import csv
import math
class Logs_reader:
    def readLog(self,s):
        with open( s,  newline='') as f:
        #C:\Users\Jura\Desktop\2019_11_15_flight_logs\VOLK\2020-08-20_10-59-45.csv
        #2020-08-20 10-59-12_target.csv
            reader = csv.reader(f, delimiter=';')
            your_list = list(reader)
            list_row = []
            x_coord = 0.0;
            y_coord = 0.0
            is_not_first = False
            aim = False
            end_aim = False
            lat1 = 0.0  # y0
            lat2 = 0.0
            lon1 = 0.0  # x0
            lon2 = 0.0
            R = 6371000;
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
                ch7 = float(your_list[l][1 + 7])
            if  (ch7 > 1600):
            # print("Signal=",your_list[l][1+7])
                aim = True
            if((ch7 < 1600) and aim):
                end_aim = True

            if (ch7 > 1600 and end_aim):
                print("next")
                aim = False
                end_aim = False
            if (your_list[l][0] == "GPS")  and aim and not is_not_first:
                is_not_first = True
                lat1 = float(your_list[l][7])
                lon1 = float(your_list[l][8])
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

                x_coord=x_coord+d_x
                y_coord=y_coord+d_y
                d = R * c;


                print( x_coord,",",y_coord,",",alt)
                lon1=lon2
                lat1=lat2
    #print( round(d_x,3), round(d_y,3))

            i=i+1

