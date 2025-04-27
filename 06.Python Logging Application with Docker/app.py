import time

# Create or open a log file to write data
with open("/data/app.log", "a") as log_file:
    while True:
        log_file.write(f"App is running at {time.ctime()}\n")
        log_file.flush()
        time.sleep(5)
