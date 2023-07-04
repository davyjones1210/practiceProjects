#install all the libraries needed
#create a function that collects text and converts to qr code
#save the qr code as an image
#run the function

import qrcode

def generate_qrcode(text_url):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(text_url)
    qr.make(fit=True)
    img = qr.make_image()
    img.save("qrimg001.png")

url = input("Enter your url: ")
generate_qrcode(url)


