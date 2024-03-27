import sys
import qrcode
from dotenv import load_dotenv
import logging.config
from pathlib import Path
import os

# Load environment variables
load_dotenv()

# Environment Variables
# URL for QR code
DATA_URL = os.getenv('QR_DATA_URL', 'https://github.com/tabrezdn1')
# Directory for saving QR code
QR_DIRECTORY = os.getenv('QR_CODE_DIR', 'qr_code')
# Filename for the QR code
QR_FILENAME = os.getenv('QR_CODE_FILENAME', 'MyQRCode2.png')
 # Fill color for the QR code
FILL_COLOR = os.getenv('FILL_COLOR', 'black')
 # Background color for the QR code
BACK_COLOR = os.getenv('BACK_COLOR', 'white')

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(sys.stdout),  
        ]
    )


def create_directory(path: Path):
    try:
        path.mkdir(parents=True, exist_ok=True)
    except Exception as e:
        logging.error(f"Failed to create directory {path}: {e}")
        exit(1)

def generate_qr_code(data, path, fill_color='red', back_color='white'):
    try:
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color=fill_color, back_color=back_color)

        with path.open('wb') as qr_file:
            img.save(qr_file)
        logging.info(f"QR code successfully saved to {path}")

    except Exception as e:
        logging.error(f"An error occurred while generating or saving the QR code: {e}")

def main():
    # Initial logging
    setup_logging()

    qr_code_full_path = Path.cwd() / QR_DIRECTORY / QR_FILENAME

    create_directory(qr_code_full_path.parent)

    generate_qr_code(DATA_URL, qr_code_full_path, FILL_COLOR, BACK_COLOR)

if __name__ == "__main__":
    main()