import os
import requests
from helpers import get_image_type, get_image_path


def download_image(image_id):
    url = 'http://hubblesite.org/api/v3/image/{}'.format(image_id)

    response = requests.get(url).json()
    image_link = response['image_files'][-1]['file_url']

    image_type = get_image_type(image_link)
    file_path = get_image_path('{}.{}'.format(image_id, image_type))
    response = requests.get(image_link)

    with open(file_path, 'wb') as file:
        file.write(response.content)


def fetch_hubble_collection_images():
    url = 'http://hubblesite.org/api/v3/images?page=all&collection_name=spacecraft'
    response = requests.get(url)

    os.makedirs(get_image_path(), exist_ok=True)

    for image in response.json():
        download_image(image['id'])


if __name__ == '__main__':
    fetch_hubble_collection_images()