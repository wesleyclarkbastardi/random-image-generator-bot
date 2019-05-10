from PIL import Image
import random
import tweepy
import os

os.chdir(os.path.dirname(__file__))


def create_row(color, num_of_rows=112, num_of_columns=600):
    matrix = [color for x in range(num_of_columns) for y in range(num_of_rows)]
    return matrix


def create_random_rgb_tuple():
    random_r = random.randint(0, 256)
    random_g = random.randint(0, 256)
    random_b = random.randint(0, 256)
    random_tuple = (random_r, random_g, random_b)
    return random_tuple


def rgb_to_hex(rgb_tuple):
    hex_string = '%02X%02X%02X' % rgb_tuple
    return '0x' + hex_string


def create_three_rows():
    first_row_tuple = create_random_rgb_tuple()
    second_row_tuple = create_random_rgb_tuple()
    third_row_tuple = create_random_rgb_tuple()
    if first_row_tuple == second_row_tuple or first_row_tuple == third_row_tuple or second_row_tuple == third_row_tuple:
        create_three_rows()
    else:
        first_row = create_row(first_row_tuple)
        second_row = create_row(second_row_tuple)
        third_row = create_row(third_row_tuple)
        temp_row = first_row
        temp_row.extend(second_row)
        temp_row.extend(third_row)
        return temp_row, first_row[0], second_row[0], third_row[0]


three_rows, first_row_value, second_row_value, third_row_value = create_three_rows()

first_row_hex = rgb_to_hex(first_row_value)
second_row_hex = rgb_to_hex(second_row_value)
third_row_hex = rgb_to_hex(third_row_value)
img = Image.new("RGBA", (600, 336))
img.putdata(three_rows)

random_file_number = random.randint(1, 1000000)
file_name = 'img_' + str(random_file_number) + '.png'
img.save(file_name)

# personal information
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

# authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
tweet = first_row_hex + "\n" + second_row_hex + "\n" + third_row_hex
image_path = file_name

# to attach the media file
api.update_with_media(image_path, status = tweet)

#delete file
os.remove(file_name)
