import cv2 as cv
import os
import math


def get_doc_size(path):
    try:
        size = os.path.getsize(path)
        return get_mb_size(size)
    except Exception as err:
        print(err)


def get_mb_size(bytes):
    bytes = float(bytes)
    mb = bytes / 1024 / 1024
    return mb


def delete_file(path):
    if file_exist(path):
        os.remove(path)
    else:
        pass

def file_exist(path):
    return os.path.exists(path)


def resize_rate(path, resize_path, fx, fy):
    image = read_image(path)
    im_resize = cv.resize(image, None, fx=fx, fy=fy)
    delete_file(resize_path)
    save_image(resize_path, im_resize)


def save_image(path, image):
    if not os.path.exists(os.path.dirname(path)):
        os.makedirs(os.path.dirname(path))
    cv.imwrite(path, image)


def read_image(path):
    return cv.imread(path)

def resize_image(path, resize_path, filesize):

    print("Resizing {}".format(path))
    print("Origin size: {:.4f} MB".format(get_doc_size(path)))

    size = get_doc_size(path)

    delete_file(resize_path)

    if size < filesize:
        image = read_image(path)
        save_image(resize_path, image)

    while size > filesize:
        rate = math.ceil((size / filesize) * 10) / 10 + 0.1
        rate = math.sqrt(rate)

        rate = 1.0 / rate
        if file_exist(resize_path):
            resize_rate(resize_path, resize_path, rate, rate)
        else:
            resize_rate(path, resize_path, rate, rate)
        size = get_doc_size(resize_path)

    print("Success! Saving to {}".format(resize_path))
    print("New image size: {:.4f} MB".format(get_doc_size(resize_path)))
    print("------------------------------")


def list_all_files(path):

    files = []
    for root, directories, filenames in os.walk(path):
        for filename in filenames:
            if filename != ".DS_Store":
                files.append(os.path.join(root, filename))
    return files

if __name__=="__main__":

    filesize = 0.3
    source_path = "/Users/lxc/project/aifighter/aifighter.github.io/origin_images"
    target_path = "/Users/lxc/project/aifighter/aifighter.github.io/source/images"
    source_files = list_all_files(source_path)
    target_files = [f.replace(source_path, target_path) for f in source_files]
    target_files = ['.'.join(f.split('.')[:-1] + ['jpg']) for f in target_files]
    for s, t in zip(source_files, target_files):
        if not os.path.exists(t):
            resize_image(s, t, filesize)