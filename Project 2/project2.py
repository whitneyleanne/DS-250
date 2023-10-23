#%%
import pandas as pd
import altair as alt
import numpy as np
#%%
url = "https://raw.githubusercontent.com/byuidatascience/data4missing/master/data-raw/flights_missing/flights_missing.json" 
flights = pd.read_json(url)


#%% 
flights.groupby("airport_code").agg(
    total_flights = ('num_of_flights_total', np.sum),
    total_delays = ('num_of_delays_total', np.sum),
    ave_delay_minutes = ('minutes_delayed_total', np.sum)
).assign(
    prop_delays = lambda df: df.total_delays / df.total_flights,
    num_delay = lambda df: df.total_delay_minutes / df.total_delays
)
# %%
flights.month.replace("Febuary", "February", inplace = True),
flights.month.replace("n/a", np.nan, inplace = True)

## df.dropna(how = "all") If all the data is missing, this will delete it
## df.dropna(subset = ["rowname"]) - any missing value in rowname is taken out
## f fill ; forward (top to bottom). b fill ; upward (bottom to top) can use inplace for true

#%% 
(flights.assign(
        severe = flights.num_of_delays_weather, 
        late_aircraft_weather = lambda.df: df.num_of_delays_late_aircraft * 0.3,
        weather_nas_delays = lambda.df: np.where(
            df.month.isin(["April", "May", "June", "July", "August"]),
            df.num_of_delays_nas * 0.4,
            df.num_of_delays_nas * 0.65)          )
)
# %%
# hints for number 3 weather_nas_delays = np.where(), is in method
weather = flights.assign(
    severe = lambda df: df.num_of_delays_weather,
    mild_late = 
    mild_nas = np.where()
    total_weather = 
).filter(['airport_code','month','severe','mild_late','mild_nas',
    'total_weather', 'num_of_delays_total'])


#%%
json_data = flights.to_json(orient="table")
json_object = json.loads(json_data)
json_formatted_str = json.dumps(json_object, indent = 4)
print(json_formatted_str)