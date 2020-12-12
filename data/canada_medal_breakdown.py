import matplotlib.pyplot as plt 

#generate a pie chart with our Olympic data

values = [315, 203, 107]
colors = ["gold", "silver", "brown"]
labels = ["Gold: 315", "Silver: 203", "Bronze: 107"]
explode = (0.05, 0, 0)

plt.title("Canada Medal Breakdown", pad="15")

plt.pie(values, labels=labels, colors=colors, explode=explode)

plt.show()
