import qrcode as qr

img =qr.make("https://youtu.be/au5uNkCKzaY?si=QemQTizyWGi72K43")
img = img.save("qrcode.png")