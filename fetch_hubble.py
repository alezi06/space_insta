import os
import requests


def get_image_type(link):
    return link.split('.')[-1]

def download_image(image_id):
    url = 'http://hubblesite.org/api/v3/image/{}'.format(image_id)

    response = requests.get(url).json()
    image_link = response['image_files'][-1]['file_url']

    file_path = './images/{}.{}'.format(image_id, get_image_type(image_link))
    response = requests.get(image_link)

    with open(file_path, 'wb') as file:
        file.write(response.content)


def fetch_hubble_collection_images():
    url = 'http://hubblesite.org/api/v3/images?page=all&collection_name=spacecraft'
    response = requests.get(url)

    os.makedirs('./images/', exist_ok=True)

    for image in response.json():
        download_image(image['id'])


if __name__ == '__main__':
    fetch_hubble_collection_images()