import fetch_spacex_images
import fetch_nasa_photos
import fetch_epic_photo
import argparse


def create_arg_parser():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('id_launch', nargs='?')
    return arg_parser

arg_parser = create_arg_parser()
id_launch = arg_parser.parse_args().id_launch
fetch_spacex_images.get_spacex_last_launch(id_launch)   # test id 5eb87d42ffd86e000604b384

fetch_nasa_photos.get_nasa_random_photos(10)

fetch_epic_photo.get_epic_photo()
