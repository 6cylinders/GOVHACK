
import pandas as pd
import matplotlib.pyplot as plt

# DO EMERALD, BUDERIM, CASSIA, ARAGORN, ELIZABETH

mainData = pd.read_csv("EnvvecFlyingFoxSurvey.csv")


def foxGraph(location, foxType, mainData=mainData):

    try:
        regionData = mainData.loc[mainData["LocationName"] == location]
        regionData = (regionData.sort_values(by='ObservationDate')).dropna()

        foxes = regionData[[foxType, "ObservationDate"]]

        strippedDate = []

        for line in foxes["ObservationDate"]:
            strippedDate.append(line[:9])

        observations = strippedDate
        population = foxes[foxType]

        plt.plot(observations, population)
        plt.xlabel("Observation Dates")
        plt.ylabel(f"Population of {foxType} Flying Foxes")
        plt.title(f"Population of {foxType} Flying Foxes from {min(strippedDate)[:4]} - {max(strippedDate)[:4]} in {location}.")

        plt.xticks(rotation=25, ha='right')
        plt.gca().xaxis.set_major_locator(plt.MaxNLocator(10))

        plt.show()

    except KeyError:
        print("Please reenter parameters")


foxGraph("Emerald", "Black")
foxGraph("Buderim", "Black")
foxGraph("Cassia", "Black")
foxGraph("Aragorn", "Black")
foxGraph("Elizabeth", "Black")
