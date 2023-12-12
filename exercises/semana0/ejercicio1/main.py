"""
Imagina que en tu compañía llamada ImageDup se quiere probar el desempeño del
lenguaje Python con la manipulación de imágenes y el performance en APIs.

Todo esto porque en la empresa se ha trabajado previamente con lenguajes como
C+, C++ y Java. Para esto tu technical lead te pide a ti como Data Engineer de
la empresa que hagas una prueba de concepto (PoC) sobre la api
Imgflip: https://imgflip.com/api . Esta api proporciona imágenes a través de
un método GET (/get_memes) de memes aleatorios. Deberás obtener al menos una
imagen y guardarla en formato .jpeg en tu computadora.

Se te encomienda que generes un proceso sencillo corriendo un script de Python
llamado obtener_meme.py y la imagen de salida debería llamarse imagen_meme.jpeg.

Ayuda: Puedes hacer uso de la librería requests, PIL  y io
"""

import datetime
from pathlib import Path
import random

import requests


def main():
    url = "https://api.imgflip.com/get_memes"
    response = requests.get(url)

    if response.status_code != 200:
        raise ValueError(f"Invalid api url")

    response_json = response.json()
    img_list = response_json["data"]["memes"]
    img_url = random.choice(img_list)["url"]

    print(img_url)

    filename = datetime.datetime.now().strftime("%Y%m%d%H%M%S") + ".jpg"
    path = Path(__file__).resolve().parent / "output" / filename

    with open(path, 'wb') as f:
        content = requests.get(img_url).content
        f.write(content)


if __name__ == "__main__":
    main()
