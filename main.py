
import pandas as pd
import matplotlib.pyplot as plt

# DO EMERALD, BUDERIM, CASSIA, ARAGORN, ELIZABETH

mainData = pd.read_csv("EnvvecFlyingFoxSurvey.csv")

emeraldData = mainData.loc[mainData["LocationName"] == "Emerald"]
emeraldData = (emeraldData.sort_values(by='ObservationDate')).dropna()

black = emeraldData[["Black", "ObservationDate"]]
blackNumeric = emeraldData["Black"]

strippedDate = []

for line in black["ObservationDate"]:
    strippedDate.append(line[:9])


observations = strippedDate
population = black["Black"]

plt.plot(observations, population)
plt.xlabel("Observation Dates")
plt.ylabel("Population of black flying foxes")
plt.title("Population of Black Flying Foxes from 2015-2023")

plt.xticks(rotation=25, ha='right')
plt.gca().xaxis.set_major_locator(plt.MaxNLocator(10))

plt.show()
