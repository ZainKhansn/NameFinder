# importing pandas as pd
import time
import replit
import pandas as pd
 
# importing re for regular expressions
na = input("Enter a name!: ")
replit.clear()
# Creating the Series
df = pd.read_csv("names.csv")
names = df.loc[df['name'].str.contains(na, case=False)]

i = 0
for name in range(len(names)):
  print(names)
  time.sleep(3)
replit.clear()

quit()



    