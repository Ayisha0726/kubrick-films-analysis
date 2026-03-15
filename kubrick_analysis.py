import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("kubrick_films.csv")

# Show first rows
print(df.head())

# Find highest rated film
top_film = df.sort_values(by="IMDb", ascending=False).iloc[0]
print("Highest rated Kubrick film:")
print(top_film)

# Plot IMDb rating over time
plt.figure(figsize=(10,5))
plt.plot(df["Year"], df["IMDb"], marker="o")

# Highlight 2001: A Space Odyssey
film_2001 = df[df["Film"] == "2001: A Space Odyssey"]
plt.scatter(film_2001["Year"], film_2001["IMDb"], color="red", s=100)

plt.title("IMDb Ratings of Stanley Kubrick Films Over Time")
plt.xlabel("Year")
plt.ylabel("IMDb Rating")

plt.show()

# Plot runtime over time
plt.figure(figsize=(10,5))
plt.plot(df["Year"], df["Runtime"], marker="o")

plt.title("Runtime of Kubrick Films Over Time")
plt.xlabel("Year")
plt.ylabel("Runtime (minutes)")

plt.show()

# Plot runtime vs rating
plt.figure(figsize=(8,6))
plt.scatter(df["Runtime"], df["IMDb"])

plt.title("Runtime vs IMDb Rating")
plt.xlabel("Runtime (minutes)")
plt.ylabel("IMDb Rating")

plt.show()
