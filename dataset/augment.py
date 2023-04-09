import os
import random
from PIL import Image, ImageOps

def augment_image(image, rotation_angle, translate_x, translate_y, fill_color=(255, 255, 255)):
    rotated_image = image.rotate(rotation_angle, fillcolor=fill_color)
    translated_image = ImageOps.expand(rotated_image, border=max(abs(translate_x), abs(translate_y)), fill=fill_color)
    translated_image = translated_image.transform(translated_image.size, Image.AFFINE, (1, 0, translate_x, 0, 1, translate_y))
    cropped_image = translated_image.crop((0, 0, image.size[0], image.size[1]))
    return cropped_image

train_data_path = "./train"
test_data_path = "./test"
augment_train_path = "./augmented_train"
augment_test_path = "./augmented_test"

rotation_range = (-10, 10)  # Define the range of rotation angles (degrees)
translation_range_x = (-2, 2)  # Define the range of translation in x-axis (pixels)
translation_range_y = (-2, 2)  # Define the range of translation in y-axis (pixels)

def read_file(input_path, output_path, output_bundle_size):
    for foldername in os.listdir(input_path):
        bundle_path = os.path.join(input_path, foldername)
        if os.path.isdir(bundle_path):
            for i in range(output_bundle_size):
                os.makedirs(f'{output_path}\{foldername}_{i}', exist_ok=True)

            for file_name in os.listdir(bundle_path):
                image = Image.open(f'{input_path}\{foldername}\{file_name}')

                for i in range(output_bundle_size):
                    random_angle = random.randint(*rotation_range)
                    random_translate_x = random.randint(*translation_range_x)
                    random_translate_y = random.randint(*translation_range_y)
                    augmented_image = augment_image(image, random_angle, random_translate_x, random_translate_y)

                    augmented_image.save(f'{output_path}\{foldername}_{i}\{file_name}')

read_file(input_path=train_data_path, output_path=augment_train_path, output_bundle_size=5)
