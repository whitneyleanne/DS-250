#%%
from types import GeneratorType
import pandas as pd
import altair as alt
import numpy as np
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics

#%%
denver = pd.read_csv("https://raw.githubusercontent.com/byuidatascience/data4dwellings/master/data-raw/dwellings_denver/dwellings_denver.csv")
ml_dat = pd.read_csv("https://raw.githubusercontent.com/byuidatascience/data4dwellings/master/data-raw/dwellings_ml/dwellings_ml.csv")

alt.data_transformers.disable_max_rows()
pd.set_option("display.max_columns", None)
#%%
ml_dat.before1980 = ml_dat.before1980.astype('str')
Chart = alt.Chart(ml_dat).mark_boxplot().encode(
    y= alt.Y('yrbuilt').axis(title = "Year",format="d").scale(domainMin= 1870),
    x= "numbaths",
)
Chart
# %%
## this creates a lot of different plots with different features
denver["before1980"] = denver.yrbuilt < 1980
denver.columns

selected = denver.filter(["before1980", 'livearea', 'finbsmnt', 'basement', 'stories', 'nocars', 'sprice', 'yrbuilt']).sample(n=500)

sns.pairplot(selected, hue="before1980")

# %%
h_subset = ml_dat.filter(['livearea', 'finbsmnt', 
    'basement', 'yearbuilt', 'nocars', 'numbdrm', 'numbaths', 
    'stories', 'yrbuilt', 'before1980']).sample(500)

sns.pairplot(h_subset, hue = 'before1980')

corr = h_subset.drop(columns = 'before1980').corr()
# %%
sns.heatmap(corr)

# %%
x = ml_dat.filter(['arcstyle_END UNIT',
       'arcstyle_MIDDLE UNIT', 'arcstyle_ONE AND HALF-STORY',
       'arcstyle_ONE-STORY', 'arcstyle_SPLIT LEVEL', 'arcstyle_THREE-STORY',
       'arcstyle_TRI-LEVEL', 'arcstyle_TRI-LEVEL WITH BASEMENT',
       'arcstyle_TWO AND HALF-STORY', 'arcstyle_TWO-STORY', 'livearea', 'finbsmnt', 'basement'])

y = ml_dat.before1980
# %%
## set a training and testing dataset
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size= .2, random_state= 666)

## create the model
classifer = DecisionTreeClassifier()

## train the model
classifer.fit(x_train, y_train)

## make predictions
y_predictions = classifer.predict(x_test)

## test accuracy of predictions
metrics.accuracy_score(y_test, y_predictions)
# %%


