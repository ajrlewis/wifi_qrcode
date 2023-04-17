# wifi_qrcode

Script to generate a 800×1200 pixel WIFI credentials.

## Environmental Variables

Include a `.env` file in the with the following key-value pairs:

```bash
NETWORK="your-ssid"
PASSWORD="your-password"
FILENAME="filename-of-image"
```

## Installation

```bash
git clone https://github.com/ajrlewis/wifi_qrcode.git
cd wifi_qrcode
python3.11 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

## Usaage

Assuming you are in the root directory with a valid `.env` file:

```bash
python3 wifi_qrcode/wifi_qrcode.py
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
