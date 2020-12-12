import matplotlib.pyplot as plt 
import numpy as np

medals = [653, 625, 457, 440, 434, 433, 360, 285, 280, 263]
country = ["USA", "CAN", "NOR", "URS", "FIN", "SWE", "GER", "SUI", "AUT", "RUS"]

colors=["black", "red", "black", "black", "black", "black", "black", "black", "black", "black",]

ypos = np.arange(len(country))

plt.ylabel("Medals Won")
plt.xlabel("Country")

plt.xticks(ypos, country)
plt.bar(ypos, medals, color=colors)

plt.title("Total Medal Count Rankings", pad="15")

plt.show()
