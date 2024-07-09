import pytesseract
from PIL import Image

print("Do not forget to input the type of image too (.png/.jpeg)")

path=str(input("Enter path to image file"))

text=pytesseract.image_to_string(path)

print("Here is the extracted text from the provided image")
print(text)
im= Image.open(path)
im.show()
