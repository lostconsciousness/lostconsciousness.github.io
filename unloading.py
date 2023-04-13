import requests
import time

while(True):
    response = requests.get(
        "https://anix.salesdrive.me/export/yml/export.yml?publicKey=fl6yiRQy6G170JBBaa7eFQehljUhWWgNxHpuiPpH03IgQWVb5z98Jw6SBhIj"
    )
    with open("media/final.xml", "w+", encoding="utf-8") as file:
        file.write(response.text)
    time.sleep(3600)
    