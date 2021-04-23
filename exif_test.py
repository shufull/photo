from PIL import Image
from PIL.ExifTags import TAGS

def get_exif(file):
	im = Image.open(file)

	try:
		exif = im._getexif()
	except:
		return {}

	exif_table = {}
	for tag_id, value in exif.items():
		tag = TAGS.get(tag_id, tag_id)
		exif_table[tag] = value

	return exif_table

print(get_exif("NZ6_7010.jpg"))
