import pandas as pd
a = pd.read_csv("dataset.txt", sep = ";", header = 0)
print(a)

columns = ["Company","Payment"]
print( a.groupby(columns)["Quantity"].sum() )

Company_names = {"Deloite & Touche": {"Cash": 0, "Credit": 0},
            "EY": {"Cash": 0, "Credit": 0},
            "KPMG": {"Cash": 0, "Credit": 0},
            "PWC": {"Cash": 0, "Credit": 0}}

for i in range(len(a)):
    companyName, payment, quantity = a.iloc[i]["Company"], a.iloc[i]["Payment"], a.iloc[i]["Quantity"]
    Company_names[companyName][payment] = quantity  

for key,value in Company_names.items():
    companyName = key
    cashCount = value["Cash"]
    creditCount = value["Credit"]
    print("From {0} {1} people have bought stuff on discount and paid in cash, also assistants got {2} serving of coffee on credit".format(companyName,cashCount,creditCount))