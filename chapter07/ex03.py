import time

unix_timestamp = time.time()
local_time = time.localtime(unix_timestamp)

print(time.strftime('%y-%m-%d %H:%M:%S', local_time))
