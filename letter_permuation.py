import os
from datetime import datetime
from itertools import product
def allperm(reserved_name):
    return set( map( ''.join, product( *zip( reserved_name.lower(), reserved_name.upper() ) )  ) )

#reserved_names = ['aux', 'com1', 'com2', 'com3', 'com4', 'com5', 'com6', 'com7', 'com8', 'com9', 'lpt1', 'lpt2', 'lpt3', 'lpt4', 'lpt5', 'lpt6', 'lpt7', 'lpt8', 'lpt9', 'con', 'nul', 'prn']
reserved_names = ['aux', 'com1', 'com9', 'lpt1', 'con', 'nul', 'prn']
global_list = []
for reserved_name in reserved_names:
    jpg_l = allperm(reserved_name + '.jpg')
    global_list.extend(jpg_l)
    jpeg_l = allperm(reserved_name + '.jpeg')
    global_list.extend(jpeg_l)

#print(global_list)
global_total = len(global_list)

folder_name = 'images/'
try:
    os.mkdir(folder_name)
except FileExistsError:
    pass
for i, l in enumerate(global_list):
    print(l)
    #print(str(i) + '/' + str(global_total) )
    #os.system("convert -font /usr/share/fonts/truetype/roboto/unhinted/RobotoCondensed-Regular.ttf -pointsize 11  caption:'" + l + "' '" + folder_name + l + "'")

with open('con.html', 'w') as f:
    f.write('<!DOCTYPE html>\n<html><body>\n' + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '</br>\n')
    f.write('hello, world!<br/>\n')
    for l in global_list:
        f.write('<img src="' + folder_name + l + '" loading="lazy">') 
    f.write('</body></html>')
    
