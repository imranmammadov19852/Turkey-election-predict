import pandas as pd

df2024 = pd.read_csv("election2024.csv")

akp_data = df2024['AKP(%)']
chp_data = df2024['CHP(%)']
dem_data = df2024['DEM(%)']
mhp_data = df2024['MHP(%)']
yrp_data = df2024['YRP(%)']
iyip_data = df2024['IYIP(%)']
zafer_data = df2024['ZAFER(%)']

party_counts = {
    'AKP': 0,
    'CHP': 0,
    'DEM': 0,
    'MHP': 0,
    'YRP': 0,
    'IYIP': 0,
    'ZAFER': 0
}


for province, akp_percentage, chp_percentage, dem_percentage, mhp_percentage, yrp_percentage, iyip_percentage, zafer_percentage in zip(df2024['Province'], akp_data, chp_data, dem_data, mhp_data, yrp_data, iyip_data, zafer_data):
    akp_percentage = float(akp_percentage)
    chp_percentage = float(chp_percentage)
    dem_percentage = float(dem_percentage)
    mhp_percentage = float(mhp_percentage)
    yrp_percentage = float(yrp_percentage)
    iyip_percentage = float(iyip_percentage)
    zafer_percentage = float(zafer_percentage)

    max_percentage = max(akp_percentage, chp_percentage, dem_percentage, mhp_percentage, yrp_percentage, iyip_percentage, zafer_percentage)
    
    if max_percentage == akp_percentage:
        party_counts['AKP'] += 1
    elif max_percentage == chp_percentage:
        party_counts['CHP'] += 1
    elif max_percentage == dem_percentage:
        party_counts['DEM'] += 1
    elif max_percentage == mhp_percentage:
        party_counts['MHP'] += 1
    elif max_percentage == yrp_percentage:
        party_counts['YRP'] += 1
    elif max_percentage == iyip_percentage:
        party_counts['IYIP'] += 1
    elif max_percentage == zafer_percentage:
        party_counts['ZAFER'] += 1


for party, count in party_counts.items():
    print(f"{party}: {count} provinces won")