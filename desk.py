import pandas as dp
import matplotlib.pyplot as table
cd = dp.read_csv('gender_submission.csv')
print(cd)
Total_Pass = cd["Survived"].value_counts()
total = len(cd)
a = Total_Pass[0]
perc = (a / total) * 100
print(f"Percentage of non-survivors is: {perc:.2f}%")
Total_Pass.plot(kind = 'bar',color = ["violet","blue"])
table.xlabel("Survived people")
table.ylabel("Non-Survived people")
table.title("Survived passenger in the flight")
table.xticks(rotation = 0)
table.yticks(rotation = 24)
table.show()