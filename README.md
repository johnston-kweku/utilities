README.md
Markdown
# Utilities 🛠️

A collection of lightweight, open-source Python utility scripts designed to handle everyday automation tasks. Currently, this repository features robust, production-ready command-line generators for both **1D Barcodes (Code 128 & EAN-13)** and **2D QR Codes**.

This project is built to be modular, fast, and dependency-light, serving as a reliable toolkit for developers, logistics testing, or asset management.

---

## 🚀 Features

- **Dynamic Barcode Generator (`barcode_generator.py`)**
  - High-density encoding using the **Code 128** standard.
  - Supports standard 12-digit retail codes (UPC/EAN format) as well as complex, long alphanumeric marketplace SKUs or serial numbers.
  - Automatically exports clean, high-resolution `.png` files into an organized directory structure.
- **Dynamic QR Code Generator (`qrcode_generator.py`)**
  - Generates highly scannable 2D matrix codes.
  - Capable of encoding URLs, text blocks, Wi-Fi configurations, or contact details.
- **Fail-Safe Execution**
  - Built-in validation to prevent script crashes on empty inputs or directory absence (`os.makedirs` handlers).

---

## 📋 System Requirements

- **Python 3.12+**
- Active internet connection (only for initial package installation)

---

## ⚙️ Installation & Setup

Follow these steps to get the utilities running locally on your machine.

### 1. Clone the Repository
```bash
git clone [https://github.com/yourusername/utilities.git](https://github.com/yourusername/utilities.git)
cd utilities
2. Set Up a Virtual Environment
Python 3.12+ does not bundle setuptools by default. Creating a fresh virtual environment ensures isolation:

Bash
# Create the virtual environment
python3 -m venv venv

# Activate the virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows (Command Prompt):
venv\Scripts\activate.bat
# On Windows (PowerShell):
venv\Scripts\Activate.ps1
3. Install Dependencies
Install the core encoding libraries along with pillow (required for image rendering) and setuptools (required for legacy package resolution backend mapping):

Bash
pip install --upgrade pip
pip install python-barcode qrcode pillow setuptools
🖥️ Usage
1. Barcode Generator
Run the script from your terminal within the activated virtual environment:

Bash
python barcode_generator.py
How it works:

Enter your alphanumeric SKU, serial number, or numeric string (e.g., GE779EA4ELH12NAFAMZ-353970692 or 871256188013).

Input a preferred filename.

The script ensures a barcodes/ directory exists and saves your asset inside it as a .png file.

2. QR Code Generator
Run the companion script for 2D matrix generation:

Bash
python qrcode_generator.py
How it works:

Paste your target URL or string data, provide a filename, and look inside the generated qrcodes/ output folder.

📂 Repository Structure
Plaintext
utilities/
│
├── barcodes/               # Output folder for generated barcodes (Auto-generated)
├── qrcodes/                # Output folder for generated QR codes (Auto-generated)
│
├── barcode_generator.py    # Core 1D barcode script
├── qrcode_generator.py     # Core 2D QR code script
│
├── venv/                   # Local virtual environment (Git-ignored)
└── README.md               # Repository documentation
🤝 Contributing
This is an open-source utility hub! We welcome optimizations, bug fixes, and entirely new utility scripts (e.g., PDF processors, image optimizers, secure token generators).

Fork the Project.

Create your Feature Branch (git checkout -b feature/AmazingUtility).

Commit your Changes (git commit -m 'Add some AmazingUtility').

Push to the Branch (git push origin feature/AmazingUtility).

Open a Pull Request.

📄 License
Distributed under the MIT License. See LICENSE for more information.