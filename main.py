
import pandas as pd
import matplotlib.pyplot as plt


def foxGraph(location, foxType):
"""
Graphs flying fox population versus year of data entry
Takes desired location and species of flying fox as input

"""
    try:
        mainData = pd.read_csv("EnvvecFlyingFoxSurvey.csv")
        regionData = mainData.loc[mainData["LocationName"] == location]  # subsets data by location
        regionData = (regionData.sort_values(by='ObservationDate')).dropna()  # to clean data
        
        foxes = regionData[[foxType, "ObservationDate"]]

        strippedDate = []

        for line in foxes["ObservationDate"]:
            strippedDate.append(line[:9])  # sanitises dates from dataset for display purposes

        observations = strippedDate #x axis
        population = foxes[foxType] #y axis

        plt.plot(observations, population)
        plt.xlabel("Observation Dates")
        plt.ylabel(f"Population of {foxType.replace('_', ' ')} Flying Foxes")
        plt.title(f"Population of {foxType.replace('_', ' ')} Flying Foxes from {min(strippedDate)[:4]} - {max(strippedDate)[:4]} in {location}.")

        plt.xticks(rotation=25, ha='right') 
        plt.gca().xaxis.set_major_locator(plt.MaxNLocator(10))  # sets max amounts of ticks in graph to 10

        plt.show()

    except KeyError:
        print("Please reenter parameters")


def weatherGraph(tempData, weatherType, units):

    """
    Graphs desired weather data against year of data entry
    Takes dataset, type of weather, and measurement units as inputs
    
    """
    
    tempData = (pd.read_csv(tempData)).dropna() 
    tempData = tempData.loc[pd.to_numeric(tempData["Year"]) >= 2010]  # subsets data from 2010 onwards
    tempData["Date"] = pd.to_datetime(tempData[["Year", "Month", "Day"]])  # formats date for graph display

    dates = tempData["Date"]  # x axis
    weatherData = tempData[weatherType]

    plt.plot(dates, weatherData) 
    plt.xlabel("Observation Date")
    plt.ylabel(f"{weatherType} ({units})")
    plt.title(f"{weatherType} in the Sunshine Coast area from 2010-2023")
    plt.show()


fileInput = input("Type Data Type Here (Foxes | Weather): ")
typeInput = input("Enter Flying Fox / Weather Type Here: ")

# code below checks input above and runs appropriate function to graph the desired data.

try:
    if fileInput.lower() == "foxes":
        locationInput = input("What location do you want data for? ")
        foxGraph(locationInput, typeInput)

    elif fileInput.lower() == "weather":
        if typeInput == "Maximum Temperature":
            unit = "Celsius"
            dataset = "MaxTemp_SunshineCoast.csv"

        elif typeInput == "Rainfall Amount":
            unit = "mm"
            dataset = "Rainfall_SunshineCoast.csv"

        weatherGraph(dataset, typeInput, unit)

except FileNotFoundError:
    print("File not Located")
