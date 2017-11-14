from geopy.geocoders import Nominatim
# from geopy.distance import vincenty
import pandas as pd
# from glob import glob
import os

os.chdir("C:/Development/Personal/geocoding")

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

df_from_coords = df.iloc[:, [2, 3]]
df_to_coords = df.iloc[:, [4, 5]]

from_coords = tuple([tuple(df_from_coords[col]) for col in df_from_coords])
print(from_coords)
# print(df_from_coords)
# print("*" * 80)
# print(df_to_coords)

# df["Vincenty_Distance"] = vincenty().miles
