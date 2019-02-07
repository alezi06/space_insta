import os
import requests


def fetch_spacex_last_launch():
    url = 'https://api.spacexdata.com/v3/launches/latest'

    response = requests.get(url).json()
    image_links_list = response['links']['flickr_images']

    os.makedirs('./images/', exist_ok=True)

    for image_number, image_link in enumerate(image_links_list, 1):
        file_path = './images/spacex{}.jpg'.format(image_number)
        response = requests.get(image_link)

        with open(file_path, 'wb') as file:
            file.write(response.content)


if __name__ == '__main__':
    fetch_spacex_last_launch()