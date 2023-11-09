#%%
import pandas as pd
import altair as alt

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics

# %%
# Load data
dwellings_ml = pd.read_csv("https://github.com/byuidatascience/data4dwellings/raw/master/data-raw/dwellings_ml/dwellings_ml.csv")

#%%
# Separate the features (X) and targets (Y)
x = dwellings_ml.filter(["livearea","basement","stories","numbaths", 'netprice', 'condition_AVG', 'gartype_ATT/DET'])
y = dwellings_ml[["before1980"]]

#%% Split the data into train and test sets
x_train, x_test, y_train, y_test = train_test_split(x, y)

# Create a decision tree
classifier_DT = DecisionTreeClassifier(max_depth = 29)

# Fit the decision tree
classifier_DT.fit(x_train, y_train)

# Test the decision tree (make predictions)
y_predicted_DT = classifier_DT.predict(x_test)

# Evaluate the decision tree
print("Accuracy:", metrics.accuracy_score(y_test, y_predicted_DT))
# %%
#%%
from sklearn import tree
import matplotlib

#%% 
# method 1 - text
print(tree.export_text(classifier_DT))

#%% 
# method 2 - graph
tree.plot_tree(classifier_DT, feature_names=list(x.columns), filled=True)
# %%
# Feature importance
classifier_DT.feature_importances_

#%%
feature_df = pd.DataFrame({'features':x.columns, 'importance':classifier_DT.feature_importances_})
feature_df

alt.chart(data = feature_df).mark_bar().encode(
    y = alt.Y("features", sort = "-x"),
    x = alt.X("importance")
)
# %%
