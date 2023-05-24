from    coloda import Coloda
from    pathlib import Path
import  matplotlib.pyplot as plt
import  matplotlib.image as mpimg
from matplotlib.widgets import Button

coloda = Coloda()

path = Path('.').joinpath('cards')

def _yes():
    return next(coloda.deal_card())

figure, axes_list = plt.subplots(nrows=4, ncols=13)

for axes in axes_list.ravel(): # мне кажется что цикл здесь не нужен(могу ошибаться)
    coloda.shuffle()
    axes.get_xaxis().set_visible(False)
    axes.get_yaxis().set_visible(False)
        
    image_name = str(_yes().image_name)
    img = mpimg.imread(str(path.joinpath(image_name).resolve()))
    axes.imshow(img)
    
    
figure.tight_layout()# Не понял

def func(next_card): #  Как написать логику?
    print()

axcut = plt.axes([0.9, 0.0, 0.1, 0.075])
bcut = Button(axcut, 'Next Cart', color='red', hovercolor='green')    
bcut.on_clicked(func())
plt.show()