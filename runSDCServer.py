
import argparse

from SDCServer.bacnet.readServer import ReadServer;

import threading

def main():
	parser = argparse.ArgumentParser(description='Run SDC Server')
	parser.add_argument('--read_port', default=61221, type=int, help='Read server listening port');
	parser.add_argument('--write_port', default=61222, type=int, help='Write server listening port');
	parser.add_argument('--read_config', default='SDCServer/bacnet/IW_lighting_ReadConfig.cfg', type=str, help='Read server configuration file');
	parser.add_argument('--write_config', default='SDCServer/bacnet/IW9701_WriteConfig.cfg', type=str, help='Write server configuration file')
	args = parser.parse_args();
	# Run
	readServerIns = ReadServer();
	runReadServer = lambda: readServerIns.runReadServer(args.read_port, args.read_config);
	readThread = threading.Thread(target = (runReadServer));
	readThread.start();

if __name__ == '__main__':
    main()

