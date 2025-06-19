import qrcode

link = "sgnl://linkdevice?uuid=GJJcZtcGzLoTDK7I7ly-Rg%3D%3D&pub_key=BbpNeQspnd6rZngDH6frWRgNXft2FUbzgvkKmeqw3btl"
img = qrcode.make(link)
img.show()  # Opens default image viewer
img.save("signal_qr.png")
