from sklearn.linear_model import LinearRegression
import pandas as pd
import csv

df2024 = pd.read_csv("election2024.csv")
akp_data2024 = df2024['AKP(%)']
chp_data2024 = df2024['CHP(%)']
dem_data2024 = df2024['DEM(%)']
mhp_data2024 = df2024['MHP(%)']
yrp_data2024 = df2024['YRP(%)']
iyip_data2024 = df2024['IYIP(%)']
zafer_data2024 = df2024['ZAFER(%)']

cities_in_akp2024 = []
for x, y in zip(df2024['Province'], akp_data2024):
        cities_in_akp2024.append((x, y))

cities_in_chp2024 = []
for x, y in zip(df2024['Province'], chp_data2024):
        cities_in_chp2024.append((x, y))

cities_in_dem2024 = []
for x, y in zip(df2024['Province'], dem_data2024):
        cities_in_dem2024.append((x, y))

cities_in_mhp2024 = []
for x, y in zip(df2024['Province'], mhp_data2024):
        cities_in_mhp2024.append((x, y))

cities_in_yrp2024= []
for x, y in zip(df2024['Province'], yrp_data2024):
        cities_in_yrp2024.append((x, y))
        
cities_in_iyip2024 = []
for x, y in zip(df2024['Province'], iyip_data2024):
        cities_in_iyip2024.append((x, y))

cities_in_zafer2024 = []
for x, y in zip(df2024['Province'], zafer_data2024):
        cities_in_zafer2024.append((x, y))




df2019 = pd.read_csv("election2019.csv")
akp_data2019 = df2019['AKP(%)']
chp_data2019 = df2019['CHP(%)']
dem_data2019 = df2019['DEM(%)']
mhp_data2019 = df2019['MHP(%)']
yrp_data2019 = df2019['YRP(%)']
iyip_data2019 = df2019['IYIP(%)']
zafer_data2019 = df2019['ZAFER(%)']

cities_in_akp2019 = []
for x, y in zip(df2019['Province'], akp_data2019):
        cities_in_akp2019.append((x, y))

cities_in_chp2019 = []
for x, y in zip(df2019['Province'], chp_data2019):
        cities_in_chp2019.append((x, y))

cities_in_dem2019 = []
for x, y in zip(df2019['Province'], dem_data2019):
        cities_in_dem2019.append((x, y))

cities_in_mhp2019 = []
for x, y in zip(df2019['Province'], mhp_data2019):
        cities_in_mhp2019.append((x, y))

cities_in_yrp2019 = []
for x, y in zip(df2019['Province'], yrp_data2019):
        cities_in_yrp2019.append((x, y))

cities_in_iyip2019 = []
for x, y in zip(df2019['Province'], iyip_data2019):
        cities_in_iyip2019.append((x, y))

cities_in_zafer2019 = []
for x, y in zip(df2019['Province'], zafer_data2019):
        cities_in_zafer2019.append((x, y))



df2014 = pd.read_csv("election2014.csv")
akp_data2014 = df2014['AKP(%)']
chp_data2014 = df2014['CHP(%)']
dem_data2014 = df2014['DEM(%)']
mhp_data2014 = df2014['MHP(%)']
yrp_data2014 = df2014['YRP(%)']
iyip_data2014 = df2014['IYIP(%)']
zafer_data2014 = df2014['ZAFER(%)']

cities_in_akp2014 = []
for x, y in zip(df2014['Province'], akp_data2014):
        cities_in_akp2014.append((x, y))

cities_in_chp2014 = []
for x, y in zip(df2014['Province'], chp_data2014):
        cities_in_chp2014.append((x, y))

cities_in_dem2014 = []
for x, y in zip(df2014['Province'], dem_data2014):
        cities_in_dem2014.append((x, y))

cities_in_mhp2014 = []
for x, y in zip(df2014['Province'], mhp_data2014):
        cities_in_mhp2014.append((x, y))

cities_in_yrp2014 = []
for x, y in zip(df2014['Province'], yrp_data2014):
        cities_in_yrp2014.append((x, y))

cities_in_iyip2014 = []
for x, y in zip(df2014['Province'], iyip_data2014):
        cities_in_iyip2014.append((x, y))

