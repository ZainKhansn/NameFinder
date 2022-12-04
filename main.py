# importing pandas as pd
#Using Replit to clear console
# importing time to halt program for x amount of time
import time
import replit
import pandas as pd

na = input("Enter a name!: ")
replit.clear()
# Creating the Series
df = pd.read_csv("names.csv")
#Opening csv file
names = df.loc[df['name'].str.contains(na, case=False)]
#checking case for names

for name in range(len(names)):
  print(names)
  time.sleep(3)
replit.clear()
#loops through csv file to find name

quit()
#exit



    
