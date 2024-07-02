import numpy as np 
import matplotlib.pyplot as plt

x= np.arange(1, 100)
percentages = []
percent_dict = {}
for i in range(1, 100):
    percent = (1/i)*100
    percentages.append(percent)
    percent_dict[i] = percent
#plt.title("draw relationship")
#plt.xlabel("cards in deck")
#plt.ylabel("percentage to draw a specified card")
#plt.plot(x, percentages, color = "red", percentages, x, color = "blue")
#plt.show()

relationship = []
for key, value in percent_dict.items():
    relationship.append(key/value)

plt.title("relationship")
plt.xlabel("cards")
plt.ylabel("relationship")
plt.plot(x, relationship, color="blue")
plt.show()

print(relationship)
