import os
import barcode
from barcode.writer import ImageWriter

def generate_barcode(data, filename):

    os.makedirs('barcodes', exist_ok=True)
    
    EAN = barcode.get_barcode_class('ean13')

    ean = EAN(data, writer=ImageWriter())
    ean.save(f'barcodes/{filename}')
    print(f"Barcode successfully saved to barcodes/{filename}.png")

def main():
    while True:
        print('\n----------BARCODE GENERATOR----------')
        data = input('Enter 12 digit number: ').strip()

        if not data.isdigit() or len(data) != 12:
            print("❌ Error: Enter a valid 12 digit number")
            continue

        filename = input('Enter file name without extension: ').strip()
        if not filename:
            filename = 'barcode'
        
        try:
            generate_barcode(data, filename)
        except Exception as e:
            print(f"❌ Failed to generate barcode: {e}")

        answer = input('Wanna generate another? (y/n): ').strip().lower()
        if answer not in ['yes', 'yep', 'yh', 'yeah', 'y']:
            print('Goodbye!')
            break

if __name__ == "__main__":
    main()