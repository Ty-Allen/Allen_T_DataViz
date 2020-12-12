import matplotlib.pyplot as plt 

#generate a pie chart with our Olympic data

values = [315, 203, 107]
colors = ["gold", "silver", "brown"]
labels = ["Gold: 167", "Silver: 319", "Bronze: 167"]
explode = (0, 0.05, 0)

plt.title("United States of America Medal Breakdown", pad="15")

plt.pie(values, labels=labels, colors=colors, explode=explode)

plt.show()
