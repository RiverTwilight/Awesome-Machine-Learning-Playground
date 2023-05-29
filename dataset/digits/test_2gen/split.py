import os
from PIL import Image

def split_image(image_path, save_dir):
    # Open the image file
    img = Image.open(image_path)

    # Check if the image is of the desired size
    width, height = img.size
    if width != 28 or height != 84:
        print(f'Skipped {image_path} due to incorrect size.')
        return
    
    # Calculate the height of each sub-image
    sub_img_height = height // 3

    # Split the image and save each part
    for i in range(3):
        start = i * sub_img_height
        end = (i + 1) * sub_img_height
        sub_img = img.crop((0, start, 28, end))
        base_name = os.path.basename(image_path)
        base_name_without_ext = os.path.splitext(base_name)[0]
        sub_img_path = os.path.join(save_dir, f'{base_name_without_ext}_part{i}.png')
        sub_img.save(sub_img_path)
        print(f'Saved {sub_img_path}.')

def split_images_in_folder(folder_path, save_dir):
    # Ensure save directory exists
    os.makedirs(save_dir, exist_ok=True)

    # List all files in the directory
    for filename in os.listdir(folder_path):
        if filename.endswith('.png'):
            image_path = os.path.join(folder_path, filename)
            split_image(image_path, save_dir)

# Call function on your folder
split_images_in_folder('dataset/test_2gen/out', 'dataset/test_2gen/processd')
