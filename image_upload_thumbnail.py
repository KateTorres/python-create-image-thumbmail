# This script monitors, written in Python, monitors one directory. 
# When file with jpg extention is dropped in that directory, the script creates a thumbnail.

# File must be dropped using a mouse. Copy-pasting will give permission error.

# The script is useful for autoamted updates of a website. 

import os # for operating system interactions
from PIL import Image #Python Imaging Library for image processing
from watchdog.observers import Observer #for monitoring filesystem events
from watchdog.events import PatternMatchingEventHandler #for monitoring filesystem events

#Name your directories: 
IMAGES_DIR = r"C:\projects\templates\images"
THUMBNAILS_DIR = r"C:\projects\templates\thumbnails"

class ImageEventHandler(PatternMatchingEventHandler):
    def __init__(self, source_dir, target_dir, patterns=None):
        super().__init__(patterns=patterns)
        self.source_dir = os.path.abspath(source_dir)
        self.target_dir = os.path.abspath(target_dir)
        os.makedirs(self.target_dir, exist_ok=True)

    def on_created(self, event):
        super(ImageEventHandler, self).on_created(event)
        # Process only if it's an image file in the source directory
        if os.path.dirname(os.path.abspath(event.src_path)) == self.source_dir:
            self.process_new_image(event.src_path)

    def process_new_image(self, path):
        filename = os.path.basename(path)
        thumbnail_path = os.path.join(self.target_dir, f"thmb-{filename}")

        try:
            with Image.open(path) as img:
                img.thumbnail((100, 100))
                img.save(thumbnail_path)
            print(f"Thumbnail created: {thumbnail_path}")
        except IOError as e:
            print(f"Failed to create thumbnail for {filename}: {e}")

if __name__ == "__main__":
    IMAGES_DIR
    THUMBNAILS_DIR

    patterns = ["*.jpg", "*.jpeg"]  # Only process JPEG images
    event_handler = ImageEventHandler(IMAGES_DIR, THUMBNAILS_DIR, patterns=patterns)
    observer = Observer()
    observer.schedule(event_handler, IMAGES_DIR, recursive=False)
    observer.start()
    print("Monitoring for new images...")

    try:
        observer.join()
    except KeyboardInterrupt:
        observer.stop()
    observer.join()