import pandas as pd
import altair as alt
from vega_datasets import data
#datag = pd.DataFrame({
#    'a': list ("CCCDDDDEEEE"),
#    'b': [2,7,4,1,2,6,7,5,1,2,3]
#})
#chart = alt.Chart(datag).mark_bar().encode(
#    x='a',
#    y='average(b)',
#)
#
# 
# chart.save('chart.html')

source = pd.DataFrame([
    {
        "class": "Cross",
        "xp": 0.0,
        "xk": 16.0
    },
    {
        "class": "Cross",
        "xp": 0.0,
        "xk": 16.0
    },
    {
        "class": "Cross",
        "xp": 0.0,
        "xk": 16.0
    },
    {
        "class": "Cross",
        "xp": 0.0,
        "xk": 16.0
    },
    {
        "class": "Forest",
        "xp": 2.0,
        "xk": 10.0
    },
    {
        "class": "Cross",
        "xp": 0.0,
        "xk": 16.0
    },
    {
        "class": "Forest",
        "xp": 2.0,
        "xk": 10.0
    },
    {
        "class": "City",
        "xp": 4.0,
        "xk": 7.0
    },
    {
        "class": "Cross",
        "xp": 0.0,
        "xk": 16.0
    },
    {
        "class": "Forest",
        "xp": 2.0,
        "xk": 10.0
    },
    {
        "class": "Cross",
        "xp": 0.0,
        "xk": 16.0
    },
    {
        "class": "Forest",
        "xp": 2.0,
        "xk": 10.0
    },
    {
        "class": "Windows",
        "xp": 4.0,
        "xk": 9.0
    },
    {
        "class": "Cross",
        "xp": 0.0,
        "xk": 16.0
    },
    {
        "class": "Forest",
        "xp": 2.0,
        "xk": 10.0
    },
    {
        "class": "Person",
        "xp": 2.0,
        "xk": 14.0
    },
    {
        "class": "Windows",
        "xp": 4.0,
        "xk": 9.0
    },
    {
        "class": "Cross",
        "xp": 0.0,
        "xk": 16.0
    },
    {
        "class": "Footpath",
        "xp": 3.0,
        "xk": 18.0
    },
    {
        "class": "Forest",
        "xp": 2.0,
        "xk": 10.0
    },
    {
        "class": "Person",
        "xp": 2.0,
        "xk": 14.0
    },
    {
        "class": "Plants",
        "xp": 0.0,
        "xk": 15.0
    },
    {
        "class": "Trees",
        "xp": 0.0,
        "xk": 14.0
    },
    {
        "class": "Cross",
        "xp": 0.0,
        "xk": 16.0
    },
    {
        "class": "Cultural institution",
        "xp": 5.0,
        "xk": 61.0
    },
    {
        "class": "Footpath",
        "xp": 3.0,
        "xk": 18.0
    },
    {
        "class": "Person",
        "xp": 2.0,
        "xk": 14.0
    },
    {
        "class": "Plants",
        "xp": 0.0,
        "xk": 15.0
    },
    {
        "class": "Trees",
        "xp": 0.0,
        "xk": 14.0
    },
    {
        "class": "City",
        "xp": 9.0,
        "xk": 24.0
    },
    {
        "class": "Cross",
        "xp": 0.0,
        "xk": 16.0
    },
    {
        "class": "Cultural institution",
        "xp": 5.0,
        "xk": 61.0
    },
    {
        "class": "Footpath",
        "xp": 3.0,
        "xk": 18.0
    },
    {
        "class": "Person",
        "xp": 2.0,
        "xk": 14.0
    },
    {
        "class": "Plants",
        "xp": 0.0,
        "xk": 15.0
    },
    {
        "class": "Trees",
        "xp": 0.0,
        "xk": 14.0
    },
    {
        "class": "City",
        "xp": 9.0,
        "xk": 24.0
    },
    {
        "class": "Cross",
        "xp": 0.0,
        "xk": 16.0
    },
    {
        "class": "Cultural institution",
        "xp": 5.0,
        "xk": 61.0
    },
    {
        "class": "Footpath",
        "xp": 3.0,
        "xk": 18.0
    },
    {
        "class": "Person",
        "xp": 2.0,
        "xk": 14.0
    },
    {
        "class": "Plants",
        "xp": 0.0,
        "xk": 15.0
    },
    {
        "class": "Trees",
        "xp": 0.0,
        "xk": 14.0
    },
    {
        "class": "City",
        "xp": 9.0,
        "xk": 24.0
    },
    {
        "class": "Cross",
        "xp": 0.0,
        "xk": 16.0
    },
    {
        "class": "Cultural institution",
        "xp": 5.0,
        "xk": 61.0
    },
    {
        "class": "Footpath",
        "xp": 3.0,
        "xk": 18.0
    },
    {
        "class": "Grass",
        "xp": 0.0,
        "xk": 15.0
    },
    {
        "class": "Person",
        "xp": 2.0,
        "xk": 14.0
    },
    {
        "class": "Plants",
        "xp": 0.0,
        "xk": 15.0
    },
    {
        "class": "Trees",
        "xp": 0.0,
        "xk": 14.0
    },
    {
        "class": "City",
        "xp": 9.0,
        "xk": 24.0
    },
    {
        "class": "Cross",
        "xp": 0.0,
        "xk": 16.0
    },
    {
        "class": "Cultural institution",
        "xp": 5.0,
        "xk": 61.0
    },
    {
        "class": "Footpath",
        "xp": 3.0,
        "xk": 18.0
    },
    {
        "class": "Grass",
        "xp": 0.0,
        "xk": 15.0
    },
    {
        "class": "Plants",
        "xp": 0.0,
        "xk": 15.0
    },
    {
        "class": "City",
        "xp": 9.0,
        "xk": 24.0
    },
    {
        "class": "Cross",
        "xp": 0.0,
        "xk": 16.0
    },
    {
        "class": "Cultural institution",
        "xp": 5.0,
        "xk": 61.0
    },
    {
        "class": "Footpath",
        "xp": 3.0,
        "xk": 18.0
    },
    {
        "class": "Windows",
        "xp": 11.0,
        "xk": 33.0
    },
    {
        "class": "City",
        "xp": 9.0,
        "xk": 24.0
    },
    {
        "class": "Cultural institution",
        "xp": 5.0,
        "xk": 61.0
    },
    {
        "class": "Footpath",
        "xp": 3.0,
        "xk": 18.0
    },
    {
        "class": "Windows",
        "xp": 11.0,
        "xk": 33.0
    },
    {
        "class": "City",
        "xp": 9.0,
        "xk": 24.0
    },
    {
        "class": "Cultural institution",
        "xp": 5.0,
        "xk": 61.0
    },
    {
        "class": "Footpath",
        "xp": 3.0,
        "xk": 18.0
    },
    {
        "class": "Windows",
        "xp": 11.0,
        "xk": 33.0
    },
    {
        "class": "Building",
        "xp": 0.0,
        "xk": 26.0
    },
    {
        "class": "City",
        "xp": 9.0,
        "xk": 24.0
    },
    {
        "class": "Cultural institution",
        "xp": 5.0,
        "xk": 61.0
    },
    {
        "class": "Forest",
        "xp": 12.0,
        "xk": 33.0
    },
    {
        "class": "Person",
        "xp": 16.0,
        "xk": 23.0
    },
    {
        "class": "Windows",
        "xp": 11.0,
        "xk": 33.0
    },
    {
        "class": "Building",
        "xp": 0.0,
        "xk": 26.0
    },
    {
        "class": "City",
        "xp": 9.0,
        "xk": 24.0
    },
    {
        "class": "Cultural institution",
        "xp": 5.0,
        "xk": 61.0
    },
    {
        "class": "Forest",
        "xp": 12.0,
        "xk": 33.0
    },
    {
        "class": "Person",
        "xp": 16.0,
        "xk": 23.0
    },
    {
        "class": "Windows",
        "xp": 11.0,
        "xk": 33.0
    },
    {
        "class": "Building",
        "xp": 0.0,
        "xk": 26.0
    },
    {
        "class": "City",
        "xp": 9.0,
        "xk": 24.0
    },
    {
        "class": "Cultural institution",
        "xp": 5.0,
        "xk": 61.0
    },
    {
        "class": "Forest",
        "xp": 12.0,
        "xk": 33.0
    },
    {
        "class": "Graveyard",
        "xp": 18.0,
        "xk": 24.0
    },
    {
        "class": "Person",
        "xp": 16.0,
        "xk": 23.0
    },
    {
        "class": "Windows",
        "xp": 11.0,
        "xk": 33.0
    },
    {
        "class": "Building",
        "xp": 0.0,
        "xk": 26.0
    },
    {
        "class": "City",
        "xp": 9.0,
        "xk": 24.0
    },
    {
        "class": "Cultural institution",
        "xp": 5.0,
        "xk": 61.0
    },
    {
        "class": "Forest",
        "xp": 12.0,
        "xk": 33.0
    },
    {
        "class": "Graveyard",
        "xp": 18.0,
        "xk": 24.0
    },
    {
        "class": "Person",
        "xp": 16.0,
        "xk": 23.0
    },
    {
        "class": "Windows",
        "xp": 11.0,
        "xk": 33.0
    },
    {
        "class": "Building",
        "xp": 0.0,
        "xk": 26.0
    },
    {
        "class": "City",
        "xp": 9.0,
        "xk": 24.0
    },
    {
        "class": "Cultural institution",
        "xp": 5.0,
        "xk": 61.0
    },
    {
        "class": "Footpath",
        "xp": 20.0,
        "xk": 52.0
    },
    {
        "class": "Forest",
        "xp": 12.0,
        "xk": 33.0
    },
    {
        "class": "Graveyard",
        "xp": 18.0,
        "xk": 24.0
    },
    {
        "class": "Person",
        "xp": 16.0,
        "xk": 23.0
    },
    {
        "class": "Windows",
        "xp": 11.0,
        "xk": 33.0
    },
    {
        "class": "Building",
        "xp": 0.0,
        "xk": 26.0
    },
    {
        "class": "City",
        "xp": 9.0,
        "xk": 24.0
    },
    {
        "class": "Cultural institution",
        "xp": 5.0,
        "xk": 61.0
    },
    {
        "class": "Footpath",
        "xp": 20.0,
        "xk": 52.0
    },
    {
        "class": "Forest",
        "xp": 12.0,
        "xk": 33.0
    },
    {
        "class": "Graveyard",
        "xp": 18.0,
        "xk": 24.0
    },
    {
        "class": "Windows",
        "xp": 11.0,
        "xk": 33.0
    },
    {
        "class": "Building",
        "xp": 0.0,
        "xk": 26.0
    },
    {
        "class": "Cultural institution",
        "xp": 5.0,
        "xk": 61.0
    },
    {
        "class": "Footpath",
        "xp": 20.0,
        "xk": 52.0
    },
    {
        "class": "Forest",
        "xp": 12.0,
        "xk": 33.0
    },
    {
        "class": "Windows",
        "xp": 11.0,
        "xk": 33.0
    },
    {
        "class": "Building",
        "xp": 0.0,
        "xk": 26.0
    },
    {
        "class": "Cultural institution",
        "xp": 5.0,
        "xk": 61.0
    },
    {
        "class": "Footpath",
        "xp": 20.0,
        "xk": 52.0
    },
    {
        "class": "Forest",
        "xp": 12.0,
        "xk": 33.0
    },
    {
        "class": "Landscape",
        "xp": 17.0,
        "xk": 37.0
    },
    {
        "class": "Windows",
        "xp": 11.0,
        "xk": 33.0
    },
    {
        "class": "Cultural institution",
        "xp": 5.0,
        "xk": 61.0
    },
    {
        "class": "Footpath",
        "xp": 20.0,
        "xk": 52.0
    },
    {
        "class": "Forest",
        "xp": 12.0,
        "xk": 33.0
    },
    {
        "class": "Landscape",
        "xp": 17.0,
        "xk": 37.0
    },
    {
        "class": "Person",
        "xp": 25.0,
        "xk": 52.0
    },
    {
        "class": "Windows",
        "xp": 11.0,
        "xk": 33.0
    },
    {
        "class": "Church",
        "xp": 22.0,
        "xk": 48.0
    },
    {
        "class": "City",
        "xp": 26.0,
        "xk": 28.0
    },
    {
        "class": "Cultural institution",
        "xp": 5.0,
        "xk": 61.0
    },
    {
        "class": "Footpath",
        "xp": 20.0,
        "xk": 52.0
    },
    {
        "class": "Forest",
        "xp": 12.0,
        "xk": 33.0
    },
    {
        "class": "Graveyard",
        "xp": 26.0,
        "xk": 28.0
    },
    {
        "class": "Landscape",
        "xp": 17.0,
        "xk": 37.0
    },
    {
        "class": "Monument",
        "xp": 26.0,
        "xk": 35.0
    },
    {
        "class": "Person",
        "xp": 25.0,
        "xk": 52.0
    },
    {
        "class": "Windows",
        "xp": 11.0,
        "xk": 33.0
    },
    {
        "class": "Church",
        "xp": 22.0,
        "xk": 48.0
    },
    {
        "class": "Cultural institution",
        "xp": 5.0,
        "xk": 61.0
    },
    {
        "class": "Footpath",
        "xp": 20.0,
        "xk": 52.0
    },
    {
        "class": "Forest",
        "xp": 12.0,
        "xk": 33.0
    },
    {
        "class": "Landscape",
        "xp": 17.0,
        "xk": 37.0
    },
    {
        "class": "Monument",
        "xp": 26.0,
        "xk": 35.0
    },
    {
        "class": "Person",
        "xp": 25.0,
        "xk": 52.0
    },
    {
        "class": "Windows",
        "xp": 11.0,
        "xk": 33.0
    },
    {
        "class": "Church",
        "xp": 22.0,
        "xk": 48.0
    },
    {
        "class": "Cultural institution",
        "xp": 5.0,
        "xk": 61.0
    },
    {
        "class": "Footpath",
        "xp": 20.0,
        "xk": 52.0
    },
    {
        "class": "Forest",
        "xp": 12.0,
        "xk": 33.0
    },
    {
        "class": "Landscape",
        "xp": 17.0,
        "xk": 37.0
    },
    {
        "class": "Monument",
        "xp": 26.0,
        "xk": 35.0
    },
    {
        "class": "Person",
        "xp": 25.0,
        "xk": 52.0
    },
    {
        "class": "Windows",
        "xp": 11.0,
        "xk": 33.0
    },
    {
        "class": "Church",
        "xp": 22.0,
        "xk": 48.0
    },
    {
        "class": "Cross",
        "xp": 18.0,
        "xk": 41.0
    },
    {
        "class": "Cultural institution",
        "xp": 5.0,
        "xk": 61.0
    },
    {
        "class": "Footpath",
        "xp": 20.0,
        "xk": 52.0
    },
    {
        "class": "Forest",
        "xp": 12.0,
        "xk": 33.0
    },
    {
        "class": "Landscape",
        "xp": 17.0,
        "xk": 37.0
    },
    {
        "class": "Monument",
        "xp": 26.0,
        "xk": 35.0
    },
    {
        "class": "Person",
        "xp": 25.0,
        "xk": 52.0
    },
    {
        "class": "Windows",
        "xp": 11.0,
        "xk": 33.0
    },
    {
        "class": "Church",
        "xp": 22.0,
        "xk": 48.0
    },
    {
        "class": "City",
        "xp": 30.0,
        "xk": 33.0
    },
    {
        "class": "Cross",
        "xp": 18.0,
        "xk": 41.0
    },
    {
        "class": "Cultural institution",
        "xp": 5.0,
        "xk": 61.0
    },
    {
        "class": "Footpath",
        "xp": 20.0,
        "xk": 52.0
    },
    {
        "class": "Forest",
        "xp": 12.0,
        "xk": 33.0
    },
    {
        "class": "Landscape",
        "xp": 17.0,
        "xk": 37.0
    },
    {
        "class": "Monument",
        "xp": 26.0,
        "xk": 35.0
    },
    {
        "class": "Person",
        "xp": 25.0,
        "xk": 52.0
    },
    {
        "class": "Windows",
        "xp": 11.0,
        "xk": 33.0
    },
    {
        "class": "Church",
        "xp": 22.0,
        "xk": 48.0
    },
    {
        "class": "City",
        "xp": 30.0,
        "xk": 33.0
    },
    {
        "class": "Cross",
        "xp": 18.0,
        "xk": 41.0
    },
    {
        "class": "Cultural institution",
        "xp": 5.0,
        "xk": 61.0
    },
    {
        "class": "Footpath",
        "xp": 20.0,
        "xk": 52.0
    },
    {
        "class": "Forest",
        "xp": 12.0,
        "xk": 33.0
    },
    {
        "class": "Graveyard",
        "xp": 30.0,
        "xk": 47.0
    },
    {
        "class": "Landscape",
        "xp": 17.0,
        "xk": 37.0
    },
    {
        "class": "Monument",
        "xp": 26.0,
        "xk": 35.0
    },
    {
        "class": "Person",
        "xp": 25.0,
        "xk": 52.0
    },
    {
        "class": "Windows",
        "xp": 11.0,
        "xk": 33.0
    },
    {
        "class": "Church",
        "xp": 22.0,
        "xk": 48.0
    },
    {
        "class": "Cross",
        "xp": 18.0,
        "xk": 41.0
    },
    {
        "class": "Cultural institution",
        "xp": 5.0,
        "xk": 61.0
    },
    {
        "class": "Footpath",
        "xp": 20.0,
        "xk": 52.0
    },
    {
        "class": "Graveyard",
        "xp": 30.0,
        "xk": 47.0
    },
    {
        "class": "Landscape",
        "xp": 17.0,
        "xk": 37.0
    },
    {
        "class": "Monument",
        "xp": 26.0,
        "xk": 35.0
    },
    {
        "class": "Person",
        "xp": 25.0,
        "xk": 52.0
    },
    {
        "class": "Church",
        "xp": 22.0,
        "xk": 48.0
    },
    {
        "class": "Cross",
        "xp": 18.0,
        "xk": 41.0
    },
    {
        "class": "Cultural institution",
        "xp": 5.0,
        "xk": 61.0
    },
    {
        "class": "Footpath",
        "xp": 20.0,
        "xk": 52.0
    },
    {
        "class": "Graveyard",
        "xp": 30.0,
        "xk": 47.0
    },
    {
        "class": "Landscape",
        "xp": 17.0,
        "xk": 37.0
    },
    {
        "class": "Monument",
        "xp": 26.0,
        "xk": 35.0
    },
    {
        "class": "Person",
        "xp": 25.0,
        "xk": 52.0
    },
    {
        "class": "Church",
        "xp": 22.0,
        "xk": 48.0
    },
    {
        "class": "Cross",
        "xp": 18.0,
        "xk": 41.0
    },
    {
        "class": "Cultural institution",
        "xp": 5.0,
        "xk": 61.0
    },
    {
        "class": "Footpath",
        "xp": 20.0,
        "xk": 52.0
    },
    {
        "class": "Graveyard",
        "xp": 30.0,
        "xk": 47.0
    },
    {
        "class": "Landscape",
        "xp": 17.0,
        "xk": 37.0
    },
    {
        "class": "Person",
        "xp": 25.0,
        "xk": 52.0
    },
    {
        "class": "Plants",
        "xp": 17.0,
        "xk": 41.0
    },
    {
        "class": "Church",
        "xp": 22.0,
        "xk": 48.0
    },
    {
        "class": "City",
        "xp": 35.0,
        "xk": 38.0
    },
    {
        "class": "Cross",
        "xp": 18.0,
        "xk": 41.0
    },
    {
        "class": "Cultural institution",
        "xp": 5.0,
        "xk": 61.0
    },
    {
        "class": "Footpath",
        "xp": 20.0,
        "xk": 52.0
    },
    {
        "class": "Graveyard",
        "xp": 30.0,
        "xk": 47.0
    },
    {
        "class": "Landscape",
        "xp": 17.0,
        "xk": 37.0
    },
    {
        "class": "Park",
        "xp": 35.0,
        "xk": 122.0
    },
    {
        "class": "Person",
        "xp": 25.0,
        "xk": 52.0
    },
    {
        "class": "Plants",
        "xp": 17.0,
        "xk": 41.0
    },
    {
        "class": "Church",
        "xp": 22.0,
        "xk": 48.0
    },
    {
        "class": "City",
        "xp": 35.0,
        "xk": 38.0
    },
    {
        "class": "Cross",
        "xp": 18.0,
        "xk": 41.0
    },
    {
        "class": "Cultural institution",
        "xp": 5.0,
        "xk": 61.0
    },
    {
        "class": "Footpath",
        "xp": 20.0,
        "xk": 52.0
    },
    {
        "class": "Graveyard",
        "xp": 30.0,
        "xk": 47.0
    },
    {
        "class": "Park",
        "xp": 35.0,
        "xk": 122.0
    },
    {
        "class": "Person",
        "xp": 25.0,
        "xk": 52.0
    },
    {
        "class": "Plants",
        "xp": 17.0,
        "xk": 41.0
    },
    {
        "class": "Church",
        "xp": 22.0,
        "xk": 48.0
    },
    {
        "class": "Cross",
        "xp": 18.0,
        "xk": 41.0
    },
    {
        "class": "Cultural institution",
        "xp": 5.0,
        "xk": 61.0
    },
    {
        "class": "Footpath",
        "xp": 20.0,
        "xk": 52.0
    },
    {
        "class": "Graveyard",
        "xp": 30.0,
        "xk": 47.0
    },
    {
        "class": "Park",
        "xp": 35.0,
        "xk": 122.0
    },
    {
        "class": "Person",
        "xp": 25.0,
        "xk": 52.0
    },
    {
        "class": "Plants",
        "xp": 17.0,
        "xk": 41.0
    },
    {
        "class": "Church",
        "xp": 22.0,
        "xk": 48.0
    },
    {
        "class": "Cross",
        "xp": 18.0,
        "xk": 41.0
    },
    {
        "class": "Cultural institution",
        "xp": 5.0,
        "xk": 61.0
    },
    {
        "class": "Footpath",
        "xp": 20.0,
        "xk": 52.0
    },
    {
        "class": "Graveyard",
        "xp": 30.0,
        "xk": 47.0
    },
    {
        "class": "Monument",
        "xp": 37.0,
        "xk": 56.0
    },
    {
        "class": "Park",
        "xp": 35.0,
        "xk": 122.0
    },
    {
        "class": "Person",
        "xp": 25.0,
        "xk": 52.0
    },
    {
        "class": "Plants",
        "xp": 17.0,
        "xk": 41.0
    },
    {
        "class": "Windows",
        "xp": 35.0,
        "xk": 50.0
    },
    {
        "class": "Church",
        "xp": 22.0,
        "xk": 48.0
    },
    {
        "class": "Cross",
        "xp": 18.0,
        "xk": 41.0
    },
    {
        "class": "Cultural institution",
        "xp": 5.0,
        "xk": 61.0
    },
    {
        "class": "Footpath",
        "xp": 20.0,
        "xk": 52.0
    },
    {
        "class": "Graveyard",
        "xp": 30.0,
        "xk": 47.0
    },
    {
        "class": "Monument",
        "xp": 37.0,
        "xk": 56.0
    },
    {
        "class": "Park",
        "xp": 35.0,
        "xk": 122.0
    },
    {
        "class": "Person",
        "xp": 25.0,
        "xk": 52.0
    },
    {
        "class": "Plants",
        "xp": 17.0,
        "xk": 41.0
    },
    {
        "class": "Windows",
        "xp": 35.0,
        "xk": 50.0
    },
    {
        "class": "Building",
        "xp": 28.0,
        "xk": 47.0
    },
    {
        "class": "Church",
        "xp": 22.0,
        "xk": 48.0
    },
    {
        "class": "Cultural institution",
        "xp": 5.0,
        "xk": 61.0
    },
    {
        "class": "Footpath",
        "xp": 20.0,
        "xk": 52.0
    },
    {
        "class": "Graveyard",
        "xp": 30.0,
        "xk": 47.0
    },
    {
        "class": "Monument",
        "xp": 37.0,
        "xk": 56.0
    },
    {
        "class": "Park",
        "xp": 35.0,
        "xk": 122.0
    },
    {
        "class": "Person",
        "xp": 25.0,
        "xk": 52.0
    },
    {
        "class": "Windows",
        "xp": 35.0,
        "xk": 50.0
    },
    {
        "class": "Building",
        "xp": 28.0,
        "xk": 47.0
    },
    {
        "class": "Church",
        "xp": 22.0,
        "xk": 48.0
    },
    {
        "class": "Cultural institution",
        "xp": 5.0,
        "xk": 61.0
    },
    {
        "class": "Footpath",
        "xp": 20.0,
        "xk": 52.0
    },
    {
        "class": "Graveyard",
        "xp": 30.0,
        "xk": 47.0
    },
    {
        "class": "Landscape",
        "xp": 39.0,
        "xk": 46.0
    },
    {
        "class": "Mine",
        "xp": 39.0,
        "xk": 122.0
    },
    {
        "class": "Monument",
        "xp": 37.0,
        "xk": 56.0
    },
    {
        "class": "Park",
        "xp": 35.0,
        "xk": 122.0
    },
    {
        "class": "Person",
        "xp": 25.0,
        "xk": 52.0
    },
    {
        "class": "Windows",
        "xp": 35.0,
        "xk": 50.0
    },
    {
        "class": "Building",
        "xp": 28.0,
        "xk": 47.0
    },
    {
        "class": "Church",
        "xp": 22.0,
        "xk": 48.0
    },
    {
        "class": "City",
        "xp": 40.0,
        "xk": 47.0
    },
    {
        "class": "Cultural institution",
        "xp": 5.0,
        "xk": 61.0
    },
    {
        "class": "Footpath",
        "xp": 20.0,
        "xk": 52.0
    },
    {
        "class": "Forest",
        "xp": 35.0,
        "xk": 73.0
    },
    {
        "class": "Graveyard",
        "xp": 30.0,
        "xk": 47.0
    },
    {
        "class": "Landscape",
        "xp": 39.0,
        "xk": 46.0
    },
    {
        "class": "Mine",
        "xp": 39.0,
        "xk": 122.0
    },
    {
        "class": "Monument",
        "xp": 37.0,
        "xk": 56.0
    },
    {
        "class": "Park",
        "xp": 35.0,
        "xk": 122.0
    },
    {
        "class": "Person",
        "xp": 25.0,
        "xk": 52.0
    },
    {
        "class": "Windows",
        "xp": 35.0,
        "xk": 50.0
    },
    {
        "class": "Building",
        "xp": 28.0,
        "xk": 47.0
    },
    {
        "class": "Church",
        "xp": 22.0,
        "xk": 48.0
    },
    {
        "class": "City",
        "xp": 40.0,
        "xk": 47.0
    },
    {
        "class": "Cultural institution",
        "xp": 5.0,
        "xk": 61.0
    },
    {
        "class": "Footpath",
        "xp": 20.0,
        "xk": 52.0
    },
    {
        "class": "Forest",
        "xp": 35.0,
        "xk": 73.0
    },
    {
        "class": "Graveyard",
        "xp": 30.0,
        "xk": 47.0
    },
    {
        "class": "Landscape",
        "xp": 39.0,
        "xk": 46.0
    },
    {
        "class": "Mine",
        "xp": 39.0,
        "xk": 122.0
    },
    {
        "class": "Monument",
        "xp": 37.0,
        "xk": 56.0
    },
    {
        "class": "Park",
        "xp": 35.0,
        "xk": 122.0
    },
    {
        "class": "Person",
        "xp": 25.0,
        "xk": 52.0
    },
    {
        "class": "Windows",
        "xp": 35.0,
        "xk": 50.0
    },
    {
        "class": "Building",
        "xp": 28.0,
        "xk": 47.0
    },
    {
        "class": "Church",
        "xp": 22.0,
        "xk": 48.0
    },
    {
        "class": "City",
        "xp": 40.0,
        "xk": 47.0
    },
    {
        "class": "Cultural institution",
        "xp": 5.0,
        "xk": 61.0
    },
    {
        "class": "Footpath",
        "xp": 20.0,
        "xk": 52.0
    },
    {
        "class": "Forest",
        "xp": 35.0,
        "xk": 73.0
    },
    {
        "class": "Graveyard",
        "xp": 30.0,
        "xk": 47.0
    },
    {
        "class": "Landscape",
        "xp": 39.0,
        "xk": 46.0
    },
    {
        "class": "Mine",
        "xp": 39.0,
        "xk": 122.0
    },
    {
        "class": "Monument",
        "xp": 37.0,
        "xk": 56.0
    },
    {
        "class": "Park",
        "xp": 35.0,
        "xk": 122.0
    },
    {
        "class": "Person",
        "xp": 25.0,
        "xk": 52.0
    },
    {
        "class": "Windows",
        "xp": 35.0,
        "xk": 50.0
    },
    {
        "class": "Building",
        "xp": 28.0,
        "xk": 47.0
    },
    {
        "class": "Church",
        "xp": 22.0,
        "xk": 48.0
    },
    {
        "class": "City",
        "xp": 40.0,
        "xk": 47.0
    },
    {
        "class": "Cultural institution",
        "xp": 5.0,
        "xk": 61.0
    },
    {
        "class": "Footpath",
        "xp": 20.0,
        "xk": 52.0
    },
    {
        "class": "Forest",
        "xp": 35.0,
        "xk": 73.0
    },
    {
        "class": "Graveyard",
        "xp": 30.0,
        "xk": 47.0
    },
    {
        "class": "Mine",
        "xp": 39.0,
        "xk": 122.0
    },
    {
        "class": "Monument",
        "xp": 37.0,
        "xk": 56.0
    },
    {
        "class": "Park",
        "xp": 35.0,
        "xk": 122.0
    },
    {
        "class": "Person",
        "xp": 25.0,
        "xk": 52.0
    },
    {
        "class": "Windows",
        "xp": 35.0,
        "xk": 50.0
    },
    {
        "class": "Church",
        "xp": 22.0,
        "xk": 48.0
    },
    {
        "class": "Cultural institution",
        "xp": 5.0,
        "xk": 61.0
    },
    {
        "class": "Footpath",
        "xp": 20.0,
        "xk": 52.0
    },
    {
        "class": "Forest",
        "xp": 35.0,
        "xk": 73.0
    },
    {
        "class": "Mine",
        "xp": 39.0,
        "xk": 122.0
    },
    {
        "class": "Monument",
        "xp": 37.0,
        "xk": 56.0
    },
    {
        "class": "Park",
        "xp": 35.0,
        "xk": 122.0
    },
    {
        "class": "Person",
        "xp": 25.0,
        "xk": 52.0
    },
    {
        "class": "Rocks",
        "xp": 43.0,
        "xk": 73.0
    },
    {
        "class": "Windows",
        "xp": 35.0,
        "xk": 50.0
    },
    {
        "class": "Cultural institution",
        "xp": 5.0,
        "xk": 61.0
    },
    {
        "class": "Footpath",
        "xp": 20.0,
        "xk": 52.0
    },
    {
        "class": "Forest",
        "xp": 35.0,
        "xk": 73.0
    },
    {
        "class": "Mine",
        "xp": 39.0,
        "xk": 122.0
    },
    {
        "class": "Monument",
        "xp": 37.0,
        "xk": 56.0
    },
    {
        "class": "Park",
        "xp": 35.0,
        "xk": 122.0
    },
    {
        "class": "Person",
        "xp": 25.0,
        "xk": 52.0
    },
    {
        "class": "Rocks",
        "xp": 43.0,
        "xk": 73.0
    },
    {
        "class": "Windows",
        "xp": 35.0,
        "xk": 50.0
    },
    {
        "class": "Cultural institution",
        "xp": 5.0,
        "xk": 61.0
    },
    {
        "class": "Footpath",
        "xp": 20.0,
        "xk": 52.0
    },
    {
        "class": "Forest",
        "xp": 35.0,
        "xk": 73.0
    },
    {
        "class": "Mine",
        "xp": 39.0,
        "xk": 122.0
    },
    {
        "class": "Monument",
        "xp": 37.0,
        "xk": 56.0
    },
    {
        "class": "Park",
        "xp": 35.0,
        "xk": 122.0
    },
    {
        "class": "Person",
        "xp": 25.0,
        "xk": 52.0
    },
    {
        "class": "Rocks",
        "xp": 43.0,
        "xk": 73.0
    },
    {
        "class": "Windows",
        "xp": 35.0,
        "xk": 50.0
    },
    {
        "class": "Cultural institution",
        "xp": 5.0,
        "xk": 61.0
    },
    {
        "class": "Footpath",
        "xp": 20.0,
        "xk": 52.0
    },
    {
        "class": "Forest",
        "xp": 35.0,
        "xk": 73.0
    },
    {
        "class": "Graveyard",
        "xp": 49.0,
        "xk": 96.0
    },
    {
        "class": "Mine",
        "xp": 39.0,
        "xk": 122.0
    },
    {
        "class": "Monument",
        "xp": 37.0,
        "xk": 56.0
    },
    {
        "class": "Park",
        "xp": 35.0,
        "xk": 122.0
    },
    {
        "class": "Person",
        "xp": 25.0,
        "xk": 52.0
    },
    {
        "class": "Rocks",
        "xp": 43.0,
        "xk": 73.0
    },
    {
        "class": "Church",
        "xp": 50.0,
        "xk": 52.0
    },
    {
        "class": "Cultural institution",
        "xp": 5.0,
        "xk": 61.0
    },
    {
        "class": "Footpath",
        "xp": 20.0,
        "xk": 52.0
    },
    {
        "class": "Forest",
        "xp": 35.0,
        "xk": 73.0
    },
    {
        "class": "Graveyard",
        "xp": 49.0,
        "xk": 96.0
    },
    {
        "class": "Mine",
        "xp": 39.0,
        "xk": 122.0
    },
    {
        "class": "Monument",
        "xp": 37.0,
        "xk": 56.0
    },
    {
        "class": "Park",
        "xp": 35.0,
        "xk": 122.0
    },
    {
        "class": "Person",
        "xp": 25.0,
        "xk": 52.0
    },
    {
        "class": "Rocks",
        "xp": 43.0,
        "xk": 73.0
    },
    {
        "class": "Cultural institution",
        "xp": 5.0,
        "xk": 61.0
    },
    {
        "class": "Forest",
        "xp": 35.0,
        "xk": 73.0
    },
    {
        "class": "Graveyard",
        "xp": 49.0,
        "xk": 96.0
    },
    {
        "class": "Mine",
        "xp": 39.0,
        "xk": 122.0
    },
    {
        "class": "Monument",
        "xp": 37.0,
        "xk": 56.0
    },
    {
        "class": "Park",
        "xp": 35.0,
        "xk": 122.0
    },
    {
        "class": "Rocks",
        "xp": 43.0,
        "xk": 73.0
    },
    {
        "class": "Cultural institution",
        "xp": 5.0,
        "xk": 61.0
    },
    {
        "class": "Forest",
        "xp": 35.0,
        "xk": 73.0
    },
    {
        "class": "Graveyard",
        "xp": 49.0,
        "xk": 96.0
    },
    {
        "class": "Mine",
        "xp": 39.0,
        "xk": 122.0
    },
    {
        "class": "Monument",
        "xp": 37.0,
        "xk": 56.0
    },
    {
        "class": "Park",
        "xp": 35.0,
        "xk": 122.0
    },
    {
        "class": "Rocks",
        "xp": 43.0,
        "xk": 73.0
    },
    {
        "class": "Windows",
        "xp": 52.0,
        "xk": 58.0
    },
    {
        "class": "Cultural institution",
        "xp": 5.0,
        "xk": 61.0
    },
    {
        "class": "Forest",
        "xp": 35.0,
        "xk": 73.0
    },
    {
        "class": "Graveyard",
        "xp": 49.0,
        "xk": 96.0
    },
    {
        "class": "Landscape",
        "xp": 48.0,
        "xk": 96.0
    },
    {
        "class": "Mine",
        "xp": 39.0,
        "xk": 122.0
    },
    {
        "class": "Monument",
        "xp": 37.0,
        "xk": 56.0
    },
    {
        "class": "Park",
        "xp": 35.0,
        "xk": 122.0
    },
    {
        "class": "Rocks",
        "xp": 43.0,
        "xk": 73.0
    },
    {
        "class": "Windows",
        "xp": 52.0,
        "xk": 58.0
    },
    {
        "class": "Cultural institution",
        "xp": 5.0,
        "xk": 61.0
    },
    {
        "class": "Footpath",
        "xp": 54.0,
        "xk": 76.0
    },
    {
        "class": "Forest",
        "xp": 35.0,
        "xk": 73.0
    },
    {
        "class": "Grass",
        "xp": 17.0,
        "xk": 60.0
    },
    {
        "class": "Graveyard",
        "xp": 49.0,
        "xk": 96.0
    },
    {
        "class": "Landscape",
        "xp": 48.0,
        "xk": 96.0
    },
    {
        "class": "Mine",
        "xp": 39.0,
        "xk": 122.0
    },
    {
        "class": "Monument",
        "xp": 37.0,
        "xk": 56.0
    },
    {
        "class": "Park",
        "xp": 35.0,
        "xk": 122.0
    },
    {
        "class": "Rocks",
        "xp": 43.0,
        "xk": 73.0
    },
    {
        "class": "Windows",
        "xp": 52.0,
        "xk": 58.0
    },
    {
        "class": "Cultural institution",
        "xp": 5.0,
        "xk": 61.0
    },
    {
        "class": "Footpath",
        "xp": 54.0,
        "xk": 76.0
    },
    {
        "class": "Forest",
        "xp": 35.0,
        "xk": 73.0
    },
    {
        "class": "Grass",
        "xp": 17.0,
        "xk": 60.0
    },
    {
        "class": "Graveyard",
        "xp": 49.0,
        "xk": 96.0
    },
    {
        "class": "Landscape",
        "xp": 48.0,
        "xk": 96.0
    },
    {
        "class": "Mine",
        "xp": 39.0,
        "xk": 122.0
    },
    {
        "class": "Park",
        "xp": 35.0,
        "xk": 122.0
    },
    {
        "class": "Rocks",
        "xp": 43.0,
        "xk": 73.0
    },
    {
        "class": "Windows",
        "xp": 52.0,
        "xk": 58.0
    },
    {
        "class": "Cultural institution",
        "xp": 5.0,
        "xk": 61.0
    },
    {
        "class": "Footpath",
        "xp": 54.0,
        "xk": 76.0
    },
    {
        "class": "Forest",
        "xp": 35.0,
        "xk": 73.0
    },
    {
        "class": "Grass",
        "xp": 17.0,
        "xk": 60.0
    },
    {
        "class": "Graveyard",
        "xp": 49.0,
        "xk": 96.0
    },
    {
        "class": "Landscape",
        "xp": 48.0,
        "xk": 96.0
    },
    {
        "class": "Mine",
        "xp": 39.0,
        "xk": 122.0
    },
    {
        "class": "Park",
        "xp": 35.0,
        "xk": 122.0
    },
    {
        "class": "Rocks",
        "xp": 43.0,
        "xk": 73.0
    },
    {
        "class": "Windows",
        "xp": 52.0,
        "xk": 58.0
    },
    {
        "class": "Cultural institution",
        "xp": 5.0,
        "xk": 61.0
    },
    {
        "class": "Footpath",
        "xp": 54.0,
        "xk": 76.0
    },
    {
        "class": "Forest",
        "xp": 35.0,
        "xk": 73.0
    },
    {
        "class": "Grass",
        "xp": 17.0,
        "xk": 60.0
    },
    {
        "class": "Graveyard",
        "xp": 49.0,
        "xk": 96.0
    },
    {
        "class": "Landscape",
        "xp": 48.0,
        "xk": 96.0
    },
    {
        "class": "Mine",
        "xp": 39.0,
        "xk": 122.0
    },
    {
        "class": "Park",
        "xp": 35.0,
        "xk": 122.0
    },
    {
        "class": "Rocks",
        "xp": 43.0,
        "xk": 73.0
    },
    {
        "class": "Cultural institution",
        "xp": 5.0,
        "xk": 61.0
    },
    {
        "class": "Footpath",
        "xp": 54.0,
        "xk": 76.0
    },
    {
        "class": "Forest",
        "xp": 35.0,
        "xk": 73.0
    },
    {
        "class": "Grass",
        "xp": 17.0,
        "xk": 60.0
    },
    {
        "class": "Graveyard",
        "xp": 49.0,
        "xk": 96.0
    },
    {
        "class": "Landscape",
        "xp": 48.0,
        "xk": 96.0
    },
    {
        "class": "Mine",
        "xp": 39.0,
        "xk": 122.0
    },
    {
        "class": "Park",
        "xp": 35.0,
        "xk": 122.0
    },
    {
        "class": "Person",
        "xp": 54.0,
        "xk": 61.0
    },
    {
        "class": "Rocks",
        "xp": 43.0,
        "xk": 73.0
    },
    {
        "class": "Cultural institution",
        "xp": 5.0,
        "xk": 61.0
    },
    {
        "class": "Footpath",
        "xp": 54.0,
        "xk": 76.0
    },
    {
        "class": "Forest",
        "xp": 35.0,
        "xk": 73.0
    },
    {
        "class": "Graveyard",
        "xp": 49.0,
        "xk": 96.0
    },
    {
        "class": "Landscape",
        "xp": 48.0,
        "xk": 96.0
    },
    {
        "class": "Mine",
        "xp": 39.0,
        "xk": 122.0
    },
    {
        "class": "Motor vehicle",
        "xp": 59.0,
        "xk": 120.0
    },
    {
        "class": "Park",
        "xp": 35.0,
        "xk": 122.0
    },
    {
        "class": "Person",
        "xp": 54.0,
        "xk": 61.0
    },
    {
        "class": "Rocks",
        "xp": 43.0,
        "xk": 73.0
    },
    {
        "class": "Footpath",
        "xp": 54.0,
        "xk": 76.0
    },
    {
        "class": "Forest",
        "xp": 35.0,
        "xk": 73.0
    },
    {
        "class": "Graveyard",
        "xp": 49.0,
        "xk": 96.0
    },
    {
        "class": "Landscape",
        "xp": 48.0,
        "xk": 96.0
    },
    {
        "class": "Mine",
        "xp": 39.0,
        "xk": 122.0
    },
    {
        "class": "Motor vehicle",
        "xp": 59.0,
        "xk": 120.0
    },
    {
        "class": "Park",
        "xp": 35.0,
        "xk": 122.0
    },
    {
        "class": "Rocks",
        "xp": 43.0,
        "xk": 73.0
    },
    {
        "class": "Windows",
        "xp": 60.0,
        "xk": 80.0
    },
    {
        "class": "City",
        "xp": 49.0,
        "xk": 68.0
    },
    {
        "class": "Cross",
        "xp": 43.0,
        "xk": 76.0
    },
    {
        "class": "Footpath",
        "xp": 54.0,
        "xk": 76.0
    },
    {
        "class": "Forest",
        "xp": 35.0,
        "xk": 73.0
    },
    {
        "class": "Graveyard",
        "xp": 49.0,
        "xk": 96.0
    },
    {
        "class": "Landscape",
        "xp": 48.0,
        "xk": 96.0
    },
    {
        "class": "Mine",
        "xp": 39.0,
        "xk": 122.0
    },
    {
        "class": "Monument",
        "xp": 58.0,
        "xk": 122.0
    },
    {
        "class": "Motor vehicle",
        "xp": 59.0,
        "xk": 120.0
    },
    {
        "class": "Park",
        "xp": 35.0,
        "xk": 122.0
    },
    {
        "class": "Road",
        "xp": 59.0,
        "xk": 109.0
    },
    {
        "class": "Rocks",
        "xp": 43.0,
        "xk": 73.0
    },
    {
        "class": "Windows",
        "xp": 60.0,
        "xk": 80.0
    },
    {
        "class": "Church",
        "xp": 54.0,
        "xk": 76.0
    },
    {
        "class": "City",
        "xp": 49.0,
        "xk": 68.0
    },
    {
        "class": "Cross",
        "xp": 43.0,
        "xk": 76.0
    },
    {
        "class": "Footpath",
        "xp": 54.0,
        "xk": 76.0
    },
    {
        "class": "Forest",
        "xp": 35.0,
        "xk": 73.0
    },
    {
        "class": "Graveyard",
        "xp": 49.0,
        "xk": 96.0
    },
    {
        "class": "Landscape",
        "xp": 48.0,
        "xk": 96.0
    },
    {
        "class": "Mine",
        "xp": 39.0,
        "xk": 122.0
    },
    {
        "class": "Monument",
        "xp": 58.0,
        "xk": 122.0
    },
    {
        "class": "Motor vehicle",
        "xp": 59.0,
        "xk": 120.0
    },
    {
        "class": "Park",
        "xp": 35.0,
        "xk": 122.0
    },
    {
        "class": "Plants",
        "xp": 43.0,
        "xk": 72.0
    },
    {
        "class": "Road",
        "xp": 59.0,
        "xk": 109.0
    },
    {
        "class": "Rocks",
        "xp": 43.0,
        "xk": 73.0
    },
    {
        "class": "Trees",
        "xp": 16.0,
        "xk": 72.0
    },
    {
        "class": "Windows",
        "xp": 60.0,
        "xk": 80.0
    },
    {
        "class": "Church",
        "xp": 54.0,
        "xk": 76.0
    },
    {
        "class": "City",
        "xp": 49.0,
        "xk": 68.0
    },
    {
        "class": "Cross",
        "xp": 43.0,
        "xk": 76.0
    },
    {
        "class": "Cultural institution",
        "xp": 63.0,
        "xk": 88.0
    },
    {
        "class": "Footpath",
        "xp": 54.0,
        "xk": 76.0
    },
    {
        "class": "Forest",
        "xp": 35.0,
        "xk": 73.0
    },
    {
        "class": "Graveyard",
        "xp": 49.0,
        "xk": 96.0
    },
    {
        "class": "Landscape",
        "xp": 48.0,
        "xk": 96.0
    },
    {
        "class": "Mine",
        "xp": 39.0,
        "xk": 122.0
    },
    {
        "class": "Monument",
        "xp": 58.0,
        "xk": 122.0
    },
    {
        "class": "Motor vehicle",
        "xp": 59.0,
        "xk": 120.0
    },
    {
        "class": "Park",
        "xp": 35.0,
        "xk": 122.0
    },
    {
        "class": "Plants",
        "xp": 43.0,
        "xk": 72.0
    },
    {
        "class": "Road",
        "xp": 59.0,
        "xk": 109.0
    },
    {
        "class": "Rocks",
        "xp": 43.0,
        "xk": 73.0
    },
    {
        "class": "Trees",
        "xp": 16.0,
        "xk": 72.0
    },
    {
        "class": "Windows",
        "xp": 60.0,
        "xk": 80.0
    },
    {
        "class": "Church",
        "xp": 54.0,
        "xk": 76.0
    },
    {
        "class": "City",
        "xp": 49.0,
        "xk": 68.0
    },
    {
        "class": "Cross",
        "xp": 43.0,
        "xk": 76.0
    },
    {
        "class": "Cultural institution",
        "xp": 63.0,
        "xk": 88.0
    },
    {
        "class": "Footpath",
        "xp": 54.0,
        "xk": 76.0
    },
    {
        "class": "Forest",
        "xp": 35.0,
        "xk": 73.0
    },
    {
        "class": "Grass",
        "xp": 62.0,
        "xk": 71.0
    },
    {
        "class": "Graveyard",
        "xp": 49.0,
        "xk": 96.0
    },
    {
        "class": "Landscape",
        "xp": 48.0,
        "xk": 96.0
    },
    {
        "class": "Mine",
        "xp": 39.0,
        "xk": 122.0
    },
    {
        "class": "Monument",
        "xp": 58.0,
        "xk": 122.0
    },
    {
        "class": "Motor vehicle",
        "xp": 59.0,
        "xk": 120.0
    },
    {
        "class": "Museum",
        "xp": 63.0,
        "xk": 122.0
    },
    {
        "class": "Park",
        "xp": 35.0,
        "xk": 122.0
    },
    {
        "class": "Plants",
        "xp": 43.0,
        "xk": 72.0
    },
    {
        "class": "Road",
        "xp": 59.0,
        "xk": 109.0
    },
    {
        "class": "Rocks",
        "xp": 43.0,
        "xk": 73.0
    },
    {
        "class": "Trees",
        "xp": 16.0,
        "xk": 72.0
    },
    {
        "class": "Windows",
        "xp": 60.0,
        "xk": 80.0
    },
    {
        "class": "Church",
        "xp": 54.0,
        "xk": 76.0
    },
    {
        "class": "City",
        "xp": 49.0,
        "xk": 68.0
    },
    {
        "class": "Cross",
        "xp": 43.0,
        "xk": 76.0
    },
    {
        "class": "Cultural institution",
        "xp": 63.0,
        "xk": 88.0
    },
    {
        "class": "Footpath",
        "xp": 54.0,
        "xk": 76.0
    },
    {
        "class": "Forest",
        "xp": 35.0,
        "xk": 73.0
    },
    {
        "class": "Grass",
        "xp": 62.0,
        "xk": 71.0
    },
    {
        "class": "Graveyard",
        "xp": 49.0,
        "xk": 96.0
    },
    {
        "class": "Landscape",
        "xp": 48.0,
        "xk": 96.0
    },
    {
        "class": "Mine",
        "xp": 39.0,
        "xk": 122.0
    },
    {
        "class": "Monument",
        "xp": 58.0,
        "xk": 122.0
    },
    {
        "class": "Motor vehicle",
        "xp": 59.0,
        "xk": 120.0
    },
    {
        "class": "Museum",
        "xp": 63.0,
        "xk": 122.0
    },
    {
        "class": "Park",
        "xp": 35.0,
        "xk": 122.0
    },
    {
        "class": "Plants",
        "xp": 43.0,
        "xk": 72.0
    },
    {
        "class": "Road",
        "xp": 59.0,
        "xk": 109.0
    },
    {
        "class": "Rocks",
        "xp": 43.0,
        "xk": 73.0
    },
    {
        "class": "Trees",
        "xp": 16.0,
        "xk": 72.0
    },
    {
        "class": "Windows",
        "xp": 60.0,
        "xk": 80.0
    },
    {
        "class": "Church",
        "xp": 54.0,
        "xk": 76.0
    },
    {
        "class": "City",
        "xp": 49.0,
        "xk": 68.0
    },
    {
        "class": "Cross",
        "xp": 43.0,
        "xk": 76.0
    },
    {
        "class": "Cultural institution",
        "xp": 63.0,
        "xk": 88.0
    },
    {
        "class": "Footpath",
        "xp": 54.0,
        "xk": 76.0
    },
    {
        "class": "Forest",
        "xp": 35.0,
        "xk": 73.0
    },
    {
        "class": "Grass",
        "xp": 62.0,
        "xk": 71.0
    },
    {
        "class": "Graveyard",
        "xp": 49.0,
        "xk": 96.0
    },
    {
        "class": "Landscape",
        "xp": 48.0,
        "xk": 96.0
    },
    {
        "class": "Mine",
        "xp": 39.0,
        "xk": 122.0
    },
    {
        "class": "Monument",
        "xp": 58.0,
        "xk": 122.0
    },
    {
        "class": "Motor vehicle",
        "xp": 59.0,
        "xk": 120.0
    },
    {
        "class": "Museum",
        "xp": 63.0,
        "xk": 122.0
    },
    {
        "class": "Park",
        "xp": 35.0,
        "xk": 122.0
    },
    {
        "class": "Plants",
        "xp": 43.0,
        "xk": 72.0
    },
    {
        "class": "Road",
        "xp": 59.0,
        "xk": 109.0
    },
    {
        "class": "Rocks",
        "xp": 43.0,
        "xk": 73.0
    },
    {
        "class": "Trees",
        "xp": 16.0,
        "xk": 72.0
    },
    {
        "class": "Windows",
        "xp": 60.0,
        "xk": 80.0
    },
    {
        "class": "Church",
        "xp": 54.0,
        "xk": 76.0
    },
    {
        "class": "Cross",
        "xp": 43.0,
        "xk": 76.0
    },
    {
        "class": "Cultural institution",
        "xp": 63.0,
        "xk": 88.0
    },
    {
        "class": "Footpath",
        "xp": 54.0,
        "xk": 76.0
    },
    {
        "class": "Forest",
        "xp": 35.0,
        "xk": 73.0
    },
    {
        "class": "Grass",
        "xp": 62.0,
        "xk": 71.0
    },
    {
        "class": "Graveyard",
        "xp": 49.0,
        "xk": 96.0
    },
    {
        "class": "Landscape",
        "xp": 48.0,
        "xk": 96.0
    },
    {
        "class": "Mine",
        "xp": 39.0,
        "xk": 122.0
    },
    {
        "class": "Monument",
        "xp": 58.0,
        "xk": 122.0
    },
    {
        "class": "Motor vehicle",
        "xp": 59.0,
        "xk": 120.0
    },
    {
        "class": "Museum",
        "xp": 63.0,
        "xk": 122.0
    },
    {
        "class": "Park",
        "xp": 35.0,
        "xk": 122.0
    },
    {
        "class": "Plants",
        "xp": 43.0,
        "xk": 72.0
    },
    {
        "class": "Road",
        "xp": 59.0,
        "xk": 109.0
    },
    {
        "class": "Rocks",
        "xp": 43.0,
        "xk": 73.0
    },
    {
        "class": "Trees",
        "xp": 16.0,
        "xk": 72.0
    },
    {
        "class": "Windows",
        "xp": 60.0,
        "xk": 80.0
    },
    {
        "class": "Church",
        "xp": 54.0,
        "xk": 76.0
    },
    {
        "class": "Cross",
        "xp": 43.0,
        "xk": 76.0
    },
    {
        "class": "Cultural institution",
        "xp": 63.0,
        "xk": 88.0
    },
    {
        "class": "Footpath",
        "xp": 54.0,
        "xk": 76.0
    },
    {
        "class": "Forest",
        "xp": 35.0,
        "xk": 73.0
    },
    {
        "class": "Grass",
        "xp": 62.0,
        "xk": 71.0
    },
    {
        "class": "Graveyard",
        "xp": 49.0,
        "xk": 96.0
    },
    {
        "class": "Landscape",
        "xp": 48.0,
        "xk": 96.0
    },
    {
        "class": "Mine",
        "xp": 39.0,
        "xk": 122.0
    },
    {
        "class": "Monument",
        "xp": 58.0,
        "xk": 122.0
    },
    {
        "class": "Motor vehicle",
        "xp": 59.0,
        "xk": 120.0
    },
    {
        "class": "Museum",
        "xp": 63.0,
        "xk": 122.0
    },
    {
        "class": "Park",
        "xp": 35.0,
        "xk": 122.0
    },
    {
        "class": "Plants",
        "xp": 43.0,
        "xk": 72.0
    },
    {
        "class": "Road",
        "xp": 59.0,
        "xk": 109.0
    },
    {
        "class": "Rocks",
        "xp": 43.0,
        "xk": 73.0
    },
    {
        "class": "Trees",
        "xp": 16.0,
        "xk": 72.0
    },
    {
        "class": "Windows",
        "xp": 60.0,
        "xk": 80.0
    },
    {
        "class": "Church",
        "xp": 54.0,
        "xk": 76.0
    },
    {
        "class": "Cross",
        "xp": 43.0,
        "xk": 76.0
    },
    {
        "class": "Cultural institution",
        "xp": 63.0,
        "xk": 88.0
    },
    {
        "class": "Footpath",
        "xp": 54.0,
        "xk": 76.0
    },
    {
        "class": "Forest",
        "xp": 35.0,
        "xk": 73.0
    },
    {
        "class": "Grass",
        "xp": 62.0,
        "xk": 71.0
    },
    {
        "class": "Graveyard",
        "xp": 49.0,
        "xk": 96.0
    },
    {
        "class": "Landscape",
        "xp": 48.0,
        "xk": 96.0
    },
    {
        "class": "Mine",
        "xp": 39.0,
        "xk": 122.0
    },
    {
        "class": "Monument",
        "xp": 58.0,
        "xk": 122.0
    },
    {
        "class": "Motor vehicle",
        "xp": 59.0,
        "xk": 120.0
    },
    {
        "class": "Museum",
        "xp": 63.0,
        "xk": 122.0
    },
    {
        "class": "Park",
        "xp": 35.0,
        "xk": 122.0
    },
    {
        "class": "Plants",
        "xp": 43.0,
        "xk": 72.0
    },
    {
        "class": "Road",
        "xp": 59.0,
        "xk": 109.0
    },
    {
        "class": "Rocks",
        "xp": 43.0,
        "xk": 73.0
    },
    {
        "class": "Trees",
        "xp": 16.0,
        "xk": 72.0
    },
    {
        "class": "Windows",
        "xp": 60.0,
        "xk": 80.0
    },
    {
        "class": "Church",
        "xp": 54.0,
        "xk": 76.0
    },
    {
        "class": "Cross",
        "xp": 43.0,
        "xk": 76.0
    },
    {
        "class": "Cultural institution",
        "xp": 63.0,
        "xk": 88.0
    },
    {
        "class": "Footpath",
        "xp": 54.0,
        "xk": 76.0
    },
    {
        "class": "Forest",
        "xp": 35.0,
        "xk": 73.0
    },
    {
        "class": "Graveyard",
        "xp": 49.0,
        "xk": 96.0
    },
    {
        "class": "Landscape",
        "xp": 48.0,
        "xk": 96.0
    },
    {
        "class": "Mine",
        "xp": 39.0,
        "xk": 122.0
    },
    {
        "class": "Monument",
        "xp": 58.0,
        "xk": 122.0
    },
    {
        "class": "Motor vehicle",
        "xp": 59.0,
        "xk": 120.0
    },
    {
        "class": "Museum",
        "xp": 63.0,
        "xk": 122.0
    },
    {
        "class": "Park",
        "xp": 35.0,
        "xk": 122.0
    },
    {
        "class": "Plants",
        "xp": 43.0,
        "xk": 72.0
    },
    {
        "class": "Road",
        "xp": 59.0,
        "xk": 109.0
    },
    {
        "class": "Rocks",
        "xp": 43.0,
        "xk": 73.0
    },
    {
        "class": "Trees",
        "xp": 16.0,
        "xk": 72.0
    },
    {
        "class": "Windows",
        "xp": 60.0,
        "xk": 80.0
    },
    {
        "class": "Church",
        "xp": 54.0,
        "xk": 76.0
    },
    {
        "class": "Cross",
        "xp": 43.0,
        "xk": 76.0
    },
    {
        "class": "Cultural institution",
        "xp": 63.0,
        "xk": 88.0
    },
    {
        "class": "Footpath",
        "xp": 54.0,
        "xk": 76.0
    },
    {
        "class": "Forest",
        "xp": 35.0,
        "xk": 73.0
    },
    {
        "class": "Graveyard",
        "xp": 49.0,
        "xk": 96.0
    },
    {
        "class": "Landscape",
        "xp": 48.0,
        "xk": 96.0
    },
    {
        "class": "Mine",
        "xp": 39.0,
        "xk": 122.0
    },
    {
        "class": "Monument",
        "xp": 58.0,
        "xk": 122.0
    },
    {
        "class": "Motor vehicle",
        "xp": 59.0,
        "xk": 120.0
    },
    {
        "class": "Museum",
        "xp": 63.0,
        "xk": 122.0
    },
    {
        "class": "Park",
        "xp": 35.0,
        "xk": 122.0
    },
    {
        "class": "Road",
        "xp": 59.0,
        "xk": 109.0
    },
    {
        "class": "Rocks",
        "xp": 43.0,
        "xk": 73.0
    },
    {
        "class": "Windows",
        "xp": 60.0,
        "xk": 80.0
    },
    {
        "class": "Building",
        "xp": 49.0,
        "xk": 78.0
    },
    {
        "class": "Church",
        "xp": 54.0,
        "xk": 76.0
    },
    {
        "class": "City",
        "xp": 70.0,
        "xk": 89.0
    },
    {
        "class": "Cross",
        "xp": 43.0,
        "xk": 76.0
    },
    {
        "class": "Cultural institution",
        "xp": 63.0,
        "xk": 88.0
    },
    {
        "class": "Footpath",
        "xp": 54.0,
        "xk": 76.0
    },
    {
        "class": "Graveyard",
        "xp": 49.0,
        "xk": 96.0
    },
    {
        "class": "Landscape",
        "xp": 48.0,
        "xk": 96.0
    },
    {
        "class": "Mine",
        "xp": 39.0,
        "xk": 122.0
    },
    {
        "class": "Monument",
        "xp": 58.0,
        "xk": 122.0
    },
    {
        "class": "Motor vehicle",
        "xp": 59.0,
        "xk": 120.0
    },
    {
        "class": "Museum",
        "xp": 63.0,
        "xk": 122.0
    },
    {
        "class": "Park",
        "xp": 35.0,
        "xk": 122.0
    },
    {
        "class": "Road",
        "xp": 59.0,
        "xk": 109.0
    },
    {
        "class": "Windows",
        "xp": 60.0,
        "xk": 80.0
    },
    {
        "class": "Building",
        "xp": 49.0,
        "xk": 78.0
    },
    {
        "class": "Church",
        "xp": 54.0,
        "xk": 76.0
    },
    {
        "class": "City",
        "xp": 70.0,
        "xk": 89.0
    },
    {
        "class": "Cross",
        "xp": 43.0,
        "xk": 76.0
    },
    {
        "class": "Cultural institution",
        "xp": 63.0,
        "xk": 88.0
    },
    {
        "class": "Footpath",
        "xp": 54.0,
        "xk": 76.0
    },
    {
        "class": "Graveyard",
        "xp": 49.0,
        "xk": 96.0
    },
    {
        "class": "Landscape",
        "xp": 48.0,
        "xk": 96.0
    },
    {
        "class": "Mine",
        "xp": 39.0,
        "xk": 122.0
    },
    {
        "class": "Monument",
        "xp": 58.0,
        "xk": 122.0
    },
    {
        "class": "Motor vehicle",
        "xp": 59.0,
        "xk": 120.0
    },
    {
        "class": "Museum",
        "xp": 63.0,
        "xk": 122.0
    },
    {
        "class": "Park",
        "xp": 35.0,
        "xk": 122.0
    },
    {
        "class": "Road",
        "xp": 59.0,
        "xk": 109.0
    },
    {
        "class": "Windows",
        "xp": 60.0,
        "xk": 80.0
    },
    {
        "class": "Building",
        "xp": 49.0,
        "xk": 78.0
    },
    {
        "class": "Church",
        "xp": 54.0,
        "xk": 76.0
    },
    {
        "class": "City",
        "xp": 70.0,
        "xk": 89.0
    },
    {
        "class": "Cross",
        "xp": 43.0,
        "xk": 76.0
    },
    {
        "class": "Cultural institution",
        "xp": 63.0,
        "xk": 88.0
    },
    {
        "class": "Footpath",
        "xp": 54.0,
        "xk": 76.0
    },
    {
        "class": "Graveyard",
        "xp": 49.0,
        "xk": 96.0
    },
    {
        "class": "Landscape",
        "xp": 48.0,
        "xk": 96.0
    },
    {
        "class": "Mine",
        "xp": 39.0,
        "xk": 122.0
    },
    {
        "class": "Monument",
        "xp": 58.0,
        "xk": 122.0
    },
    {
        "class": "Motor vehicle",
        "xp": 59.0,
        "xk": 120.0
    },
    {
        "class": "Museum",
        "xp": 63.0,
        "xk": 122.0
    },
    {
        "class": "Park",
        "xp": 35.0,
        "xk": 122.0
    },
    {
        "class": "Road",
        "xp": 59.0,
        "xk": 109.0
    },
    {
        "class": "Windows",
        "xp": 60.0,
        "xk": 80.0
    },
    {
        "class": "Building",
        "xp": 49.0,
        "xk": 78.0
    },
    {
        "class": "City",
        "xp": 70.0,
        "xk": 89.0
    },
    {
        "class": "Cultural institution",
        "xp": 63.0,
        "xk": 88.0
    },
    {
        "class": "Graveyard",
        "xp": 49.0,
        "xk": 96.0
    },
    {
        "class": "Landscape",
        "xp": 48.0,
        "xk": 96.0
    },
    {
        "class": "Mine",
        "xp": 39.0,
        "xk": 122.0
    },
    {
        "class": "Monument",
        "xp": 58.0,
        "xk": 122.0
    },
    {
        "class": "Motor vehicle",
        "xp": 59.0,
        "xk": 120.0
    },
    {
        "class": "Museum",
        "xp": 63.0,
        "xk": 122.0
    },
    {
        "class": "Park",
        "xp": 35.0,
        "xk": 122.0
    },
    {
        "class": "Road",
        "xp": 59.0,
        "xk": 109.0
    },
    {
        "class": "Windows",
        "xp": 60.0,
        "xk": 80.0
    },
    {
        "class": "Building",
        "xp": 49.0,
        "xk": 78.0
    },
    {
        "class": "City",
        "xp": 70.0,
        "xk": 89.0
    },
    {
        "class": "Cultural institution",
        "xp": 63.0,
        "xk": 88.0
    },
    {
        "class": "Graveyard",
        "xp": 49.0,
        "xk": 96.0
    },
    {
        "class": "Landscape",
        "xp": 48.0,
        "xk": 96.0
    },
    {
        "class": "Mine",
        "xp": 39.0,
        "xk": 122.0
    },
    {
        "class": "Monument",
        "xp": 58.0,
        "xk": 122.0
    },
    {
        "class": "Motor vehicle",
        "xp": 59.0,
        "xk": 120.0
    },
    {
        "class": "Museum",
        "xp": 63.0,
        "xk": 122.0
    },
    {
        "class": "Park",
        "xp": 35.0,
        "xk": 122.0
    },
    {
        "class": "Road",
        "xp": 59.0,
        "xk": 109.0
    },
    {
        "class": "Windows",
        "xp": 60.0,
        "xk": 80.0
    },
    {
        "class": "City",
        "xp": 70.0,
        "xk": 89.0
    },
    {
        "class": "Cultural institution",
        "xp": 63.0,
        "xk": 88.0
    },
    {
        "class": "Graveyard",
        "xp": 49.0,
        "xk": 96.0
    },
    {
        "class": "Landscape",
        "xp": 48.0,
        "xk": 96.0
    },
    {
        "class": "Mine",
        "xp": 39.0,
        "xk": 122.0
    },
    {
        "class": "Monument",
        "xp": 58.0,
        "xk": 122.0
    },
    {
        "class": "Motor vehicle",
        "xp": 59.0,
        "xk": 120.0
    },
    {
        "class": "Museum",
        "xp": 63.0,
        "xk": 122.0
    },
    {
        "class": "Park",
        "xp": 35.0,
        "xk": 122.0
    },
    {
        "class": "Road",
        "xp": 59.0,
        "xk": 109.0
    },
    {
        "class": "Windows",
        "xp": 60.0,
        "xk": 80.0
    },
    {
        "class": "City",
        "xp": 70.0,
        "xk": 89.0
    },
    {
        "class": "Cultural institution",
        "xp": 63.0,
        "xk": 88.0
    },
    {
        "class": "Footpath",
        "xp": 78.0,
        "xk": 89.0
    },
    {
        "class": "Graveyard",
        "xp": 49.0,
        "xk": 96.0
    },
    {
        "class": "Landscape",
        "xp": 48.0,
        "xk": 96.0
    },
    {
        "class": "Mine",
        "xp": 39.0,
        "xk": 122.0
    },
    {
        "class": "Monument",
        "xp": 58.0,
        "xk": 122.0
    },
    {
        "class": "Motor vehicle",
        "xp": 59.0,
        "xk": 120.0
    },
    {
        "class": "Museum",
        "xp": 63.0,
        "xk": 122.0
    },
    {
        "class": "Park",
        "xp": 35.0,
        "xk": 122.0
    },
    {
        "class": "River",
        "xp": 76.0,
        "xk": 122.0
    },
    {
        "class": "Road",
        "xp": 59.0,
        "xk": 109.0
    },
    {
        "class": "Windows",
        "xp": 60.0,
        "xk": 80.0
    },
    {
        "class": "City",
        "xp": 70.0,
        "xk": 89.0
    },
    {
        "class": "Cultural institution",
        "xp": 63.0,
        "xk": 88.0
    },
    {
        "class": "Footpath",
        "xp": 78.0,
        "xk": 89.0
    },
    {
        "class": "Graveyard",
        "xp": 49.0,
        "xk": 96.0
    },
    {
        "class": "Landscape",
        "xp": 48.0,
        "xk": 96.0
    },
    {
        "class": "Mine",
        "xp": 39.0,
        "xk": 122.0
    },
    {
        "class": "Monument",
        "xp": 58.0,
        "xk": 122.0
    },
    {
        "class": "Motor vehicle",
        "xp": 59.0,
        "xk": 120.0
    },
    {
        "class": "Museum",
        "xp": 63.0,
        "xk": 122.0
    },
    {
        "class": "Park",
        "xp": 35.0,
        "xk": 122.0
    },
    {
        "class": "Person",
        "xp": 63.0,
        "xk": 95.0
    },
    {
        "class": "River",
        "xp": 76.0,
        "xk": 122.0
    },
    {
        "class": "Road",
        "xp": 59.0,
        "xk": 109.0
    },
    {
        "class": "City",
        "xp": 70.0,
        "xk": 89.0
    },
    {
        "class": "Cultural institution",
        "xp": 63.0,
        "xk": 88.0
    },
    {
        "class": "Footpath",
        "xp": 78.0,
        "xk": 89.0
    },
    {
        "class": "Forest",
        "xp": 75.0,
        "xk": 82.0
    },
    {
        "class": "Graveyard",
        "xp": 49.0,
        "xk": 96.0
    },
    {
        "class": "Landscape",
        "xp": 48.0,
        "xk": 96.0
    },
    {
        "class": "Mine",
        "xp": 39.0,
        "xk": 122.0
    },
    {
        "class": "Monument",
        "xp": 58.0,
        "xk": 122.0
    },
    {
        "class": "Motor vehicle",
        "xp": 59.0,
        "xk": 120.0
    },
    {
        "class": "Museum",
        "xp": 63.0,
        "xk": 122.0
    },
    {
        "class": "Park",
        "xp": 35.0,
        "xk": 122.0
    },
    {
        "class": "Person",
        "xp": 63.0,
        "xk": 95.0
    },
    {
        "class": "River",
        "xp": 76.0,
        "xk": 122.0
    },
    {
        "class": "Road",
        "xp": 59.0,
        "xk": 109.0
    },
    {
        "class": "City",
        "xp": 70.0,
        "xk": 89.0
    },
    {
        "class": "Cultural institution",
        "xp": 63.0,
        "xk": 88.0
    },
    {
        "class": "Footpath",
        "xp": 78.0,
        "xk": 89.0
    },
    {
        "class": "Graveyard",
        "xp": 49.0,
        "xk": 96.0
    },
    {
        "class": "Landscape",
        "xp": 48.0,
        "xk": 96.0
    },
    {
        "class": "Mine",
        "xp": 39.0,
        "xk": 122.0
    },
    {
        "class": "Monument",
        "xp": 58.0,
        "xk": 122.0
    },
    {
        "class": "Motor vehicle",
        "xp": 59.0,
        "xk": 120.0
    },
    {
        "class": "Museum",
        "xp": 63.0,
        "xk": 122.0
    },
    {
        "class": "Park",
        "xp": 35.0,
        "xk": 122.0
    },
    {
        "class": "Person",
        "xp": 63.0,
        "xk": 95.0
    },
    {
        "class": "River",
        "xp": 76.0,
        "xk": 122.0
    },
    {
        "class": "Road",
        "xp": 59.0,
        "xk": 109.0
    },
    {
        "class": "Church",
        "xp": 78.0,
        "xk": 122.0
    },
    {
        "class": "City",
        "xp": 70.0,
        "xk": 89.0
    },
    {
        "class": "Cultural institution",
        "xp": 63.0,
        "xk": 88.0
    },
    {
        "class": "Footpath",
        "xp": 78.0,
        "xk": 89.0
    },
    {
        "class": "Graveyard",
        "xp": 49.0,
        "xk": 96.0
    },
    {
        "class": "Landscape",
        "xp": 48.0,
        "xk": 96.0
    },
    {
        "class": "Mine",
        "xp": 39.0,
        "xk": 122.0
    },
    {
        "class": "Monument",
        "xp": 58.0,
        "xk": 122.0
    },
    {
        "class": "Motor vehicle",
        "xp": 59.0,
        "xk": 120.0
    },
    {
        "class": "Museum",
        "xp": 63.0,
        "xk": 122.0
    },
    {
        "class": "Park",
        "xp": 35.0,
        "xk": 122.0
    },
    {
        "class": "Person",
        "xp": 63.0,
        "xk": 95.0
    },
    {
        "class": "River",
        "xp": 76.0,
        "xk": 122.0
    },
    {
        "class": "Road",
        "xp": 59.0,
        "xk": 109.0
    },
    {
        "class": "Rocks",
        "xp": 75.0,
        "xk": 84.0
    },
    {
        "class": "Windows",
        "xp": 82.0,
        "xk": 110.0
    },
    {
        "class": "Church",
        "xp": 78.0,
        "xk": 122.0
    },
    {
        "class": "City",
        "xp": 70.0,
        "xk": 89.0
    },
    {
        "class": "Cultural institution",
        "xp": 63.0,
        "xk": 88.0
    },
    {
        "class": "Footpath",
        "xp": 78.0,
        "xk": 89.0
    },
    {
        "class": "Graveyard",
        "xp": 49.0,
        "xk": 96.0
    },
    {
        "class": "Landscape",
        "xp": 48.0,
        "xk": 96.0
    },
    {
        "class": "Mine",
        "xp": 39.0,
        "xk": 122.0
    },
    {
        "class": "Monument",
        "xp": 58.0,
        "xk": 122.0
    },
    {
        "class": "Motor vehicle",
        "xp": 59.0,
        "xk": 120.0
    },
    {
        "class": "Museum",
        "xp": 63.0,
        "xk": 122.0
    },
    {
        "class": "Park",
        "xp": 35.0,
        "xk": 122.0
    },
    {
        "class": "Person",
        "xp": 63.0,
        "xk": 95.0
    },
    {
        "class": "River",
        "xp": 76.0,
        "xk": 122.0
    },
    {
        "class": "Road",
        "xp": 59.0,
        "xk": 109.0
    },
    {
        "class": "Windows",
        "xp": 82.0,
        "xk": 110.0
    },
    {
        "class": "Church",
        "xp": 78.0,
        "xk": 122.0
    },
    {
        "class": "City",
        "xp": 70.0,
        "xk": 89.0
    },
    {
        "class": "Cultural institution",
        "xp": 63.0,
        "xk": 88.0
    },
    {
        "class": "Footpath",
        "xp": 78.0,
        "xk": 89.0
    },
    {
        "class": "Graveyard",
        "xp": 49.0,
        "xk": 96.0
    },
    {
        "class": "Landscape",
        "xp": 48.0,
        "xk": 96.0
    },
    {
        "class": "Mine",
        "xp": 39.0,
        "xk": 122.0
    },
    {
        "class": "Monument",
        "xp": 58.0,
        "xk": 122.0
    },
    {
        "class": "Motor vehicle",
        "xp": 59.0,
        "xk": 120.0
    },
    {
        "class": "Museum",
        "xp": 63.0,
        "xk": 122.0
    },
    {
        "class": "Park",
        "xp": 35.0,
        "xk": 122.0
    },
    {
        "class": "Person",
        "xp": 63.0,
        "xk": 95.0
    },
    {
        "class": "River",
        "xp": 76.0,
        "xk": 122.0
    },
    {
        "class": "Road",
        "xp": 59.0,
        "xk": 109.0
    },
    {
        "class": "Windows",
        "xp": 82.0,
        "xk": 110.0
    },
    {
        "class": "Building",
        "xp": 80.0,
        "xk": 87.0
    },
    {
        "class": "Church",
        "xp": 78.0,
        "xk": 122.0
    },
    {
        "class": "City",
        "xp": 70.0,
        "xk": 89.0
    },
    {
        "class": "Cultural institution",
        "xp": 63.0,
        "xk": 88.0
    },
    {
        "class": "Footpath",
        "xp": 78.0,
        "xk": 89.0
    },
    {
        "class": "Graveyard",
        "xp": 49.0,
        "xk": 96.0
    },
    {
        "class": "Landscape",
        "xp": 48.0,
        "xk": 96.0
    },
    {
        "class": "Mine",
        "xp": 39.0,
        "xk": 122.0
    },
    {
        "class": "Monument",
        "xp": 58.0,
        "xk": 122.0
    },
    {
        "class": "Motor vehicle",
        "xp": 59.0,
        "xk": 120.0
    },
    {
        "class": "Museum",
        "xp": 63.0,
        "xk": 122.0
    },
    {
        "class": "Park",
        "xp": 35.0,
        "xk": 122.0
    },
    {
        "class": "Person",
        "xp": 63.0,
        "xk": 95.0
    },
    {
        "class": "River",
        "xp": 76.0,
        "xk": 122.0
    },
    {
        "class": "Road",
        "xp": 59.0,
        "xk": 109.0
    },
    {
        "class": "Windows",
        "xp": 82.0,
        "xk": 110.0
    },
    {
        "class": "Church",
        "xp": 78.0,
        "xk": 122.0
    },
    {
        "class": "City",
        "xp": 70.0,
        "xk": 89.0
    },
    {
        "class": "Cultural institution",
        "xp": 63.0,
        "xk": 88.0
    },
    {
        "class": "Footpath",
        "xp": 78.0,
        "xk": 89.0
    },
    {
        "class": "Forest",
        "xp": 84.0,
        "xk": 122.0
    },
    {
        "class": "Graveyard",
        "xp": 49.0,
        "xk": 96.0
    },
    {
        "class": "Landscape",
        "xp": 48.0,
        "xk": 96.0
    },
    {
        "class": "Mine",
        "xp": 39.0,
        "xk": 122.0
    },
    {
        "class": "Monument",
        "xp": 58.0,
        "xk": 122.0
    },
    {
        "class": "Motor vehicle",
        "xp": 59.0,
        "xk": 120.0
    },
    {
        "class": "Museum",
        "xp": 63.0,
        "xk": 122.0
    },
    {
        "class": "Park",
        "xp": 35.0,
        "xk": 122.0
    },
    {
        "class": "Person",
        "xp": 63.0,
        "xk": 95.0
    },
    {
        "class": "River",
        "xp": 76.0,
        "xk": 122.0
    },
    {
        "class": "Road",
        "xp": 59.0,
        "xk": 109.0
    },
    {
        "class": "Rocks",
        "xp": 86.0,
        "xk": 110.0
    },
    {
        "class": "Windows",
        "xp": 82.0,
        "xk": 110.0
    },
    {
        "class": "Church",
        "xp": 78.0,
        "xk": 122.0
    },
    {
        "class": "City",
        "xp": 70.0,
        "xk": 89.0
    },
    {
        "class": "Footpath",
        "xp": 78.0,
        "xk": 89.0
    },
    {
        "class": "Forest",
        "xp": 84.0,
        "xk": 122.0
    },
    {
        "class": "Graveyard",
        "xp": 49.0,
        "xk": 96.0
    },
    {
        "class": "Landscape",
        "xp": 48.0,
        "xk": 96.0
    },
    {
        "class": "Mine",
        "xp": 39.0,
        "xk": 122.0
    },
    {
        "class": "Monument",
        "xp": 58.0,
        "xk": 122.0
    },
    {
        "class": "Motor vehicle",
        "xp": 59.0,
        "xk": 120.0
    },
    {
        "class": "Museum",
        "xp": 63.0,
        "xk": 122.0
    },
    {
        "class": "Park",
        "xp": 35.0,
        "xk": 122.0
    },
    {
        "class": "Person",
        "xp": 63.0,
        "xk": 95.0
    },
    {
        "class": "River",
        "xp": 76.0,
        "xk": 122.0
    },
    {
        "class": "Road",
        "xp": 59.0,
        "xk": 109.0
    },
    {
        "class": "Rocks",
        "xp": 86.0,
        "xk": 110.0
    },
    {
        "class": "Windows",
        "xp": 82.0,
        "xk": 110.0
    },
    {
        "class": "Church",
        "xp": 78.0,
        "xk": 122.0
    },
    {
        "class": "Cross",
        "xp": 78.0,
        "xk": 90.0
    },
    {
        "class": "Forest",
        "xp": 84.0,
        "xk": 122.0
    },
    {
        "class": "Graveyard",
        "xp": 49.0,
        "xk": 96.0
    },
    {
        "class": "Landscape",
        "xp": 48.0,
        "xk": 96.0
    },
    {
        "class": "Mine",
        "xp": 39.0,
        "xk": 122.0
    },
    {
        "class": "Monument",
        "xp": 58.0,
        "xk": 122.0
    },
    {
        "class": "Motor vehicle",
        "xp": 59.0,
        "xk": 120.0
    },
    {
        "class": "Museum",
        "xp": 63.0,
        "xk": 122.0
    },
    {
        "class": "Park",
        "xp": 35.0,
        "xk": 122.0
    },
    {
        "class": "Person",
        "xp": 63.0,
        "xk": 95.0
    },
    {
        "class": "River",
        "xp": 76.0,
        "xk": 122.0
    },
    {
        "class": "Road",
        "xp": 59.0,
        "xk": 109.0
    },
    {
        "class": "Rocks",
        "xp": 86.0,
        "xk": 110.0
    },
    {
        "class": "Windows",
        "xp": 82.0,
        "xk": 110.0
    },
    {
        "class": "Church",
        "xp": 78.0,
        "xk": 122.0
    },
    {
        "class": "Forest",
        "xp": 84.0,
        "xk": 122.0
    },
    {
        "class": "Graveyard",
        "xp": 49.0,
        "xk": 96.0
    },
    {
        "class": "Landscape",
        "xp": 48.0,
        "xk": 96.0
    },
    {
        "class": "Mine",
        "xp": 39.0,
        "xk": 122.0
    },
    {
        "class": "Monument",
        "xp": 58.0,
        "xk": 122.0
    },
    {
        "class": "Motor vehicle",
        "xp": 59.0,
        "xk": 120.0
    },
    {
        "class": "Museum",
        "xp": 63.0,
        "xk": 122.0
    },
    {
        "class": "Park",
        "xp": 35.0,
        "xk": 122.0
    },
    {
        "class": "Person",
        "xp": 63.0,
        "xk": 95.0
    },
    {
        "class": "River",
        "xp": 76.0,
        "xk": 122.0
    },
    {
        "class": "Road",
        "xp": 59.0,
        "xk": 109.0
    },
    {
        "class": "Rocks",
        "xp": 86.0,
        "xk": 110.0
    },
    {
        "class": "Windows",
        "xp": 82.0,
        "xk": 110.0
    },
    {
        "class": "Church",
        "xp": 78.0,
        "xk": 122.0
    },
    {
        "class": "Cultural institution",
        "xp": 90.0,
        "xk": 122.0
    },
    {
        "class": "Forest",
        "xp": 84.0,
        "xk": 122.0
    },
    {
        "class": "Graveyard",
        "xp": 49.0,
        "xk": 96.0
    },
    {
        "class": "Landscape",
        "xp": 48.0,
        "xk": 96.0
    },
    {
        "class": "Mine",
        "xp": 39.0,
        "xk": 122.0
    },
    {
        "class": "Monument",
        "xp": 58.0,
        "xk": 122.0
    },
    {
        "class": "Motor vehicle",
        "xp": 59.0,
        "xk": 120.0
    },
    {
        "class": "Museum",
        "xp": 63.0,
        "xk": 122.0
    },
    {
        "class": "Park",
        "xp": 35.0,
        "xk": 122.0
    },
    {
        "class": "Person",
        "xp": 63.0,
        "xk": 95.0
    },
    {
        "class": "River",
        "xp": 76.0,
        "xk": 122.0
    },
    {
        "class": "Road",
        "xp": 59.0,
        "xk": 109.0
    },
    {
        "class": "Rocks",
        "xp": 86.0,
        "xk": 110.0
    },
    {
        "class": "Windows",
        "xp": 82.0,
        "xk": 110.0
    },
    {
        "class": "Church",
        "xp": 78.0,
        "xk": 122.0
    },
    {
        "class": "Cultural institution",
        "xp": 90.0,
        "xk": 122.0
    },
    {
        "class": "Forest",
        "xp": 84.0,
        "xk": 122.0
    },
    {
        "class": "Graveyard",
        "xp": 49.0,
        "xk": 96.0
    },
    {
        "class": "Landscape",
        "xp": 48.0,
        "xk": 96.0
    },
    {
        "class": "Mine",
        "xp": 39.0,
        "xk": 122.0
    },
    {
        "class": "Monument",
        "xp": 58.0,
        "xk": 122.0
    },
    {
        "class": "Motor vehicle",
        "xp": 59.0,
        "xk": 120.0
    },
    {
        "class": "Museum",
        "xp": 63.0,
        "xk": 122.0
    },
    {
        "class": "Park",
        "xp": 35.0,
        "xk": 122.0
    },
    {
        "class": "Person",
        "xp": 63.0,
        "xk": 95.0
    },
    {
        "class": "River",
        "xp": 76.0,
        "xk": 122.0
    },
    {
        "class": "Road",
        "xp": 59.0,
        "xk": 109.0
    },
    {
        "class": "Rocks",
        "xp": 86.0,
        "xk": 110.0
    },
    {
        "class": "Windows",
        "xp": 82.0,
        "xk": 110.0
    },
    {
        "class": "Church",
        "xp": 78.0,
        "xk": 122.0
    },
    {
        "class": "Cultural institution",
        "xp": 90.0,
        "xk": 122.0
    },
    {
        "class": "Forest",
        "xp": 84.0,
        "xk": 122.0
    },
    {
        "class": "Graveyard",
        "xp": 49.0,
        "xk": 96.0
    },
    {
        "class": "Landscape",
        "xp": 48.0,
        "xk": 96.0
    },
    {
        "class": "Mine",
        "xp": 39.0,
        "xk": 122.0
    },
    {
        "class": "Monument",
        "xp": 58.0,
        "xk": 122.0
    },
    {
        "class": "Motor vehicle",
        "xp": 59.0,
        "xk": 120.0
    },
    {
        "class": "Museum",
        "xp": 63.0,
        "xk": 122.0
    },
    {
        "class": "Park",
        "xp": 35.0,
        "xk": 122.0
    },
    {
        "class": "Person",
        "xp": 63.0,
        "xk": 95.0
    },
    {
        "class": "River",
        "xp": 76.0,
        "xk": 122.0
    },
    {
        "class": "Road",
        "xp": 59.0,
        "xk": 109.0
    },
    {
        "class": "Rocks",
        "xp": 86.0,
        "xk": 110.0
    },
    {
        "class": "Windows",
        "xp": 82.0,
        "xk": 110.0
    },
    {
        "class": "Church",
        "xp": 78.0,
        "xk": 122.0
    },
    {
        "class": "Cultural institution",
        "xp": 90.0,
        "xk": 122.0
    },
    {
        "class": "Footpath",
        "xp": 91.0,
        "xk": 122.0
    },
    {
        "class": "Forest",
        "xp": 84.0,
        "xk": 122.0
    },
    {
        "class": "Graveyard",
        "xp": 49.0,
        "xk": 96.0
    },
    {
        "class": "Landscape",
        "xp": 48.0,
        "xk": 96.0
    },
    {
        "class": "Mine",
        "xp": 39.0,
        "xk": 122.0
    },
    {
        "class": "Monument",
        "xp": 58.0,
        "xk": 122.0
    },
    {
        "class": "Motor vehicle",
        "xp": 59.0,
        "xk": 120.0
    },
    {
        "class": "Museum",
        "xp": 63.0,
        "xk": 122.0
    },
    {
        "class": "Park",
        "xp": 35.0,
        "xk": 122.0
    },
    {
        "class": "Person",
        "xp": 63.0,
        "xk": 95.0
    },
    {
        "class": "River",
        "xp": 76.0,
        "xk": 122.0
    },
    {
        "class": "Road",
        "xp": 59.0,
        "xk": 109.0
    },
    {
        "class": "Rocks",
        "xp": 86.0,
        "xk": 110.0
    },
    {
        "class": "Windows",
        "xp": 82.0,
        "xk": 110.0
    },
    {
        "class": "Church",
        "xp": 78.0,
        "xk": 122.0
    },
    {
        "class": "City",
        "xp": 91.0,
        "xk": 109.0
    },
    {
        "class": "Cultural institution",
        "xp": 90.0,
        "xk": 122.0
    },
    {
        "class": "Footpath",
        "xp": 91.0,
        "xk": 122.0
    },
    {
        "class": "Forest",
        "xp": 84.0,
        "xk": 122.0
    },
    {
        "class": "Graveyard",
        "xp": 49.0,
        "xk": 96.0
    },
    {
        "class": "Landscape",
        "xp": 48.0,
        "xk": 96.0
    },
    {
        "class": "Mine",
        "xp": 39.0,
        "xk": 122.0
    },
    {
        "class": "Monument",
        "xp": 58.0,
        "xk": 122.0
    },
    {
        "class": "Motor vehicle",
        "xp": 59.0,
        "xk": 120.0
    },
    {
        "class": "Museum",
        "xp": 63.0,
        "xk": 122.0
    },
    {
        "class": "Park",
        "xp": 35.0,
        "xk": 122.0
    },
    {
        "class": "River",
        "xp": 76.0,
        "xk": 122.0
    },
    {
        "class": "Road",
        "xp": 59.0,
        "xk": 109.0
    },
    {
        "class": "Rocks",
        "xp": 86.0,
        "xk": 110.0
    },
    {
        "class": "Windows",
        "xp": 82.0,
        "xk": 110.0
    },
    {
        "class": "Church",
        "xp": 78.0,
        "xk": 122.0
    },
    {
        "class": "City",
        "xp": 91.0,
        "xk": 109.0
    },
    {
        "class": "Cultural institution",
        "xp": 90.0,
        "xk": 122.0
    },
    {
        "class": "Footpath",
        "xp": 91.0,
        "xk": 122.0
    },
    {
        "class": "Forest",
        "xp": 84.0,
        "xk": 122.0
    },
    {
        "class": "Mine",
        "xp": 39.0,
        "xk": 122.0
    },
    {
        "class": "Monument",
        "xp": 58.0,
        "xk": 122.0
    },
    {
        "class": "Motor vehicle",
        "xp": 59.0,
        "xk": 120.0
    },
    {
        "class": "Museum",
        "xp": 63.0,
        "xk": 122.0
    },
    {
        "class": "Park",
        "xp": 35.0,
        "xk": 122.0
    },
    {
        "class": "River",
        "xp": 76.0,
        "xk": 122.0
    },
    {
        "class": "Road",
        "xp": 59.0,
        "xk": 109.0
    },
    {
        "class": "Rocks",
        "xp": 86.0,
        "xk": 110.0
    },
    {
        "class": "Windows",
        "xp": 82.0,
        "xk": 110.0
    },
    {
        "class": "Church",
        "xp": 78.0,
        "xk": 122.0
    },
    {
        "class": "City",
        "xp": 91.0,
        "xk": 109.0
    },
    {
        "class": "Cultural institution",
        "xp": 90.0,
        "xk": 122.0
    },
    {
        "class": "Footpath",
        "xp": 91.0,
        "xk": 122.0
    },
    {
        "class": "Forest",
        "xp": 84.0,
        "xk": 122.0
    },
    {
        "class": "Mine",
        "xp": 39.0,
        "xk": 122.0
    },
    {
        "class": "Monument",
        "xp": 58.0,
        "xk": 122.0
    },
    {
        "class": "Motor vehicle",
        "xp": 59.0,
        "xk": 120.0
    },
    {
        "class": "Museum",
        "xp": 63.0,
        "xk": 122.0
    },
    {
        "class": "Park",
        "xp": 35.0,
        "xk": 122.0
    },
    {
        "class": "River",
        "xp": 76.0,
        "xk": 122.0
    },
    {
        "class": "Road",
        "xp": 59.0,
        "xk": 109.0
    },
    {
        "class": "Rocks",
        "xp": 86.0,
        "xk": 110.0
    },
    {
        "class": "Windows",
        "xp": 82.0,
        "xk": 110.0
    },
    {
        "class": "Church",
        "xp": 78.0,
        "xk": 122.0
    },
    {
        "class": "City",
        "xp": 91.0,
        "xk": 109.0
    },
    {
        "class": "Cultural institution",
        "xp": 90.0,
        "xk": 122.0
    },
    {
        "class": "Footpath",
        "xp": 91.0,
        "xk": 122.0
    },
    {
        "class": "Forest",
        "xp": 84.0,
        "xk": 122.0
    },
    {
        "class": "Mine",
        "xp": 39.0,
        "xk": 122.0
    },
    {
        "class": "Monument",
        "xp": 58.0,
        "xk": 122.0
    },
    {
        "class": "Motor vehicle",
        "xp": 59.0,
        "xk": 120.0
    },
    {
        "class": "Museum",
        "xp": 63.0,
        "xk": 122.0
    },
    {
        "class": "Park",
        "xp": 35.0,
        "xk": 122.0
    },
    {
        "class": "Person",
        "xp": 97.0,
        "xk": 109.0
    },
    {
        "class": "River",
        "xp": 76.0,
        "xk": 122.0
    },
    {
        "class": "Road",
        "xp": 59.0,
        "xk": 109.0
    },
    {
        "class": "Rocks",
        "xp": 86.0,
        "xk": 110.0
    },
    {
        "class": "Windows",
        "xp": 82.0,
        "xk": 110.0
    },
    {
        "class": "Church",
        "xp": 78.0,
        "xk": 122.0
    },
    {
        "class": "City",
        "xp": 91.0,
        "xk": 109.0
    },
    {
        "class": "Cultural institution",
        "xp": 90.0,
        "xk": 122.0
    },
    {
        "class": "Footpath",
        "xp": 91.0,
        "xk": 122.0
    },
    {
        "class": "Forest",
        "xp": 84.0,
        "xk": 122.0
    },
    {
        "class": "Graveyard",
        "xp": 98.0,
        "xk": 101.0
    },
    {
        "class": "Mine",
        "xp": 39.0,
        "xk": 122.0
    },
    {
        "class": "Monument",
        "xp": 58.0,
        "xk": 122.0
    },
    {
        "class": "Motor vehicle",
        "xp": 59.0,
        "xk": 120.0
    },
    {
        "class": "Museum",
        "xp": 63.0,
        "xk": 122.0
    },
    {
        "class": "Park",
        "xp": 35.0,
        "xk": 122.0
    },
    {
        "class": "Person",
        "xp": 97.0,
        "xk": 109.0
    },
    {
        "class": "River",
        "xp": 76.0,
        "xk": 122.0
    },
    {
        "class": "Road",
        "xp": 59.0,
        "xk": 109.0
    },
    {
        "class": "Rocks",
        "xp": 86.0,
        "xk": 110.0
    },
    {
        "class": "Windows",
        "xp": 82.0,
        "xk": 110.0
    },
    {
        "class": "Church",
        "xp": 78.0,
        "xk": 122.0
    },
    {
        "class": "City",
        "xp": 91.0,
        "xk": 109.0
    },
    {
        "class": "Cultural institution",
        "xp": 90.0,
        "xk": 122.0
    },
    {
        "class": "Footpath",
        "xp": 91.0,
        "xk": 122.0
    },
    {
        "class": "Forest",
        "xp": 84.0,
        "xk": 122.0
    },
    {
        "class": "Graveyard",
        "xp": 98.0,
        "xk": 101.0
    },
    {
        "class": "Mine",
        "xp": 39.0,
        "xk": 122.0
    },
    {
        "class": "Monument",
        "xp": 58.0,
        "xk": 122.0
    },
    {
        "class": "Motor vehicle",
        "xp": 59.0,
        "xk": 120.0
    },
    {
        "class": "Museum",
        "xp": 63.0,
        "xk": 122.0
    },
    {
        "class": "Park",
        "xp": 35.0,
        "xk": 122.0
    },
    {
        "class": "Person",
        "xp": 97.0,
        "xk": 109.0
    },
    {
        "class": "River",
        "xp": 76.0,
        "xk": 122.0
    },
    {
        "class": "Road",
        "xp": 59.0,
        "xk": 109.0
    },
    {
        "class": "Rocks",
        "xp": 86.0,
        "xk": 110.0
    },
    {
        "class": "Windows",
        "xp": 82.0,
        "xk": 110.0
    },
    {
        "class": "Church",
        "xp": 78.0,
        "xk": 122.0
    },
    {
        "class": "City",
        "xp": 91.0,
        "xk": 109.0
    },
    {
        "class": "Cultural institution",
        "xp": 90.0,
        "xk": 122.0
    },
    {
        "class": "Footpath",
        "xp": 91.0,
        "xk": 122.0
    },
    {
        "class": "Forest",
        "xp": 84.0,
        "xk": 122.0
    },
    {
        "class": "Mine",
        "xp": 39.0,
        "xk": 122.0
    },
    {
        "class": "Monument",
        "xp": 58.0,
        "xk": 122.0
    },
    {
        "class": "Motor vehicle",
        "xp": 59.0,
        "xk": 120.0
    },
    {
        "class": "Museum",
        "xp": 63.0,
        "xk": 122.0
    },
    {
        "class": "Park",
        "xp": 35.0,
        "xk": 122.0
    },
    {
        "class": "Person",
        "xp": 97.0,
        "xk": 109.0
    },
    {
        "class": "River",
        "xp": 76.0,
        "xk": 122.0
    },
    {
        "class": "Road",
        "xp": 59.0,
        "xk": 109.0
    },
    {
        "class": "Rocks",
        "xp": 86.0,
        "xk": 110.0
    },
    {
        "class": "Windows",
        "xp": 82.0,
        "xk": 110.0
    },
    {
        "class": "Church",
        "xp": 78.0,
        "xk": 122.0
    },
    {
        "class": "City",
        "xp": 91.0,
        "xk": 109.0
    },
    {
        "class": "Cultural institution",
        "xp": 90.0,
        "xk": 122.0
    },
    {
        "class": "Footpath",
        "xp": 91.0,
        "xk": 122.0
    },
    {
        "class": "Forest",
        "xp": 84.0,
        "xk": 122.0
    },
    {
        "class": "Mine",
        "xp": 39.0,
        "xk": 122.0
    },
    {
        "class": "Monument",
        "xp": 58.0,
        "xk": 122.0
    },
    {
        "class": "Motor vehicle",
        "xp": 59.0,
        "xk": 120.0
    },
    {
        "class": "Museum",
        "xp": 63.0,
        "xk": 122.0
    },
    {
        "class": "Park",
        "xp": 35.0,
        "xk": 122.0
    },
    {
        "class": "Person",
        "xp": 97.0,
        "xk": 109.0
    },
    {
        "class": "River",
        "xp": 76.0,
        "xk": 122.0
    },
    {
        "class": "Road",
        "xp": 59.0,
        "xk": 109.0
    },
    {
        "class": "Rocks",
        "xp": 86.0,
        "xk": 110.0
    },
    {
        "class": "Windows",
        "xp": 82.0,
        "xk": 110.0
    },
    {
        "class": "Church",
        "xp": 78.0,
        "xk": 122.0
    },
    {
        "class": "City",
        "xp": 91.0,
        "xk": 109.0
    },
    {
        "class": "Cultural institution",
        "xp": 90.0,
        "xk": 122.0
    },
    {
        "class": "Footpath",
        "xp": 91.0,
        "xk": 122.0
    },
    {
        "class": "Forest",
        "xp": 84.0,
        "xk": 122.0
    },
    {
        "class": "Mine",
        "xp": 39.0,
        "xk": 122.0
    },
    {
        "class": "Monument",
        "xp": 58.0,
        "xk": 122.0
    },
    {
        "class": "Motor vehicle",
        "xp": 59.0,
        "xk": 120.0
    },
    {
        "class": "Museum",
        "xp": 63.0,
        "xk": 122.0
    },
    {
        "class": "Park",
        "xp": 35.0,
        "xk": 122.0
    },
    {
        "class": "Person",
        "xp": 97.0,
        "xk": 109.0
    },
    {
        "class": "River",
        "xp": 76.0,
        "xk": 122.0
    },
    {
        "class": "Road",
        "xp": 59.0,
        "xk": 109.0
    },
    {
        "class": "Rocks",
        "xp": 86.0,
        "xk": 110.0
    },
    {
        "class": "Windows",
        "xp": 82.0,
        "xk": 110.0
    },
    {
        "class": "Church",
        "xp": 78.0,
        "xk": 122.0
    },
    {
        "class": "City",
        "xp": 91.0,
        "xk": 109.0
    },
    {
        "class": "Cultural institution",
        "xp": 90.0,
        "xk": 122.0
    },
    {
        "class": "Footpath",
        "xp": 91.0,
        "xk": 122.0
    },
    {
        "class": "Forest",
        "xp": 84.0,
        "xk": 122.0
    },
    {
        "class": "Mine",
        "xp": 39.0,
        "xk": 122.0
    },
    {
        "class": "Monument",
        "xp": 58.0,
        "xk": 122.0
    },
    {
        "class": "Motor vehicle",
        "xp": 59.0,
        "xk": 120.0
    },
    {
        "class": "Museum",
        "xp": 63.0,
        "xk": 122.0
    },
    {
        "class": "Park",
        "xp": 35.0,
        "xk": 122.0
    },
    {
        "class": "Person",
        "xp": 97.0,
        "xk": 109.0
    },
    {
        "class": "River",
        "xp": 76.0,
        "xk": 122.0
    },
    {
        "class": "Road",
        "xp": 59.0,
        "xk": 109.0
    },
    {
        "class": "Rocks",
        "xp": 86.0,
        "xk": 110.0
    },
    {
        "class": "Windows",
        "xp": 82.0,
        "xk": 110.0
    },
    {
        "class": "Building",
        "xp": 89.0,
        "xk": 107.0
    },
    {
        "class": "Church",
        "xp": 78.0,
        "xk": 122.0
    },
    {
        "class": "City",
        "xp": 91.0,
        "xk": 109.0
    },
    {
        "class": "Cultural institution",
        "xp": 90.0,
        "xk": 122.0
    },
    {
        "class": "Footpath",
        "xp": 91.0,
        "xk": 122.0
    },
    {
        "class": "Forest",
        "xp": 84.0,
        "xk": 122.0
    },
    {
        "class": "Graveyard",
        "xp": 103.0,
        "xk": 106.0
    },
    {
        "class": "Mine",
        "xp": 39.0,
        "xk": 122.0
    },
    {
        "class": "Monument",
        "xp": 58.0,
        "xk": 122.0
    },
    {
        "class": "Motor vehicle",
        "xp": 59.0,
        "xk": 120.0
    },
    {
        "class": "Museum",
        "xp": 63.0,
        "xk": 122.0
    },
    {
        "class": "Park",
        "xp": 35.0,
        "xk": 122.0
    },
    {
        "class": "Person",
        "xp": 97.0,
        "xk": 109.0
    },
    {
        "class": "River",
        "xp": 76.0,
        "xk": 122.0
    },
    {
        "class": "Road",
        "xp": 59.0,
        "xk": 109.0
    },
    {
        "class": "Rocks",
        "xp": 86.0,
        "xk": 110.0
    },
    {
        "class": "Windows",
        "xp": 82.0,
        "xk": 110.0
    },
    {
        "class": "Building",
        "xp": 89.0,
        "xk": 107.0
    },
    {
        "class": "Church",
        "xp": 78.0,
        "xk": 122.0
    },
    {
        "class": "City",
        "xp": 91.0,
        "xk": 109.0
    },
    {
        "class": "Cultural institution",
        "xp": 90.0,
        "xk": 122.0
    },
    {
        "class": "Footpath",
        "xp": 91.0,
        "xk": 122.0
    },
    {
        "class": "Forest",
        "xp": 84.0,
        "xk": 122.0
    },
    {
        "class": "Mine",
        "xp": 39.0,
        "xk": 122.0
    },
    {
        "class": "Monument",
        "xp": 58.0,
        "xk": 122.0
    },
    {
        "class": "Motor vehicle",
        "xp": 59.0,
        "xk": 120.0
    },
    {
        "class": "Museum",
        "xp": 63.0,
        "xk": 122.0
    },
    {
        "class": "Park",
        "xp": 35.0,
        "xk": 122.0
    },
    {
        "class": "Person",
        "xp": 97.0,
        "xk": 109.0
    },
    {
        "class": "River",
        "xp": 76.0,
        "xk": 122.0
    },
    {
        "class": "Road",
        "xp": 59.0,
        "xk": 109.0
    },
    {
        "class": "Rocks",
        "xp": 86.0,
        "xk": 110.0
    },
    {
        "class": "Windows",
        "xp": 82.0,
        "xk": 110.0
    },
    {
        "class": "Church",
        "xp": 78.0,
        "xk": 122.0
    },
    {
        "class": "City",
        "xp": 91.0,
        "xk": 109.0
    },
    {
        "class": "Cultural institution",
        "xp": 90.0,
        "xk": 122.0
    },
    {
        "class": "Footpath",
        "xp": 91.0,
        "xk": 122.0
    },
    {
        "class": "Forest",
        "xp": 84.0,
        "xk": 122.0
    },
    {
        "class": "Mine",
        "xp": 39.0,
        "xk": 122.0
    },
    {
        "class": "Monument",
        "xp": 58.0,
        "xk": 122.0
    },
    {
        "class": "Motor vehicle",
        "xp": 59.0,
        "xk": 120.0
    },
    {
        "class": "Museum",
        "xp": 63.0,
        "xk": 122.0
    },
    {
        "class": "Park",
        "xp": 35.0,
        "xk": 122.0
    },
    {
        "class": "Person",
        "xp": 97.0,
        "xk": 109.0
    },
    {
        "class": "River",
        "xp": 76.0,
        "xk": 122.0
    },
    {
        "class": "Road",
        "xp": 59.0,
        "xk": 109.0
    },
    {
        "class": "Rocks",
        "xp": 86.0,
        "xk": 110.0
    },
    {
        "class": "Windows",
        "xp": 82.0,
        "xk": 110.0
    },
    {
        "class": "Church",
        "xp": 78.0,
        "xk": 122.0
    },
    {
        "class": "City",
        "xp": 91.0,
        "xk": 109.0
    },
    {
        "class": "Cultural institution",
        "xp": 90.0,
        "xk": 122.0
    },
    {
        "class": "Footpath",
        "xp": 91.0,
        "xk": 122.0
    },
    {
        "class": "Forest",
        "xp": 84.0,
        "xk": 122.0
    },
    {
        "class": "Mine",
        "xp": 39.0,
        "xk": 122.0
    },
    {
        "class": "Monument",
        "xp": 58.0,
        "xk": 122.0
    },
    {
        "class": "Motor vehicle",
        "xp": 59.0,
        "xk": 120.0
    },
    {
        "class": "Museum",
        "xp": 63.0,
        "xk": 122.0
    },
    {
        "class": "Park",
        "xp": 35.0,
        "xk": 122.0
    },
    {
        "class": "Person",
        "xp": 97.0,
        "xk": 109.0
    },
    {
        "class": "River",
        "xp": 76.0,
        "xk": 122.0
    },
    {
        "class": "Road",
        "xp": 59.0,
        "xk": 109.0
    },
    {
        "class": "Rocks",
        "xp": 86.0,
        "xk": 110.0
    },
    {
        "class": "Windows",
        "xp": 82.0,
        "xk": 110.0
    },
    {
        "class": "Church",
        "xp": 78.0,
        "xk": 122.0
    },
    {
        "class": "Cross",
        "xp": 92.0,
        "xk": 122.0
    },
    {
        "class": "Cultural institution",
        "xp": 90.0,
        "xk": 122.0
    },
    {
        "class": "Footpath",
        "xp": 91.0,
        "xk": 122.0
    },
    {
        "class": "Forest",
        "xp": 84.0,
        "xk": 122.0
    },
    {
        "class": "Grass",
        "xp": 73.0,
        "xk": 122.0
    },
    {
        "class": "Landscape",
        "xp": 98.0,
        "xk": 112.0
    },
    {
        "class": "Mine",
        "xp": 39.0,
        "xk": 122.0
    },
    {
        "class": "Monument",
        "xp": 58.0,
        "xk": 122.0
    },
    {
        "class": "Motor vehicle",
        "xp": 59.0,
        "xk": 120.0
    },
    {
        "class": "Museum",
        "xp": 63.0,
        "xk": 122.0
    },
    {
        "class": "Park",
        "xp": 35.0,
        "xk": 122.0
    },
    {
        "class": "River",
        "xp": 76.0,
        "xk": 122.0
    },
    {
        "class": "Rocks",
        "xp": 86.0,
        "xk": 110.0
    },
    {
        "class": "Windows",
        "xp": 82.0,
        "xk": 110.0
    },
    {
        "class": "Church",
        "xp": 78.0,
        "xk": 122.0
    },
    {
        "class": "Cross",
        "xp": 92.0,
        "xk": 122.0
    },
    {
        "class": "Cultural institution",
        "xp": 90.0,
        "xk": 122.0
    },
    {
        "class": "Footpath",
        "xp": 91.0,
        "xk": 122.0
    },
    {
        "class": "Forest",
        "xp": 84.0,
        "xk": 122.0
    },
    {
        "class": "Grass",
        "xp": 73.0,
        "xk": 122.0
    },
    {
        "class": "Landscape",
        "xp": 98.0,
        "xk": 112.0
    },
    {
        "class": "Mine",
        "xp": 39.0,
        "xk": 122.0
    },
    {
        "class": "Monument",
        "xp": 58.0,
        "xk": 122.0
    },
    {
        "class": "Motor vehicle",
        "xp": 59.0,
        "xk": 120.0
    },
    {
        "class": "Museum",
        "xp": 63.0,
        "xk": 122.0
    },
    {
        "class": "Park",
        "xp": 35.0,
        "xk": 122.0
    },
    {
        "class": "River",
        "xp": 76.0,
        "xk": 122.0
    },
    {
        "class": "Church",
        "xp": 78.0,
        "xk": 122.0
    },
    {
        "class": "Cross",
        "xp": 92.0,
        "xk": 122.0
    },
    {
        "class": "Cultural institution",
        "xp": 90.0,
        "xk": 122.0
    },
    {
        "class": "Footpath",
        "xp": 91.0,
        "xk": 122.0
    },
    {
        "class": "Forest",
        "xp": 84.0,
        "xk": 122.0
    },
    {
        "class": "Grass",
        "xp": 73.0,
        "xk": 122.0
    },
    {
        "class": "Graveyard",
        "xp": 108.0,
        "xk": 122.0
    },
    {
        "class": "Landscape",
        "xp": 98.0,
        "xk": 112.0
    },
    {
        "class": "Mine",
        "xp": 39.0,
        "xk": 122.0
    },
    {
        "class": "Monument",
        "xp": 58.0,
        "xk": 122.0
    },
    {
        "class": "Motor vehicle",
        "xp": 59.0,
        "xk": 120.0
    },
    {
        "class": "Museum",
        "xp": 63.0,
        "xk": 122.0
    },
    {
        "class": "Park",
        "xp": 35.0,
        "xk": 122.0
    },
    {
        "class": "River",
        "xp": 76.0,
        "xk": 122.0
    },
    {
        "class": "Trees",
        "xp": 74.0,
        "xk": 122.0
    },
    {
        "class": "Church",
        "xp": 78.0,
        "xk": 122.0
    },
    {
        "class": "Cross",
        "xp": 92.0,
        "xk": 122.0
    },
    {
        "class": "Cultural institution",
        "xp": 90.0,
        "xk": 122.0
    },
    {
        "class": "Footpath",
        "xp": 91.0,
        "xk": 122.0
    },
    {
        "class": "Forest",
        "xp": 84.0,
        "xk": 122.0
    },
    {
        "class": "Grass",
        "xp": 73.0,
        "xk": 122.0
    },
    {
        "class": "Graveyard",
        "xp": 108.0,
        "xk": 122.0
    },
    {
        "class": "Mine",
        "xp": 39.0,
        "xk": 122.0
    },
    {
        "class": "Monument",
        "xp": 58.0,
        "xk": 122.0
    },
    {
        "class": "Motor vehicle",
        "xp": 59.0,
        "xk": 120.0
    },
    {
        "class": "Museum",
        "xp": 63.0,
        "xk": 122.0
    },
    {
        "class": "Park",
        "xp": 35.0,
        "xk": 122.0
    },
    {
        "class": "River",
        "xp": 76.0,
        "xk": 122.0
    },
    {
        "class": "Trees",
        "xp": 74.0,
        "xk": 122.0
    },
    {
        "class": "Church",
        "xp": 78.0,
        "xk": 122.0
    },
    {
        "class": "Cross",
        "xp": 92.0,
        "xk": 122.0
    },
    {
        "class": "Cultural institution",
        "xp": 90.0,
        "xk": 122.0
    },
    {
        "class": "Footpath",
        "xp": 91.0,
        "xk": 122.0
    },
    {
        "class": "Forest",
        "xp": 84.0,
        "xk": 122.0
    },
    {
        "class": "Grass",
        "xp": 73.0,
        "xk": 122.0
    },
    {
        "class": "Graveyard",
        "xp": 108.0,
        "xk": 122.0
    },
    {
        "class": "Mine",
        "xp": 39.0,
        "xk": 122.0
    },
    {
        "class": "Monument",
        "xp": 58.0,
        "xk": 122.0
    },
    {
        "class": "Motor vehicle",
        "xp": 59.0,
        "xk": 120.0
    },
    {
        "class": "Museum",
        "xp": 63.0,
        "xk": 122.0
    },
    {
        "class": "Park",
        "xp": 35.0,
        "xk": 122.0
    },
    {
        "class": "River",
        "xp": 76.0,
        "xk": 122.0
    },
    {
        "class": "Trees",
        "xp": 74.0,
        "xk": 122.0
    },
    {
        "class": "Church",
        "xp": 78.0,
        "xk": 122.0
    },
    {
        "class": "Cross",
        "xp": 92.0,
        "xk": 122.0
    },
    {
        "class": "Cultural institution",
        "xp": 90.0,
        "xk": 122.0
    },
    {
        "class": "Footpath",
        "xp": 91.0,
        "xk": 122.0
    },
    {
        "class": "Forest",
        "xp": 84.0,
        "xk": 122.0
    },
    {
        "class": "Grass",
        "xp": 73.0,
        "xk": 122.0
    },
    {
        "class": "Graveyard",
        "xp": 108.0,
        "xk": 122.0
    },
    {
        "class": "Mine",
        "xp": 39.0,
        "xk": 122.0
    },
    {
        "class": "Monument",
        "xp": 58.0,
        "xk": 122.0
    },
    {
        "class": "Motor vehicle",
        "xp": 59.0,
        "xk": 120.0
    },
    {
        "class": "Mountains",
        "xp": 112.0,
        "xk": 117.0
    },
    {
        "class": "Museum",
        "xp": 63.0,
        "xk": 122.0
    },
    {
        "class": "Park",
        "xp": 35.0,
        "xk": 122.0
    },
    {
        "class": "River",
        "xp": 76.0,
        "xk": 122.0
    },
    {
        "class": "Rocks",
        "xp": 112.0,
        "xk": 117.0
    },
    {
        "class": "Snow",
        "xp": 111.0,
        "xk": 115.0
    },
    {
        "class": "Stairs",
        "xp": 111.0,
        "xk": 117.0
    },
    {
        "class": "Trees",
        "xp": 74.0,
        "xk": 122.0
    },
    {
        "class": "Church",
        "xp": 78.0,
        "xk": 122.0
    },
    {
        "class": "Cross",
        "xp": 92.0,
        "xk": 122.0
    },
    {
        "class": "Cultural institution",
        "xp": 90.0,
        "xk": 122.0
    },
    {
        "class": "Footpath",
        "xp": 91.0,
        "xk": 122.0
    },
    {
        "class": "Forest",
        "xp": 84.0,
        "xk": 122.0
    },
    {
        "class": "Grass",
        "xp": 73.0,
        "xk": 122.0
    },
    {
        "class": "Graveyard",
        "xp": 108.0,
        "xk": 122.0
    },
    {
        "class": "Mine",
        "xp": 39.0,
        "xk": 122.0
    },
    {
        "class": "Monument",
        "xp": 58.0,
        "xk": 122.0
    },
    {
        "class": "Motor vehicle",
        "xp": 59.0,
        "xk": 120.0
    },
    {
        "class": "Mountains",
        "xp": 112.0,
        "xk": 117.0
    },
    {
        "class": "Museum",
        "xp": 63.0,
        "xk": 122.0
    },
    {
        "class": "Park",
        "xp": 35.0,
        "xk": 122.0
    },
    {
        "class": "River",
        "xp": 76.0,
        "xk": 122.0
    },
    {
        "class": "Rocks",
        "xp": 112.0,
        "xk": 117.0
    },
    {
        "class": "Stairs",
        "xp": 111.0,
        "xk": 117.0
    },
    {
        "class": "Trees",
        "xp": 74.0,
        "xk": 122.0
    },
    {
        "class": "Church",
        "xp": 78.0,
        "xk": 122.0
    },
    {
        "class": "City",
        "xp": 111.0,
        "xk": 117.0
    },
    {
        "class": "Cross",
        "xp": 92.0,
        "xk": 122.0
    },
    {
        "class": "Cultural institution",
        "xp": 90.0,
        "xk": 122.0
    },
    {
        "class": "Footpath",
        "xp": 91.0,
        "xk": 122.0
    },
    {
        "class": "Forest",
        "xp": 84.0,
        "xk": 122.0
    },
    {
        "class": "Grass",
        "xp": 73.0,
        "xk": 122.0
    },
    {
        "class": "Graveyard",
        "xp": 108.0,
        "xk": 122.0
    },
    {
        "class": "Landscape",
        "xp": 114.0,
        "xk": 122.0
    },
    {
        "class": "Mine",
        "xp": 39.0,
        "xk": 122.0
    },
    {
        "class": "Monument",
        "xp": 58.0,
        "xk": 122.0
    },
    {
        "class": "Motor vehicle",
        "xp": 59.0,
        "xk": 120.0
    },
    {
        "class": "Mountains",
        "xp": 112.0,
        "xk": 117.0
    },
    {
        "class": "Museum",
        "xp": 63.0,
        "xk": 122.0
    },
    {
        "class": "Park",
        "xp": 35.0,
        "xk": 122.0
    },
    {
        "class": "River",
        "xp": 76.0,
        "xk": 122.0
    },
    {
        "class": "Rocks",
        "xp": 112.0,
        "xk": 117.0
    },
    {
        "class": "Sport",
        "xp": 114.0,
        "xk": 120.0
    },
    {
        "class": "Stairs",
        "xp": 111.0,
        "xk": 117.0
    },
    {
        "class": "Trees",
        "xp": 74.0,
        "xk": 122.0
    },
    {
        "class": "Church",
        "xp": 78.0,
        "xk": 122.0
    },
    {
        "class": "Cross",
        "xp": 92.0,
        "xk": 122.0
    },
    {
        "class": "Cultural institution",
        "xp": 90.0,
        "xk": 122.0
    },
    {
        "class": "Footpath",
        "xp": 91.0,
        "xk": 122.0
    },
    {
        "class": "Forest",
        "xp": 84.0,
        "xk": 122.0
    },
    {
        "class": "Grass",
        "xp": 73.0,
        "xk": 122.0
    },
    {
        "class": "Graveyard",
        "xp": 108.0,
        "xk": 122.0
    },
    {
        "class": "Landscape",
        "xp": 114.0,
        "xk": 122.0
    },
    {
        "class": "Mine",
        "xp": 39.0,
        "xk": 122.0
    },
    {
        "class": "Monument",
        "xp": 58.0,
        "xk": 122.0
    },
    {
        "class": "Motor vehicle",
        "xp": 59.0,
        "xk": 120.0
    },
    {
        "class": "Museum",
        "xp": 63.0,
        "xk": 122.0
    },
    {
        "class": "Park",
        "xp": 35.0,
        "xk": 122.0
    },
    {
        "class": "River",
        "xp": 76.0,
        "xk": 122.0
    },
    {
        "class": "Sport",
        "xp": 114.0,
        "xk": 120.0
    },
    {
        "class": "Trees",
        "xp": 74.0,
        "xk": 122.0
    },
    {
        "class": "Church",
        "xp": 78.0,
        "xk": 122.0
    },
    {
        "class": "Cross",
        "xp": 92.0,
        "xk": 122.0
    },
    {
        "class": "Cultural institution",
        "xp": 90.0,
        "xk": 122.0
    },
    {
        "class": "Footpath",
        "xp": 91.0,
        "xk": 122.0
    },
    {
        "class": "Forest",
        "xp": 84.0,
        "xk": 122.0
    },
    {
        "class": "Grass",
        "xp": 73.0,
        "xk": 122.0
    },
    {
        "class": "Graveyard",
        "xp": 108.0,
        "xk": 122.0
    },
    {
        "class": "Landscape",
        "xp": 114.0,
        "xk": 122.0
    },
    {
        "class": "Mine",
        "xp": 39.0,
        "xk": 122.0
    },
    {
        "class": "Monument",
        "xp": 58.0,
        "xk": 122.0
    },
    {
        "class": "Motor vehicle",
        "xp": 59.0,
        "xk": 120.0
    },
    {
        "class": "Museum",
        "xp": 63.0,
        "xk": 122.0
    },
    {
        "class": "Park",
        "xp": 35.0,
        "xk": 122.0
    },
    {
        "class": "River",
        "xp": 76.0,
        "xk": 122.0
    },
    {
        "class": "Sport",
        "xp": 114.0,
        "xk": 120.0
    },
    {
        "class": "Trees",
        "xp": 74.0,
        "xk": 122.0
    },
    {
        "class": "Church",
        "xp": 78.0,
        "xk": 122.0
    },
    {
        "class": "Cross",
        "xp": 92.0,
        "xk": 122.0
    },
    {
        "class": "Cultural institution",
        "xp": 90.0,
        "xk": 122.0
    },
    {
        "class": "Footpath",
        "xp": 91.0,
        "xk": 122.0
    },
    {
        "class": "Forest",
        "xp": 84.0,
        "xk": 122.0
    },
    {
        "class": "Grass",
        "xp": 73.0,
        "xk": 122.0
    },
    {
        "class": "Graveyard",
        "xp": 108.0,
        "xk": 122.0
    },
    {
        "class": "Landscape",
        "xp": 114.0,
        "xk": 122.0
    },
    {
        "class": "Mine",
        "xp": 39.0,
        "xk": 122.0
    },
    {
        "class": "Monument",
        "xp": 58.0,
        "xk": 122.0
    },
    {
        "class": "Motor vehicle",
        "xp": 59.0,
        "xk": 120.0
    },
    {
        "class": "Museum",
        "xp": 63.0,
        "xk": 122.0
    },
    {
        "class": "Park",
        "xp": 35.0,
        "xk": 122.0
    },
    {
        "class": "River",
        "xp": 76.0,
        "xk": 122.0
    },
    {
        "class": "Sport",
        "xp": 114.0,
        "xk": 120.0
    },
    {
        "class": "Trees",
        "xp": 74.0,
        "xk": 122.0
    },
    {
        "class": "Church",
        "xp": 78.0,
        "xk": 122.0
    },
    {
        "class": "Cross",
        "xp": 92.0,
        "xk": 122.0
    },
    {
        "class": "Cultural institution",
        "xp": 90.0,
        "xk": 122.0
    },
    {
        "class": "Footpath",
        "xp": 91.0,
        "xk": 122.0
    },
    {
        "class": "Forest",
        "xp": 84.0,
        "xk": 122.0
    },
    {
        "class": "Grass",
        "xp": 73.0,
        "xk": 122.0
    },
    {
        "class": "Graveyard",
        "xp": 108.0,
        "xk": 122.0
    },
    {
        "class": "Landscape",
        "xp": 114.0,
        "xk": 122.0
    },
    {
        "class": "Mine",
        "xp": 39.0,
        "xk": 122.0
    },
    {
        "class": "Monument",
        "xp": 58.0,
        "xk": 122.0
    },
    {
        "class": "Museum",
        "xp": 63.0,
        "xk": 122.0
    },
    {
        "class": "Park",
        "xp": 35.0,
        "xk": 122.0
    },
    {
        "class": "River",
        "xp": 76.0,
        "xk": 122.0
    },
    {
        "class": "Trees",
        "xp": 74.0,
        "xk": 122.0
    },
    {
        "class": "Church",
        "xp": 78.0,
        "xk": 122.0
    },
    {
        "class": "Cross",
        "xp": 92.0,
        "xk": 122.0
    },
    {
        "class": "Cultural institution",
        "xp": 90.0,
        "xk": 122.0
    },
    {
        "class": "Footpath",
        "xp": 91.0,
        "xk": 122.0
    },
    {
        "class": "Forest",
        "xp": 84.0,
        "xk": 122.0
    },
    {
        "class": "Grass",
        "xp": 73.0,
        "xk": 122.0
    },
    {
        "class": "Graveyard",
        "xp": 108.0,
        "xk": 122.0
    },
    {
        "class": "Landscape",
        "xp": 114.0,
        "xk": 122.0
    },
    {
        "class": "Mine",
        "xp": 39.0,
        "xk": 122.0
    },
    {
        "class": "Monument",
        "xp": 58.0,
        "xk": 122.0
    },
    {
        "class": "Museum",
        "xp": 63.0,
        "xk": 122.0
    },
    {
        "class": "Park",
        "xp": 35.0,
        "xk": 122.0
    },
    {
        "class": "River",
        "xp": 76.0,
        "xk": 122.0
    },
    {
        "class": "Trees",
        "xp": 74.0,
        "xk": 122.0
    }
])

chart=alt.Chart(source).mark_bar(height=10, color="rgb(200,100,0)").encode(
    alt.X('xp', title=''),
    alt.X2('xk',title=''),
    alt.Y('class',title='')
).configure(
    background="#202020",    
).configure_axis(
    labelColor="#ffffff"
)
chart.save('chart.html')
