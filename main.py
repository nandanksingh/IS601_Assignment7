# -----------------------------------------------------------------------------
# IS601 - Assignment 7: Dockerizing the QR Code Generator Application
# Author: Nandan Kumar
# -----------------------------------------------------------------------------

import sys
import qrcode
from dotenv import load_dotenv
import logging
from pathlib import Path
import os
import argparse
from datetime import datetime
import validators  # For URL validation

# ---------------------------------------------------------------------------
# Load environment variables from .env file (if present)
# ---------------------------------------------------------------------------
load_dotenv()

# ---------------------------------------------------------------------------
# Environment-based configuration
# ---------------------------------------------------------------------------
QR_DIRECTORY = os.getenv('QR_CODE_DIR', 'qr_codes')  # Directory to save QR codes
FILL_COLOR = os.getenv('FILL_COLOR', 'blue')          # Default fill color
BACK_COLOR = os.getenv('BACK_COLOR', 'white')        # Default background color

# ---------------------------------------------------------------------------
# Logging setup
# ---------------------------------------------------------------------------
def setup_logging():
    """Configure logging for both local and container execution."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[logging.StreamHandler(sys.stdout)]
    )

# ---------------------------------------------------------------------------
# Directory handling
# ---------------------------------------------------------------------------
def create_directory(path: Path):
    """Ensure target directory exists; create if necessary."""
    try:
        path.mkdir(parents=True, exist_ok=True)
        logging.info(f"Directory verified: {path}")
    except Exception as e:
        logging.error(f"Failed to create directory {path}: {e}")
        sys.exit(1)

# ---------------------------------------------------------------------------
# URL validation
# ---------------------------------------------------------------------------
def is_valid_url(url: str) -> bool:
    """Validate the provided URL using validators library."""
    if validators.url(url):
        return True
    else:
        logging.error(f"Invalid URL provided: {url}")
        return False

# ---------------------------------------------------------------------------
# QR code generation
# ---------------------------------------------------------------------------
def generate_qr_code(data: str, path: Path, fill_color: str, back_color: str):
    """Generate and save a QR code image for the provided data."""
    if not is_valid_url(data):
        logging.error("Aborting QR generation due to invalid URL.")
        return

    try:
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color=fill_color, back_color=back_color)

        with path.open("wb") as qr_file:
            img.save(qr_file)

        logging.info(f" QR code successfully saved to {path}")
    except Exception as e:
        logging.error(f" Error during QR code generation: {e}")

# ---------------------------------------------------------------------------
# Main entry point
# ---------------------------------------------------------------------------
def main():
    """Main execution logic: parse arguments, create directory, generate QR."""
    setup_logging()

    # Command-line argument parsing
    parser = argparse.ArgumentParser(description="Generate a QR code from a URL.")
    parser.add_argument(
        "--url",
        help="URL to encode in the QR code.",
        default="https://github.com/nandanksingh/IS601_Assignment7",
    )
    args = parser.parse_args()

    # Timestamped output filename
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    qr_filename = f"QRCode_{timestamp}.png"
    qr_output_dir = Path.cwd() / QR_DIRECTORY
    qr_full_path = qr_output_dir / qr_filename

    # Ensure directory exists and generate QR
    create_directory(qr_output_dir)
    generate_qr_code(args.url, qr_full_path, FILL_COLOR, BACK_COLOR)


if __name__ == "__main__":
    main()
