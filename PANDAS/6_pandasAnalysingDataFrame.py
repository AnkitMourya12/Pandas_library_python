# Viewing the data : one of the most used method for a quick overview of the dataframe is the head() method. this method returns the headers and a specified number of rows.
# here we will print the 1st 10 rows in the dataframe.
import pandas as pd
ankit = pd.read_csv('Details.csv')                  #:)
print(ankit.head(10))

# here we will print the last 10 rows in the dataframe.
import pandas as pd
ankit = pd.read_csv('Details.csv')
print(ankit.tail(10))

# what if you want the information about the data in the dataframe: via info()
import pandas as pd
df = pd.read_csv('Details.csv')
print(df.info())