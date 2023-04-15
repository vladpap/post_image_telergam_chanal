import os
import requests
from pathlib import Path


def extension_url_file(url):
    return os.path.splitext(url)[-1]


def save_images_from_url(url, path_name, params=None):
    Path("images").mkdir(parents=True, exist_ok=True)

    response = requests.get(url, params=params)
    response.raise_for_status()
    name_file = os.path.splitext(path_name)[0]
    extension_file = os.path.splitext(url)[-1]
    path_name_file = "".join([name_file, extension_file])
    with open(path_name_file, 'wb') as file:
        file.write(response.content)
