import sys
import time

def leak():
    dataList = []
    interval = float(sys.argv[1]) if len(sys.argv) > 1 else None
    while True:
	for i in range(1 << 20):
        	dataList.append(1337L)
        if interval is not None:
                time.sleep(interval)

leak()
