import os
import fetch_spacex_images
import fetch_nasa_photos
import fetch_epic_photo
from dotenv import load_dotenv


def main():
    load_dotenv()
    fetch_spacex_images.get_spacex_last_launch()
    fetch_nasa_photos.get_nasa_random_photos(os.environ['NASA_API_KEY'])
    fetch_epic_photo.get_epic_photo(os.environ['NASA_API_KEY'])


if __name__ == "__main__":
    main()
