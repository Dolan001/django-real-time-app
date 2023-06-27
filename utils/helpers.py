from io import BytesIO
from django.core.files import File
from PIL import Image, ImageOps  # pillow for image compression
def image_compress(file, q):
    """
    Image size compression
    """
    try:
        im = Image.open(file)
        image = im.convert('RGB')
        image = ImageOps.exif_transpose(image)
        im_io = BytesIO()
        image.save(im_io, im.format, quality=q, width=image.width, height=image.height,optimize=True)

        return File(im_io, name=file.name)
    except IOError:
        return file