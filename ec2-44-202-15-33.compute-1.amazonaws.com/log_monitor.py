import os
import time

log_file = '/var/log/suricata/fast.log'

def monitor_logs():
    with open(log_file, 'r') as f:
        f.seek(0, os.SEEK_END)  # Go to the end of the file
        while True:
            line = f.readline()
            if line:
                print(f"Alert: {line}")
            time.sleep(1)

if __name__ == '__main__':
    monitor_logs()
