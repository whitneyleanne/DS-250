# %%
import pandas as pd
import altair as alt

url = "https://raw.githubusercontent.com/byuidatascience/data4names/master/data-raw/names_year/names_year.csv"
names = pd.read_csv(url)

# %%
nm1 = ["Whitney", "Alex"]
new_data = (names.query('name in @nm1')
)

# %% 
chart1 = (alt.Chart(data=new_data)
  .encode(
    x = "year",
    y = "total",
    color = "name"
    )
  .mark_circle()
  )

chart1.mark_line()

#%%
chart2 = alt.Chart(data = new_data).encode(
    x = alt.X("year", axis = alt.Axis(title = "Year", format="d")),
    y = alt.Y("total", axis = alt.Axis(title = "Popularity of Name")),
    color = alt.Color('name')
).properties(
    title= {
        "text": ["Title of the Chart"],
        "subtitle": ["Subtitle Text"]
    }
)

chart2.mark_line() + chart2.mark_circle().configure.legend(
    labelColor="Label Name"
)


# %%
