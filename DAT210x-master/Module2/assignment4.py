import pandas as pd


# TODO: Load up the table, and extract the dataset
# out of it. If you're having issues with this, look
# carefully at the sample code provided in the reading
#
# .. your code here ..
df = pd.read_html("http://www.espn.com/nhl/statistics/player/_/stat/points/sort/points/year/2015/seasontype/2")[0]


# TODO: Rename the columns so that they are similar to the
# column definitions provided to you on the website.
# Be careful and don't accidentially use any names twice.
#
# .. your code here ..
df = df[2:]
df.columns = ["RK", "PLAYER", "TEAM", "GP", "G", "A", "PTS", "+/-", "PIM", "PTS/G", "SOG", "PCT", "GWG", "PP-G", "PP-A", "SH-G", "SH-A"]


# TODO: Get rid of any row that has at least 4 NANs in it,
# e.g. that do not contain player points statistics
#
# .. your code here ..
df = df.dropna(axis=0, thresh=13)


# TODO: At this point, look through your dataset by printing
# it. There probably still are some erroneous rows in there.
# What indexing command(s) can you use to select all rows
# EXCEPT those rows?
#
# .. your code here ..
df = df[df.RK != "RK"]

# TODO: Get rid of the 'RK' column
#
# .. your code here ..
df.drop(labels = "RK", axis=1, inplace=True)

# TODO: Ensure there are no holes in your index by resetting
# it. By the way, don't store the original index
#
# .. your code here ..
df.reset_index(drop=True, inplace=True)

# TODO: Check the data type of all columns, and ensure those
# that should be numeric are numeric
#
# .. your code here ..
df.GP = pd.to_numeric(df.GP, errors='coerce')
df.G = pd.to_numeric(df.G, errors='coerce')
df.A = pd.to_numeric(df.A, errors='coerce')
df.PTS = pd.to_numeric(df.PTS, errors='coerce')
df["+/-"] = pd.to_numeric(df["+/-"], errors='coerce')
df.PIM = pd.to_numeric(df.PIM, errors='coerce')
df["PTS/G"] = pd.to_numeric(df["PTS/G"], errors='coerce')
df.SOG = pd.to_numeric(df.SOG, errors='coerce')
df.PCT = pd.to_numeric(df.PCT, errors='coerce')
df.GWG = pd.to_numeric(df.GWG, errors='coerce')
df["PP-G"] = pd.to_numeric(df["PP-G"], errors='coerce')
df["PP-A"] = pd.to_numeric(df["PP-A"], errors='coerce')
df["SH-G"] = pd.to_numeric(df["SH-G"], errors='coerce')
df["SH-A"] = pd.to_numeric(df["SH-A"], errors='coerce')

print df.dtypes


# TODO: Your dataframe is now ready! Use the appropriate 
# commands to answer the questions on the course lab page.
#
# .. your code here ..
print df.shape
print len(df.PCT.unique())
print sum(df.GP[15:17])

