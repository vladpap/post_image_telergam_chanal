import os
import requests
import save_images_url


def get_spacex_last_launch(id_launch="5eb87d0dffd86e000604b35b"):
    
    # TODO Найти последний id с фотографиями
    id_last_launch = id_launch

    url_last_launch = f"https://api.spacexdata.com/v5/launches/{id_last_launch}"
    response = requests.get(url_last_launch)
    response.raise_for_status()
    links_photo = response.json()["links"]["flickr"]["original"]

    count = 0
    for link in links_photo:
        filename = "images/spacex_{}".format(count)
        save_images_url.save_images_from_url(url=link, path_name=filename)
        count += 1
    