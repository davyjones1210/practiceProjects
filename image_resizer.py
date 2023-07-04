#Install pillow if you haven't
#Import pillow
#Open up the image we want to resize using python
#print the current size of that image
#specify the size we want to change it to
#Save the new resized image

from PIL import Image

def resized_image(size1, size2):
    image = Image.open('IMG_E4829.jpg')
    print(f"Current size: {image.size}")

    resized_image = image.resize((size1, size2))

    resized_image.save('IMG_E4829_Resized-'+ str(size1) + 'x' + str(size2) +'.jpg')

size1 = int(input('Enter width: '))
size2 = int(input('Enter length: '))

resized_image(size1, size2)

