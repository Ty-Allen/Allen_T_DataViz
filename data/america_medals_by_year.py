import matplotlib.pyplot as plt

#draw a simple line chart showing population growth over the last 115 years

years = [1924, 1928, 1932, 1936, 1948, 1952, 1956, 1960, 1964, 1968, 1972, 1976, 1980, 1984, 1988, 1992, 1994, 1998, 2002, 2006, 2010, 2014]

medals = [13, 14, 45, 16, 16, 30, 26, 27, 8, 7, 25, 11, 30, 9, 7, 14, 21, 34, 84, 53, 98, 65]

#plot our chart with the data above, and also format the line color and width

plt.plot(years, medals, color=(10/255, 10/255, 255/255), linewidth=3.0)

#label on the left hand side
plt.ylabel("Medals Won")

#label on the bottom of the chart
plt.xlabel("Year")

#add a title to chart
plt.title("United States of America's Medal Count by Year", pad="15")

#run the show method (this lives inside the pyplot package)
#this will generate a graphic in a new window
plt.show()
