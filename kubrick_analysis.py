import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("kubrick_films.csv")

# Display the first few rows of the dataset
print(df.head())

# Find the highest rated Kubrick film
top_film = df.sort_values(by="IMDb", ascending=False).iloc[0]
print("Highest rated Kubrick film:")
print(top_film)

# Plot IMDb ratings over time
plt.figure(figsize=(10,5))
plt.plot(df["Year"], df["IMDb"], marker="o")

# Highlight "2001: A Space Odyssey"
film_2001 = df[df["Film"] == "2001: A Space Odyssey"]
plt.scatter(film_2001["Year"], film_2001["IMDb"], color="red", s=100)

plt.title("IMDb Ratings of Stanley Kubrick Films Over Time")
plt.xlabel("Year")
plt.ylabel("IMDb Rating")

plt.show()
