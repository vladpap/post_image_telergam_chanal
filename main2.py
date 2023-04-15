import os
import requests
import json
from pathlib import Path
from dotenv import load_dotenv


def extension_url_file(url):
    return os.path.splitext(url)[-1]


def save_images_from_url(url, path_name, params=None,):
    response = requests.get(url, params=params)
    response.raise_for_status()
        
    with open("".join([os.path.splitext(path_name)[0], extension_url_file(url)]), 'wb') as file:
        file.write(response.content)


def fetch_spacex_last_launch():
    id_last_launch = "5eb87d0dffd86e000604b35b"
    # TODO Найти последний id с фотографиями
    
    url_last_launch = f"https://api.spacexdata.com/v5/launches/{id_last_launch}"
    response = requests.get(url_last_launch)
    response.raise_for_status()
    links_photo = response.json()["links"]["flickr"]["original"]
    return links_photo


def fetch_nasa_random_photos(counts=40):
    url = "https://api.nasa.gov/planetary/apod"
    params = {"api_key": os.environ['NASA_API_KEY'], 
             "count": counts}
    response = requests.get(url=url, params=params)
    response.raise_for_status()
    # print(json.dumps(response.json(), indent=3))
    links_photo = []
    for nasa_json_response in response.json():
        link_photo = nasa_json_response["url"]
        if not(link_photo.find("https://apod.nasa.gov/apod/image")):
            links_photo.append(link_photo)

    return links_photo
        

def fetch_epic_photo():
    url = "https://api.nasa.gov/EPIC/api/enhanced"
    params = {"api_key": os.environ['NASA_API_KEY']}
    response = requests.get(url=url, params=params)
    response.raise_for_status()

    images_url = []
    for response_item in response.json():
        date_image = response_item["date"].split()[0].split('-')
        template_url_epic_photo = "https://api.nasa.gov/EPIC/archive/enhanced/{}/{}/{}/png/{}.png"
        images_url.append (template_url_epic_photo.format(date_image[0], date_image[1], date_image[2], response_item["image"]))

    return images_url


Path("images").mkdir(parents=True, exist_ok=True)
load_dotenv()
#token = os.getenv("NASA_API_KEY")
links_spacex_photo = fetch_spacex_last_launch()
count = 0
for link in links_spacex_photo:
    filename = "images/spacex_{}".format(count)
    save_images_from_url(link, filename)
    count += 1

links_nasa_photo = fetch_nasa_random_photos()
count = 0
for link in links_nasa_photo:
    filename = "images/nasa_apod_{}".format(count)
    save_images_from_url(link, filename)
    count += 1

links_epic_photo = fetch_epic_photo()

count = 0
params = {"api_key": os.environ['NASA_API_KEY']}
for link in links_epic_photo:
    filename = "images/nasa_epic_{}".format(count)
    save_images_from_url(link, filename, params=params)
    count += 1