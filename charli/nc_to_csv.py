
import xarray as xr
import pandas as pd
import cftime
import numpy as np

#file path to data for practicing! This is a netcdf file of 5 years of precipitation data -much smaller than the full 1200 years of paleon data
file_path = "/raid/cuden/data/test.nc"

def loadEra5Data(file_path, var):
    ds = xr.open_dataset(file_path)

    # Convert to DataFrame and reset index to bring 'time' into columns
    df = ds.to_dataframe().reset_index()
    #store time as a string
    df['time'] = df['time'].astype(str)
    # Extract the first 4 characters (year)
    df['Year'] = df['time'].str[:4]
    # Extract characters at index 5 and 6 (month)  
    df['Month'] = df['time'].str[5:7]  

    # Convert them to integer type (optional)
    df['Year'] = df['Year'].astype(int)
    df['Month'] = df['Month'].astype(int)

    #NA values are over the ocean and great lakes
    df = df.dropna()

    #get summer months
    df = df[df['Month'].between(5, 9)]

    #find average climate value for each lat lon year 
    df = df.groupby(['lat', 'lon', 'Year', 'Month'])[var].mean().reset_index()

    return df



# Load NetCDF file and display first rows
test = loadEra5Data("/raid/cuden/Lightning-Predictions/charli/test.nc",var="precipf")
print(test.columns)
print(test.head())
print(test.dtypes)
print(test.tail())
#print(test['Month'].unique())

print(len(test))
print(test.isna().sum().sum())
missing_per_column = test.isna().sum()
print(missing_per_column)

#test.to_csv('avgmonthly_precip.csv', index=False)
#test.to_csv('daily_precip.csv', index=False)

psurf = loadEra5Data("/epscorfs/data/PalEON/met_regional/phase2_met_regional_v2_daily/concatenated/psurf_0850-2010.nc", var = "psurf")
tair = loadEra5Data("/epscorfs/data/PalEON/met_regional/phase2_met_regional_v2_daily/concatenated/tair_0850-2010.nc", var = "tair")
wind = loadEra5Data("/epscorfs/data/PalEON/met_regional/phase2_met_regional_v2_daily/concatenated/wind_0850-2010.nc", var = "wind")
swr = loadEra5Data("/epscorfs/data/PalEON/met_regional/phase2_met_regional_v2_daily/concatenated/swdown_0850-2010.nc", var = "swdown")
precip = loadEra5Data("/epscorfs/data/PalEON/met_regional/phase2_met_regional_v2_daily/concatenated/precipf_0850-2010.nc", var = "precipf")


# qair: specific humididity measured at the lowest level of the atmosphere (kg kg-1))
# we want relative humidity (%): (e / e_s) x 100

#e: actual vapor 
#e = (SH * P) / (0.622 + SH)

#e_s: Saturation vapor pressure
# e_s = 6.112 * (e^((17.67*T) / (T + 243.5)))

#relative humidity:
#(e / e_s) x 100

def loadEra5Data(file_path, var):
    ds = xr.open_dataset(file_path)

    # Convert to DataFrame and reset index to bring 'time' into columns
    df = ds.to_dataframe().reset_index()
    #store time as a string
    df['time'] = df['time'].astype(str)
    # Extract the first 4 characters (year)
    df['Year'] = df['time'].str[:4]
    # Extract characters at index 5 and 6 (month)  
    df['Month'] = df['time'].str[5:7]  

    # Convert them to integer type (optional)
    df['Year'] = df['Year'].astype(int)
    df['Month'] = df['Month'].astype(int)

    #NA values are over the ocean and great lakes
    df = df.dropna()

    #get summer months
    df = df[df['Month'].between(5, 9)]

    return df


#apply this function to specific humidity (qair), temperature (tair), and pressure (psurf)
psurf = loadEra5Data("/epscorfs/data/PalEON/met_regional/phase2_met_regional_v2_daily/concatenated/psurf_0850-2010.nc", var = "psurf")
tair = loadEra5Data("/epscorfs/data/PalEON/met_regional/phase2_met_regional_v2_daily/concatenated/tair_0850-2010.nc", var = "tair")
qair = loadEra5Data("/epscorfs/data/PalEON/met_regional/phase2_met_regional_v2_daily/concatenated/qair_0850-2010.nc", var = "qair")

#combine dataframes so that there is a column for each climate variable

# apply the above calculations to these three columns so that you have relative humidity - call it rh

#find average relative humidity value for each lat lon year:
df = df.groupby(['lat', 'lon', 'Year', 'Month'])[var].mean().reset_index()

#combine dataframes so that there is lat, lon, year, month, tair, psurf, wind, precipf, swdown, and rh (relative humidity)

#export a cvs file containing lat, lon, year, month, and a column for each climate var


  
