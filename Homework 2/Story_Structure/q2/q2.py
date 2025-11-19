import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme()

years = list(range(1990, 2024))

violent_crime = [
    700, 725, 710, 685, 660, 630, 600, 570, 540, 495,
    480, 470, 485, 475, 455, 445, 455, 440, 425, 405,
    395, 390, 400, 385, 390, 400, 385, 395, 370, 365,
    320, 370, 355, 340
]

gun_ownership = [
    0.62, 0.64, 0.66, 0.67, 0.69, 0.70, 0.71, 0.72, 0.73, 0.74,
    0.75, 0.76, 0.77, 0.78, 0.79, 0.78, 0.79, 0.80, 0.81, 0.82,
    0.84, 0.86, 0.88, 0.90, 0.95, 1.00, 0.98, 1.02, 1.07, 1.10,
    1.13, 1.15, 1.18, 1.20
]

# Plot: Violent crime (blue)
plt.figure(figsize=(10,4))
plt.plot(years, violent_crime, color="blue", linewidth=2)
plt.scatter(years, violent_crime, color="blue", s=20)   
plt.title("U.S. Violent Crime Rate")
plt.xlabel("Year")
plt.ylabel("Violent Crimes per 100,000 Citizens")
plt.ylim(0, 800)                    
plt.xticks(range(1990, 2024, 3))    
plt.grid(True, linewidth=0.4)
plt.tight_layout()
plt.show()

#Gun Ownership (red)
plt.figure(figsize=(10,4))
plt.plot(years, gun_ownership, color="red", linewidth=2)
plt.scatter(years, gun_ownership, color="red", s=20)
plt.title("U.S. Gun Ownership")
plt.xlabel("Year")
plt.ylabel("Gun Ownership per Capita")
plt.ylim(0, 1.3)                    
plt.xticks(range(1990, 2024, 3))
plt.grid(True, linewidth=0.4)
plt.tight_layout()
plt.show()
