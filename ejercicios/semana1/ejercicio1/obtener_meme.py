from io import BytesIO
import os
import random

import requests
from PIL import Image


def main():
	url = "https://api.imgflip.com/get_memes"
	response = requests.get(url)
	data = response.json()

	if not data or not data["success"]:
		raise ValueError("Invalid data received")

	memes = data["data"]["memes"]
	meme = random.choice(memes)
	meme_url = meme["url"]

	response = requests.get(meme_url)
	img = Image.open(BytesIO(response.content))
	img.save("imagen_meme.jpg", "JPEG")

	os.system(f"open imagen_meme.jpg")


if __name__ == "__main__":
	main()
