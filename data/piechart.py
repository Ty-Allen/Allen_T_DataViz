import matplotlib.pyplot as plt 

#generate a pie chart with our Olympic data

values = [386, 239]
colors = ["green", "gold"]
labels = ["Men", "Women"]
explode = (0, 0.1)

plt.pie(values, labels=labels, colors=colors, explode=explode)

plt.show()