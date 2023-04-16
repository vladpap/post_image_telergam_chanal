import os
import requests
import save_images_url
from dotenv import load_dotenv


def get_nasa_random_photos(counts=40):
    load_dotenv()
    url = "https://api.nasa.gov/planetary/apod"
    params = {"api_key": os.environ['NASA_API_KEY'], 
             "count": counts}
    response = requests.get(url=url, params=params)
    response.raise_for_status()

    links_photo = []
    for nasa_json_response in response.json():
        link_photo = nasa_json_response["url"]
        if not(link_photo.find("https://apod.nasa.gov/apod/image")):
            links_photo.append(link_photo)

    count = 0
    for link in links_photo:
        filename = "images/nasa_apod_{}".format(count)
        save_images_url.save_images_from_url(link, filename)
        count += 1


def main():
    get_nasa_random_photos(30)


if __name__ == "__main__":
    main()
    