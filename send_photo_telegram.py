import os
import telegram
from dotenv import load_dotenv
from random import choice
from time import sleep
import argparse


def send_photo_chanal(path_image):
	load_dotenv()
	bot = telegram.Bot(token=os.environ['TOKEN_BOT'])
	chat_id = os.environ["CHAT_ID"]
	time_of_post = int(os.environ['TIME_OF_POST'])

	if path_image != None:
		bot.send_photo(chat_id=chat_id, photo=open(path_image, 'rb'))
		return

	while True:
	    images_files = os.listdir('images/')
	    post_images_files = []

	    while len(images_files) > 0:
	        post_image = choice(images_files)
	        bot.send_photo(chat_id=chat_id, photo=open('images/{}'.format(post_image), 'rb'))
	        post_images_files.append(post_image)
	        images_files.remove(post_image)
	        sleep(time_of_post)


def main():
	arg_parser = argparse.ArgumentParser()
	arg_parser.add_argument('path_image', nargs='?')
	path_image = arg_parser.parse_args().path_image
	send_photo_chanal(path_image)


if __name__ == "__main__":
	main()
