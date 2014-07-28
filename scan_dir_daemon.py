import sys
import time
from watchdog.events import PatternMatchingEventHandler
from watchdog.observers import Observer
from binarization_scanned_images import Binarize


class MyEventHandler(PatternMatchingEventHandler):
    patterns = ["*.png", "*.jpg"]
    ignore_directories = False

    def on_created(self, event):
        print "e=", event
        if not event.is_directory:
            print "file created!"
            Binarize(event.src_path, 25)


def main(argv=None):
    path = argv[1]
    observer = Observer()
    observer.schedule(MyEventHandler(), path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    sys.exit(main(sys.argv))