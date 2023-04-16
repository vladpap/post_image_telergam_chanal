import requests
import save_images_url
import argparse


def get_spacex_last_launch(id_launch="5eb87d0dffd86e000604b35b"):
    if id_launch == None:
    	id_launch = "5eb87d0dffd86e000604b35b"
    # TODO Найти последний id с фотографиями
    # test id 5eb87d42ffd86e000604b384
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
    

def main():
	arg_parser = argparse.ArgumentParser()
	arg_parser.add_argument('id_launch', nargs='?')
	id_launch = arg_parser.parse_args().id_launch
	get_spacex_last_launch(id_launch)


if __name__ == "__main__":
	main()
