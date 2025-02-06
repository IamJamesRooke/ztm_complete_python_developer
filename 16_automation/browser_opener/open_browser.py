import webbrowser
from datetime import datetime

# Get the current time
current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# URL to open
url = 'https://www.example.com'

# Log the current time to the file

# Path to the log file on the desktop
log_file_path = r'D:\OneDrive\Desktop\log.txt'

try:
    with open(log_file_path, 'a') as log_file:
        log_file.write(f'{url} opened at: {current_time}\n')
except Exception as e:
    print(f"Failed to write to log file: {e}")

# Open the web browser with the specified URL
try:
    webbrowser.open(url)
except Exception as e:
    print(f"Failed to open web browser: {e}")
