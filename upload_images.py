import os
from dotenv import load_dotenv
from instabot import Bot


def main():
    load_dotenv()
    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')

    bot = Bot()
    bot.login(username=login, password=password)

    images_list = os.listdir('images')

    for image in images_list:
        image_path = 'images/{}'.format(image)
        bot.upload_photo(image_path)
        

if __name__ == '__main__':
    main()