cities_in_zafer2014 = []
for x, y in zip(df2014['Province'], zafer_data2014):
        cities_in_zafer2014.append((x, y))



years = [[2014], [2019], [2024]]


ls_AKP = []
ls_CHP = []
ls_DEM = []
ls_MHP = []
ls_YRP = []
ls_IYIP = []
ls_ZAFER = []

for x, y, z in zip(cities_in_akp2014, cities_in_akp2019, cities_in_akp2024):
        ls_AKP.append([x[1], y[1], z[1]])


for x, y, z in zip(cities_in_chp2014, cities_in_chp2019, cities_in_chp2024):
        ls_CHP.append([x[1], y[1], z[1]])


for x, y, z in zip(cities_in_dem2014, cities_in_dem2019, cities_in_dem2024):
        ls_DEM.append([x[1], y[1], z[1]])


for x, y, z in zip(cities_in_mhp2014, cities_in_mhp2019, cities_in_mhp2024):
        ls_MHP.append([x[1], y[1], z[1]])


for x, y, z in zip(cities_in_yrp2014, cities_in_yrp2019, cities_in_yrp2024):
        ls_YRP.append([x[1], y[1], z[1]])


for x, y, z in zip(cities_in_iyip2014, cities_in_iyip2019, cities_in_iyip2024):
        ls_IYIP.append([x[1], y[1], z[1]])


for x, y, z in zip(cities_in_zafer2014, cities_in_zafer2019, cities_in_zafer2024):
        ls_ZAFER.append([x[1], y[1], z[1]])


ls_2029_AKP = []
ls_2029_CHP = []
ls_2029_DEM = []
ls_2029_MHP = []
ls_2029_YRP = []
ls_2029_IYIP = []
ls_2029_ZAFER = []

for i in range(len(ls_AKP)):
        model = LinearRegression()
        model.fit(years, ls_AKP[i])
        year_2029 = [[2029]]
        predicted_y_2029 = model.predict(year_2029)
        ls_2029_AKP.append(round(predicted_y_2029[0], 2))

for i in range(len(ls_CHP)):
        model = LinearRegression()
        model.fit(years, ls_CHP[i])
        year_2029 = [[2029]]
        predicted_y_2029 = model.predict(year_2029)
        ls_2029_CHP.append(round(predicted_y_2029[0], 2))

for i in range(len(ls_DEM)):
        model = LinearRegression()
        model.fit(years, ls_DEM[i])
        year_2029 = [[2029]]
        predicted_y_2029 = model.predict(year_2029)
        ls_2029_DEM.append(round(predicted_y_2029[0], 2))

for i in range(len(ls_MHP)):
        model = LinearRegression()
        model.fit(years, ls_MHP[i])
        year_2029 = [[2029]]
        predicted_y_2029 = model.predict(year_2029)
        ls_2029_MHP.append(round(predicted_y_2029[0], 2))

for i in range(len(ls_YRP)):
        model = LinearRegression()
        model.fit(years, ls_YRP[i])
        year_2029 = [[2029]]
        predicted_y_2029 = model.predict(year_2029)
        ls_2029_YRP.append(round(predicted_y_2029[0], 2))

for i in range(len(ls_IYIP)):
        model = LinearRegression()
        model.fit(years, ls_IYIP[i])
        year_2029 = [[2029]]
        predicted_y_2029 = model.predict(year_2029)
        ls_2029_IYIP.append(round(predicted_y_2029[0], 2))

for i in range(len(ls_ZAFER)):
        model = LinearRegression()
        model.fit(years, ls_ZAFER[i])
        year_2029 = [[2029]]
        predicted_y_2029 = model.predict(year_2029)
        ls_2029_ZAFER.append(round(predicted_y_2029[0], 2))



combined_data = zip(df2024['Province'], ls_2029_AKP, ls_2029_CHP, ls_2029_DEM, ls_2029_MHP, ls_2029_YRP, ls_2029_IYIP, ls_2029_ZAFER)

file_name = "election2029.csv"

with open(file_name, mode='w', newline='') as file:
    writer = csv.writer(file)
    
    writer.writerow(['Province','AKP(%)','CHP(%)','DEM(%)','MHP(%)','YRP(%)','IYIP(%)','ZAFER(%)'])
    
    for row in combined_data:
        writer.writerow(row)

print("Data successfully was written!", file_name)