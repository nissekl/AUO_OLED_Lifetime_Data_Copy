"""AUO OLED lifetime machine automatic data download program"""
"""Created by Hung-Hsiu Yen"""

import os
import datetime
import shutil
import sys
import time

file_direction = sys.argv[1] #enter file path of the lifetime data folder
usb_direction = sys.argv[2] #enter the USB path you want to copy to

print "Created by 1601002 AUO"

data_position = file_direction
lifetime_file = os.listdir(data_position)
data_count = 0

for i in lifetime_file:
    data_count=data_count+1
    print "progress:"+"%s\%s" %((data_count), (len(lifetime_file)))   
    if os.path.isdir(data_position+"\%s" %(i)) == True:
       lt_file = os.listdir(data_position+"\%s" %(i))
       data_name=[]
       data_time=[]
       for j in range(len(lt_file)):
           if len(lt_file[j]) > 12:
              data_name.append(lt_file[j])
              position = data_position+"\%s\%s" %((i),(lt_file[j]))
              data_time.append(os.stat(position).st_mtime)   
       latest_data_name = data_name[data_time.index(max(data_time))]
       copy_position = data_position+"\%s\%s" %((i),(latest_data_name))
       shutil.copy(copy_position,usb_direction)

print("Copy Complete!!")