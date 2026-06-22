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