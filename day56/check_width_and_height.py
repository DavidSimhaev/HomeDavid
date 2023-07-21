from PIL import Image
import os
class Image_ch:
    
    new_width  = 500
    new_height = 500
    def __init__(self, image) -> None:
        self.url = image
        self.image = Image.open(image)
        self.new_width  = 500
        self.new_height = 500
        self.url_l = os.path.dirname(os.path.abspath(__file__)).replace("\\", "/")

    def save(self):
        img = self.image.resize((self.new_width, self.new_height), Image.LANCZOS)
        x = []
        for elem in self.url[::-1]:
            if elem != "/":
                x.extend(elem)
                continue
            else:
                break 
        res = "".join(x[::-1])
        img.save(f"{self.url_l}/image/image_pr/"+res)
        return f"{self.url_l}/image/image_pr/"+res