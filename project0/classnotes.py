#%%
import pandas as pd
import altair as alt
import numpy as np
import json

url = "https://github.com/byuidatascience/data4missing/raw/master/data-raw/mtcars_missing/mtcars_missing.json" 
cars = pd.read_json(url)

#%%
cars_new = cars.replace([999, ""], np.nan, inplace=True)

print(cars.to_json)
cars_new = cars.iloc[1]





# making a dataset with only 6 cylinder engines
#%%
cars.query('cyl == 6').filter(["car", "hp"])

#%%
cars.sort_values(by = "hp", ascending = False)
#nat default is ascending.

#%% 
cars.replace([999, "n/a", ''], np.nan, inplace = True)

# %%
#adding a new column to a dataset. can use brackets or a dot cars.wt
cars["power_to_wt"] = cars["hp"] / cars["wt"]

#%% 
cars.assign(
    power_to_wt2 = cars["hp"] / cars.wt,
    silly_column = cars.disp * cars.qsec,
    newest = lambda df: df.power_to_wt2 /df.silly_column
    #new4 = cars.new2 / cars.new3
)

#%%
## Summarizing data. average hp for each cylinder
grouped = cars.groupby("cyl").agg(
    avg_hp = ("hp", np.mean),
    total_wt = ("wt", np.sum)
).reset_index()
# %%
