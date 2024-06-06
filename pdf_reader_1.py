import numpy as np
from pdfreader import SimplePDFViewer, PageDoesNotExist


you_pdf_file_name = "test.pdf"

fd = open(you_pdf_file_name, "rb")
viewer = SimplePDFViewer(fd)

plain_text = ""
pdf_markdown = ""
images = []
try:
    while True:
        viewer.render()
        #print(viewer.canvas.text_content)
        #pdf_markdown += viewer.canvas.text_content
        #plain_text += "".join(viewer.canvas.strings)
        print(viewer.canvas.strings)
        #images.extend(viewer.canvas.inline_images)
        #images.extend(viewer.canvas.images.values())
        viewer.next()
except PageDoesNotExist:
    pass


