#pip install pywin32
#pip install pillow
from io import BytesIO
import win32clipboard
from PIL import Image



def send_to_clipboard(clip_type, data):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(clip_type, data)
    win32clipboard.CloseClipboard()

filepath = 'C:/Users/hinnx27/Desktop/2024-02-28 11 15 46.png'
image = Image.open(filepath)
output = BytesIO()
image.convert("RGB").save(output, "BMP")
data = output.getvalue()[14:]
output.close()

send_to_clipboard(win32clipboard.CF_DIB, data)

# Ctrl + V 하면 됨..!