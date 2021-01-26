from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from datetime import datetime

import os
import time

desktop_dir = "/Users/SophieMBerger/Desktop"
destination_folder = "/Users/SophieMBerger/Documents/RelocatedItems"


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        # Track the Desktop directory
        for foldername in os.listdir(desktop_dir):
            if foldername == "Relocated Items":
                src = desktop_dir + "/" + foldername
                new_destination = destination_folder + \
                    "/" + foldername + str(datetime.now())
                os.rename(src, new_destination)


event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, desktop_dir, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
