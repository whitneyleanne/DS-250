#%%
import pandas as pd
import sqlite3

con = sqlite3.connect('lahmansbaseballdb.sqlite')


#%%
## 1
byui_salary = pd.read_sql_query("""SELECT DISTINCT s.salary, s.playerID, s.yearID, cp.schoolID
FROM salaries s, CollegePlaying cp
ON cp.playerID = s.playerID
WHERE cp.playerID = s.playerID and schoolID = 'idbyuid'
ORDER BY salary DESC;
""", con)
byui_salary

# %%
## 2a
dfbatting = pd.read_sql_query("""
SELECT playerID, yearID, 1.0*H / AB as batting_average, AB, H
FROM batting
WHERE AB >= 1
ORDER BY batting_average DESC, playerID

""", con)
dfbatting

#%%
## 2b
dfbatting2 = pd.read_sql_query("""
SELECT playerID, yearID, 1.0*H / AB as batting_average, AB, H
FROM batting
WHERE AB >= 10
LIMIT 5
ORDER BY batting_average DESC, playerID

""", con)
dfbatting2

#%%
## 2c
dfbatting3 = pd.read_sql_query("""
SELECT playerID, (1.0 * SUM(H) / SUM(AB)) AS bat_average
FROM batting
GROUP BY playerID
HAVING SUM(AB) >= 100
ORDER BY bat_average DESC, playerID
LIMIT 5
""", con)
dfbatting3

#%%
## 3
## Use cardinals and yankees ?? // salary per win per season