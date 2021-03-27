#! /usr/bin/env python3

from pathlib import Path
from time import sleep
from watchdog.observers import Observer
from src.event_handler import EventHandler

if __name__ == '__main__':
    watch_path = Path('/Volumes/USB-DRV-01M/categorised_files_from_dell01/uncategorised')
    destination_root = Path('/Volumes/USB-DRV-01M/categorised_files_from_dell01')

    event_handler = EventHandler(watch_path=watch_path, destination_root=destination_root)

    # Check files before sleeping as there may be some already present
    event_handler.move_files()

    observer = Observer()
    observer.schedule(event_handler, f'{watch_path}', recursive=True)
    observer.start()

    try:
        # print(f'Waiting for updates...')
        while True:
            sleep(5)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
