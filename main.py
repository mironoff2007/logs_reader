from logs_reader import Logs_reader

reader = Logs_reader()
reader.readLog(r'C:\Users\Jura\Desktop\2019_11_15_flight_logs\VOLK\2020-08-20_10-59-45_2.csv')
print("lat0=",reader.getLat0())
print("lon0=",reader.getLon0())

target_reader = Logs_reader()
target_reader.readLog(r'C:\Users\Jura\Desktop\2019_11_15_flight_logs\VOLK\2020-08-20 10-59-12_tar.csv')

print("lat0=",target_reader.getLat0())
print("lon0=",target_reader.getLon0())

print("distance_lon_X=",reader.calcDist(0,0,reader.getLon0(),target_reader.getLon0()))
print("distance_lat_Y=",reader.calcDist(reader.getLat0(),target_reader.getLat0(),0,0))
print("delta_time=",(reader.getSyncTime()-target_reader.getSyncTime()))