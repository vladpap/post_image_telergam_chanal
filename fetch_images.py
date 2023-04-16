import fetch_spacex_images
import fetch_nasa_photos
import fetch_epic_photo


def main():
    fetch_spacex_images.get_spacex_last_launch()   
    fetch_nasa_photos.get_nasa_random_photos()
    fetch_epic_photo.get_epic_photo()


if __name__ == "__main__":
    main()
