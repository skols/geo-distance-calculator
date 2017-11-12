from geopy.geocoders import Nominatim
from geopy.distance import vincenty, great_circle
import pandas as pd
# from glob import glob
# import os


geolocator = Nominatim()
# os.chdir = ("C:/Development/Personal/geocoding/input/")

# path = os.getcwd()
# files = os.listdir(path)

in_file = "C:/Development/Personal/geocoding/input/zips.csv"

df = pd.read_csv(in_file, dtype=str)

df["FromZip_Latitude"] = df["FromZip"].apply(geolocator.geocode).apply(
    lambda x: x.latitude if x is not None else None)

df["FromZip_Longitude"] = df["FromZip"].apply(geolocator.geocode).apply(
    lambda x: x.longitude if x is not None else None)

df["ToZip_Latitude"] = df["ToZip"].apply(geolocator.geocode).apply(
    lambda x: x.latitude if x is not None else None)

df["ToZip_Longitude"] = df["ToZip"].apply(geolocator.geocode).apply(
    lambda x: x.longitude if x is not None else None)

df["Vincenty_Distance"] = vincenty(tuple(df["FromZip_Latitude"],
                                         df["FromZip_Longitude"]),
                                   tuple(df["ToZip_Latitude"],
                                         df["ToZip_Longitude"])).miles
