from datetime import datetime, timedelta

from flight.models import *

from .models import Flight, Place, Week


def get_number_of_lines(file):
    with open(file) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


def createWeekDays():
    days = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]
    for i, day in enumerate(days):
        Week.objects.create(number=i, name=day)


def addPlaces():
    file = open("./Data/airports.csv", "r")
    print("Adding Airports...")
    total = get_number_of_lines("./Data/airports.csv")


def addDomesticFlights():
    file = open("./Data/domestic_flights.csv", "r")
    print("Adding Domestic Flights...")
    total = get_number_of_lines("./Data/domestic_flights.csv")


def addInternationalFlights():
    file = open("./Data/international_flights.csv", "r")
    print("Adding International Flights...")
    total = get_number_of_lines("./Data/international_flights.csv")
