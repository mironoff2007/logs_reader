from logs_reader import Logs_reader
#
reader_volk = Logs_reader()
reader_volk.sync(r'D:\2020-08-20_10-59-12_tar.csv',r'D:\2020-08-20_10-59-45.csv')

#
# print("distance_lon_X=",reader_volk.calcDist(reader_volk.getLat0(),target_reader.getLat0(),0,0))
# print("distance_lat_Y=",reader_volk.calcDist(0,0,reader_volk.getLon0(),target_reader.getLon0()))
# print("delta_time=",(reader_volk.getSyncTime()-target_reader.getSyncTime()))