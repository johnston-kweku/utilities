import qrcode
import os

def generate_qr_code(data, filename):
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    image = qr.make_image(fill_color="black", back_color="white")
    os.makedirs('qrcodes', exist_ok=True)
    image.save(f'qrcodes/{filename}.png')




def main():
    while True:
        print('----------QRCODE GENERATOR----------')
        data = input('Enter url: ').strip()

        if not data:
            print("Enter a valid URL")
            continue

        filename = input('Enter file name without extenstion: ').strip()
        if not filename:
            filename = 'qr_code'

        
        generate_qr_code(data, filename)

        answer = input('Wanna generate another?: ').strip().lower()

        if answer not in ['yes', 'yep', 'yh', 'yeah']:
            print('Goodbye')
            break
        



main()