import socket
import datetime
import time
import csv
import ast

# Set up log file
log_file_name = 'IW_lighting_log_1min.csv'
logheaders=['time (local Pittsburgh EDT or EST)','PO-N','SO-ZSJ', 'PO-J', 'PO-K', 'SO-X', 'Kitchen', 'BAS', 'SO-S', 'SO-A', \
                    'LC', 'PO-V', 'PO-E', 'PO-J', 'PO-VV', 'PO-CS', 'PO-O', 'SC']
with open(log_file_name, 'w') as f:
	writer = csv.writer(f)
	writer.writerow(logheaders)

# Loop forever to read lighting state
while True:
	# Set up the socket
	s = socket.socket()
	s.connect(('localhost', 61221))
	s.sendall(bytearray('getall', encoding='utf-8'))
	now_time = str(datetime.datetime.now())
	rcd_this = ast.literal_eval(s.recv(4096).decode(encoding = 'utf-8'))[3:]
	rcd_this.insert(0, now_time);
	with open(log_file_name, 'a') as f:
		writer = csv.writer(f)
		writer.writerow(rcd_this);
	print ('Recording sucesses AT %s.' %(now_time))
	time.sleep(60)



