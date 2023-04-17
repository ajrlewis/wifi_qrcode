import os
from dotenv import load_dotenv
from PIL import Image, ImageDraw, ImageFont
import qrcode

load_dotenv()


def _create_qrcode(
    ssid: str, password: str, authentication_type: str = "WPA", hidden: bool = True
):
    data = f"WIFI:T:{authentication_type};S:{ssid};P:{password};H:true;"
    qr_code = qrcode.QRCode()
    qr_code.add_data(data)
    qr_code.make_image().save("data/qrcode.png")


def create(ssid: str, password: str, filename: str):

    _create_qrcode(ssid=ssid, password=password)

    wifi_icon = Image.open("data/icon-wifi.png")
    key_icon = Image.open("data/icon-key.png")
    qrcode = Image.open("data/qrcode.png")

    width = 800
    height = 1200
    image = Image.new("RGB", (width, height), "white")

    wifi_x = (width - wifi_icon.width) // 2
    wifi_y = 180
    image.paste(wifi_icon, (wifi_x, wifi_y))

    font = ImageFont.truetype("data/arial/arial-bold.ttf", 36)
    draw = ImageDraw.Draw(image)
    ssid_x = (width - font.getsize(ssid)[0]) // 2
    ssid_y = wifi_y + wifi_icon.height + 20
    draw.text((ssid_x, ssid_y), ssid, font=font, fill="black")

    font = ImageFont.truetype("data/arial/arial.ttf", 36)
    key_x = (width - key_icon.width - font.getsize(password)[0] - 10) // 2
    key_y = ssid_y + font.getsize(ssid)[1] + 20
    image.paste(key_icon, (key_x, key_y))
    password_x = key_x + key_icon.width + 10
    password_y = key_y + (key_icon.height - font.getsize(password)[1]) // 2
    draw.text((password_x, password_y), password, font=font, fill="black")

    qrcode_x = (width - qrcode.width) // 2
    qrcode_y = key_y + key_icon.height + 20
    image.paste(qrcode, (qrcode_x, qrcode_y))

    image.save(filename)


def main():
    ssid = os.getenv("NETWORK")
    password = os.getenv("PASSWORD")
    filename = os.getenv("FILENAME")
    create(ssid=ssid, password=password, filename=filename)

if __name__ == "__main__":
    main()
