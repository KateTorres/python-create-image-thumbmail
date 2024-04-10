# This script monitors, written in Python, monitors one directory. 
# When file with jpg extention is dropped in that directory, the script creates a thumbnail.

# File must can be dropped using a mouse or copy-pasted. 

# The script is useful for autoamted updates of a website. 

import os  # For operating system interactions
from PIL import Image  # Python Imaging Library for image processing
from watchdog.observers import Observer  # For monitoring filesystem events
from watchdog.events import PatternMatchingEventHandler  # For handling specific file patterns
import time  # To add delays

# Name your directories
IMAGES_DIR = r"C:\projects\templates\images"
THUMBNAILS_DIR = r"C:\projects\templates\thumbnails"

class ImageEventHandler(PatternMatchingEventHandler):
    def __init__(self, source_dir, target_dir, patterns=None):
        super().__init__(patterns=patterns)
        self.source_dir = os.path.abspath(source_dir)
        self.target_dir = os.path.abspath(target_dir)
        os.makedirs(self.target_dir, exist_ok=True)  # Ensure target directory exists

    def on_created(self, event):
        super(ImageEventHandler, self).on_created(event)
        # Process only if it's an image file in the source directory
        if os.path.dirname(os.path.abspath(event.src_path)) == self.source_dir:
            self.process_new_image(event.src_path)

    def process_new_image(self, path):
        filename = os.path.basename(path)
        thumbnail_path = os.path.join(self.target_dir, f"thmb-{filename}")

        # Attempt to open and process the image with retries
        for attempt in range(5):  # Try up to 5 times
            try:
                with Image.open(path) as img:
                    img.thumbnail((100, 100))
                    img.save(thumbnail_path)
                print(f"Thumbnail created: {thumbnail_path}")
                break  # Success, exit the loop
            except IOError as e:
                print(f"Attempt {attempt + 1}: Failed to create thumbnail for {filename}: {e}")
                time.sleep(1)  # Wait for 1 second before retrying
            except Exception as e:
                print(f"Unexpected error creating thumbnail for {filename}: {e}")
                break  # Exit the loop on unexpected errors
        else:
            print(f"Failed to create thumbnail for {filename} after multiple attempts.")

if __name__ == "__main__":
    patterns = ["*.jpg", "*.jpeg"]  # Only process JPEG images
    event_handler = ImageEventHandler(IMAGES_DIR, THUMBNAILS_DIR, patterns=patterns)
    observer = Observer()
    observer.schedule(event_handler, IMAGES_DIR, recursive=False)
    observer.start()
    print("Monitoring for new images...")

    # The script will continue running until manually stopped
    observer.join()