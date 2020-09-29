from logs_reader import Logs_reader

reader_volk = Logs_reader()
reader_volk.readLog(r'C:\Users\Jura\Desktop\2019_11_15_flight_logs\VOLK\2020-08-20_10-59-45_2.csv',7)

print("lon0=",reader_volk.getLon0())
print("lat0=",reader_volk.getLat0())

target_reader = Logs_reader()
target_reader.setCoord0(reader_volk.getLon0(),reader_volk.getLat0())
target_reader.readLog(r'C:\Users\Jura\Desktop\2019_11_15_flight_logs\VOLK\2020-08-20 10-59-12_tar.csv',6)

print("lon0=",target_reader.getLon0())
print("lat0=",target_reader.getLat0())


print("distance_lon_X=",reader_volk.calcDist(reader_volk.getLat0(),target_reader.getLat0(),0,0))
print("distance_lat_Y=",reader_volk.calcDist(0,0,reader_volk.getLon0(),target_reader.getLon0()))
print("delta_time=",(reader_volk.getSyncTime()-target_reader.getSyncTime()))