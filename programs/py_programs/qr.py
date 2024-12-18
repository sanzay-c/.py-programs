import qrcode

qr = qrcode.make(
    'https://www.google.com/'
)

qr.save('myQRcode.png')
qr.show()