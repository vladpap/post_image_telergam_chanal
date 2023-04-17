import os
import telegram
from dotenv import load_dotenv
from random import choice
from time import sleep
import argparse


def send_photo_channel(token, chat_id, time_of_post, path_image):
    bot = telegram.Bot(token=token)
    time_of_post = time_of_post

    if path_image:
        with open(path_image, 'rb') as photo_read:
            bot.send_photo(chat_id=chat_id, photo=photo_read)
        return

    while True:
        images_files = os.listdir('images/')
        image_post_files = []

        while images_files:
            post_image = choice(images_files)
            with open('images/{}'.format(post_image), 'rb') as image_read:
                bot.send_photo(chat_id=chat_id, photo=image_read)
            image_post_files.append(post_image)
            images_files.remove(post_image)
            sleep(time_of_post)


def main():
    load_dotenv()
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument(
        'image_path',
        nargs='?',
        help="send photo in telegram chanal (default: send photo fron images/)")
    image_path = arg_parser.parse_args().image_path
    send_photo_channel(
        os.environ['TOKEN_BOT_TELEGRAM'],
        os.environ["CHAT_ID_TELEGRAM"],
        int(os.environ['TIME_OF_POST']),
        image_path)


if __name__ == "__main__":
    main()
