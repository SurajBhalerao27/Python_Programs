import segno
qrcode = segno.make_qr("कर सर्वशक्तीनीशी")
qrcode.save(
    "MyQRCode.png",
    scale=10,
)