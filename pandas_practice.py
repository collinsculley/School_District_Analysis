# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# A dictionary of high schools and the type of school.
high_school_types = [{"High School": "Griffin", "Type":"District"},
                    {"High School": "Figueroa", "Type": "District"},
                    {"High School": "Wilson", "Type": "Charter"},
                    {"High School": "Wright", "Type": "Charter"}]

for schoolType in high_school_types:
    print(schoolType)


# %%
# List of high schools
high_schools = ["Huang High School","Figueroa High School","Shelton High School","Hernandez High School","Griffin High School","Wilson High School","Cabrera High School","Bailey High School","Holden High School","Pena High School","Wright High School","Rodriguez High School","Johnson High School","Ford High School","Thomas High School"]


# %%
# add Pandas dependency
import pandas as pd


# %%
# create a Pandas Series from a list
school_series = pd.Series(high_schools)
school_series


# %%
