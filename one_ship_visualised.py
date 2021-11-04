from os import path
import pandas as pd
pd.options.display.float_format = '{:.3f}'.format
import geopandas as gpd
import seaborn as sns
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt
path = '/home/luke/Documents/xplatform/github/rendez_vous _course/daat/headingships'
df = pd.read_csv(path)
df.head()


