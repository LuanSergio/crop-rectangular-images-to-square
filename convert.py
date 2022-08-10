from PIL import Image

def crop_center(pil_img, crop_width, crop_height):
    img_width, img_height = pil_img.size
    return pil_img.crop(((img_width - crop_width) // 2,
                         (img_height - crop_height) // 2,
                         (img_width + crop_width) // 2,
                         (img_height + crop_height) // 2))


def crop_max_square(pil_img):
    return crop_center(pil_img, min(pil_img.size), min(pil_img.size))
    
imagesQuantity = 166;

for x in range(imagesQuantity):
    image=Image.open('./images/image-' + str(x + 1) + '.jpeg')
    im_new = crop_max_square(image)
    im_new.save('./converted/image-' + str(x + 1) + '.jpeg', quality=95)