import matplotlib.pyplot as plt
import numpy as np
import random
import seaborn as sns 

rolls = [random.randrange(1,7) for i in range(600)]
values, frequenies = np.unique(rolls, return_counts= True)


title = f"Rolling a dice{len(rolls):,} Times"

sns.set_style("whitegrid")

axes = sns.barplot(x=values, y= frequenies, palette="bright")

axes.set_title(title)
axes.set(xlabel= "Горизонталь", ylabel= "Вертикаль")
axes.set_ylim(top=max(frequenies)* 1.30  )


for bar, frequenies in zip(axes.patches, frequenies):
    text_x = bar.get_x() + bar.get_width()/2.0
    text_y = bar.get_height()
    text = f"{frequenies:,}\n{frequenies/len(rolls):.4}"
    axes.text(text_x, text_y, text, fontsize= 11, ha= "center", va = "bottom")
    
plt.show()