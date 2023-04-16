import os
import requests
import random
import save_images_url
from dotenv import load_dotenv


def get_epic_photo():
    load_dotenv()
    url = "https://api.nasa.gov/EPIC/api/enhanced"
    params = {"api_key": os.environ['NASA_API_KEY']}
    response = requests.get(url=url, params=params)
    response.raise_for_status()

    images_url = []
    for response_item in response.json():
        date_image = response_item["date"].split()[0].split('-')
        template_url_epic_photo = "https://api.nasa.gov/EPIC/archive/enhanced/{}/{}/{}/png/{}.png"
        images_url.append(template_url_epic_photo.format(date_image[0], date_image[1], date_image[2], response_item["image"]))

    params = {"api_key": os.environ['NASA_API_KEY']}
    save_images_url.save_images_from_url(random.choice(images_url), "images/nasa_epic", params=params)


if __name__ == "__main__":
    get_epic_photo()
