# importing pandas library
import pandas as pd
# importing matplotlib library
import matplotlib.pyplot as plt
filename1 = 'website\static\graph.xlsx' 

df= pd.DataFrame(pd.read_excel(filename1, header=None))

print(df)
df.plot()


# plotting a pie chart
plt.pie(df["Price"], labels=df["Object"])
plt.show()