import os

def get_image_path(*args):
    return os.path.join(os.path.abspath('.'), 'images', *args)


def get_image_type(link):
    return link.split('.')[-1]