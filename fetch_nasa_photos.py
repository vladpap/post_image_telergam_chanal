import os
import requests
import save_image_url
from dotenv import load_dotenv


def get_nasa_random_photos(nasa_api_key, counts=40):
    url = "https://api.nasa.gov/planetary/apod"
    params = {"api_key": nasa_api_key, "count": counts}
    response = requests.get(url=url, params=params)
    response.raise_for_status()

    photo_links = []
    for nasa_json_response in response.json():
        photo_link = nasa_json_response["url"]
        if not (photo_link.find("https://apod.nasa.gov/apod/image")):
            photo_links.append(photo_link)

    for photo_number, photo_link in enumerate(photo_links):
        filename = "images/nasa_apod_{}".format(photo_number)
        save_image_url.save_image_from_url(photo_link, filename)


def main():
    load_dotenv()
    get_nasa_random_photos(os.environ['NASA_API_KEY'], 10)


if __name__ == "__main__":
    main()
