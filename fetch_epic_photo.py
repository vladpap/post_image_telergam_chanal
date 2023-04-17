import os
import requests
import random
import save_image_url
from dotenv import load_dotenv


def get_epic_photo(nasa_api_key):
    url = "https://api.nasa.gov/EPIC/api/enhanced"
    params = {"api_key": nasa_api_key}
    response = requests.get(url=url, params=params)
    response.raise_for_status()
    epic_json_contents = response.json()

    image_urls = []
    for epic_json_content in epic_json_contents:
        date_image = epic_json_content["date"].split()[0]
        template_url_epic_photo = "https://api.nasa.gov/EPIC/archive/enhanced/{}/{}/{}/png/{}.png"
        image_urls.append(template_url_epic_photo.format(
            date_image.split('-')[0],
            date_image.split('-')[1],
            date_image.split('-')[2],
            epic_json_content["image"]))

    params = {"api_key": nasa_api_key}
    save_image_url.save_image_from_url(
        random.choice(image_urls),
        "images/nasa_epic",
        params=params)


if __name__ == "__main__":
    load_dotenv()
    get_epic_photo(os.environ['NASA_API_KEY'])
