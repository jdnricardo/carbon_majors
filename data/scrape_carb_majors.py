import requests
from bs4 import BeautifulSoup
import polars as pl

med_granularity = pl.read_csv("https://carbonmajors.org/evoke/391/get_cm_file?type=Basic&file=emissions_medium_granularity.csv")

med_granularity.write_parquet("./data/emissions_medium_granularity.parquet")