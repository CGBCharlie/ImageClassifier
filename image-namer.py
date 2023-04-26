import os
from PIL import Image
directory = 'images/ducks'

i = 1
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f):
        image = Image.open(f)
        new_image = image.resize((500, 500))
        new_image.save('images/ducks/duck_{}.jpg'.format(i))
        i+=1