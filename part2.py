import pandas as pd


df1 = pd.read_csv("madrid.csv", sep=",", header= 0)
dfmadrid = (df1["Mean TemperatureC"])
print(dfmadrid)
df2 = pd.read_csv("brazil.csv", sep = ",", header = 0)
dfbrazil = (df2["temp"])
print(dfbrazil)
#until this point I have complated Question3.

df1.rename(columns = {"CET": "date"},inplace = True) # I made it to merge data
m_madrid=df1[["Mean TemperatureC","date"]] # selecting interesting columns
m_brazil=df2.groupby(["date"])["temp"].mean() # also selecting interesting columns

finalframe=pd.merge(m_madrid, m_brazil, on='date')# thanks to merge function, I can select and use intercept of both date

result= df1['Mean TemperatureC'].corr(df2['temp'])# calculate the correlation between these columns. (inşallah)
print("correlation is :", result)
# I couldn't apply any funtion but promise I will learn :(
#BONUS PART YAAYY
#If  result of the correlation is negative we can say that there is a negative relation between  datas.
#If the result of the correlation is positive we can say that there is a positive relationship between data.
#However, I think that  there cannot be any relationship because They are different cities and they cannot affect each other.