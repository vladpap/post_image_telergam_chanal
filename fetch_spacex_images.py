import requests
import save_image_url
import argparse


def get_spacex_last_launch(launch_id="5eb87d0dffd86e000604b35b"):
    launch_url = f"https://api.spacexdata.com/v5/launches/{launch_id}"
    response = requests.get(launch_url)
    response.raise_for_status()
    photo_links = response.json()["links"]["flickr"]["original"]

    for photo_number, photo_link in enumerate(photo_links):
        filename = "images/spacex_{}".format(photo_number)
        save_image_url.save_image_from_url(url=photo_link, path_name=filename)


def main():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument(
        'launch_id',
        nargs='?',
        default="5eb87d0dffd86e000604b35b",
        help="upload photos from id launch (default: upload last launch)")
    launch_id = arg_parser.parse_args().launch_id
    get_spacex_last_launch(launch_id)


if __name__ == "__main__":
    main()
