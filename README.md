# Templates Repository

This repository stores short Python, JavaScript, and HTML templates used to support my son's art website on AWS. The focus is on automation and simplification of website updates, catering especially to individuals who might not be familiar with HTML or web development practices.

## image_upload_thumbnail.py

The `image_upload_thumbnail.py` script automates the process of updating the website when new artwork is added. It's particularly useful for non-technical users tasked with maintaining the site's content.

### Prerequisites

- **Python Version**: The script is compatible with Python version 3.12.
- **Environment**: Designed to run in a Windows environment, adjustments may be required for other operating systems.
- **Dependencies**:
  - `PIL` (Python Imaging Library) for image processing.
  - `watchdog` for monitoring file system events.

### How It Works

1. **Image Drop**: When an image file with a `.jpg` extension is placed in the directory named "images," the script automatically detects this new file.
2. **Thumbnail Creation**: Upon detection, `image_upload_thumbnail.py` generates a thumbnail version of the image and saves it in a directory named "thumbnails."
3. **Continuous Monitoring**: The script runs indefinitely, continuously monitoring the "images" directory for new additions. It only stops if the user manually terminates the process or an unexpected error occurs.

### Note

- The script ensures thumbnails are created for new images, facilitating easier and automated updates to the website. This automation helps maintain the site's gallery with minimal technical intervention.
- **Manual Termination**: To stop the script, a keyboard interrupt (Ctrl+C) in the command line where the script is running will safely terminate the process.