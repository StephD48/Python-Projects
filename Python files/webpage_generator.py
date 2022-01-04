
from tkinter import *
import webbrowser as wb
from tkinter import filedialog as fd



f = open("web.html", "x")

message = """<html>
<body>
    <h1>
    Stay tuned for our amazing summer sale!
    </h1>
</body>
</html>"""
f.write(message)
f.close()


wb.open_new_tab('web.html')



