import pandas as pd
from datetime import datetime, timedelta

#first reading the Jason.csv File#
df = pd.read_csv("cleaneddata.csv")
#convert the "date into parsable format" File#
df["Service start date"] = pd.to_datetime(df["Service start date"], format='%m/%d/%Y')
df["Service end date"] = pd.to_datetime(df["Service end date"], format='%m/%d/%Y')
start_yeardate = datetime(2021, 1, 1)
end_yeardate = datetime(2021, 12, 31)
today_date = datetime(2021, 12, 30)

start_date_list = df["Service start date"].tolist()

end_date_list = df["Service end date"].tolist()

mealQty_list = df["TOTAL Meal Qty"].tolist()

weekDiff = []
for i in range(len(start_date_list)):
    if end_date_list[i] < start_date_list[i]:
        end_date_list[i] = end_yeardate
    if start_date_list[i] < start_yeardate:
        start_date_list[i] = start_yeardate
    if end_date_list[i] > end_yeardate:
        end_date_list[i] = end_yeardate
    if end_date_list[i] is pd.NaT:
        end_date_list[i] = end_yeardate

for i in range(len(start_date_list)):
    monday1 = (start_date_list[i] - timedelta(days=start_date_list[i].weekday()))
    monday2 = (end_date_list[i] - timedelta(days=end_date_list[i].weekday()))
    weekD = int((monday2 - monday1).days / 7)
    weekDiff.append(weekD)

overall_meals = []
for i in range(len(weekDiff)):
    overall = weekDiff[i] * mealQty_list[i]
    overall_meals.append(overall)

df["Overall Meals"] = overall_meals

df.to_csv("testing1234.csv", index=False)
