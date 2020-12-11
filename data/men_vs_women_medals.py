import matplotlib.pyplot as plt 
import numpy as np

medal_count_men = [192, 128, 66]
medal_count_women = [123, 75, 41]
medal_type = ["Gold", "Silver", "Bronze"]

xpos = np.arange(len(medal_type))

plt.ylabel("Medals Won")
plt.xlabel("Type of Medal")

plt.xticks(xpos, medal_type)
plt.bar(xpos-0.2, medal_count_men, width=0.4, label="Men", edgecolor="black", color=(255/255, 10/255, 10/255))
plt.bar(xpos+0.2, medal_count_women, width=0.4, label="Women", edgecolor="black", color=(255/255, 255/255, 255/255))

plt.legend()
plt.show()
