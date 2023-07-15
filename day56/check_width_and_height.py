from PIL import Image

class Image_ch:
    
    new_width  = 500
    new_height = 500
    def __init__(self, image) -> None:
        self.url = image
        self.image = Image.open(image)
        self.new_width  = 500
        self.new_height = 500
    
    
    def save(self):
        img = self.image.resize((self.new_width, self.new_height), Image.ANTIALIAS)
        x = []
        for elem in self.url[::-1]:
            if elem != "/":
                x.extend(elem)
                continue
            else:
                break 
        res = "".join(x[::-1])
        img.save("C:/Users/ASUS/Desktop/HomeWorkDavid/day56/image/image_pr/"+res)
        return "C:/Users/ASUS/Desktop/HomeWorkDavid/day56/image/image_pr/"+res