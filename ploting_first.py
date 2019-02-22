from matplotlib import pyplot as plt

# Line Plot
years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

plt.plot(years, gdp, color='blue', marker='x', linestyle='solid')

plt.title("GDP")
plt.ylabel("Billions of $")

plt.show()

# Bar plot

movies = ["Thor: Ragnorak", "Miss Sloane", "Infinity War"]
rating = [4, 3, 10]

arr = [i + 0.1 for i, _ in enumerate(movies)]

plt.bar(arr, rating)

plt.ylabel("Ratings")
plt.title("Good movies!")

plt.xticks([i + 0.5 for i, _ in enumerate(movies)], movies)

plt.show()