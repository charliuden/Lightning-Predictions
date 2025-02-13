# Lightning-Predictions I am jeb and I am commiting changes
Applying a lightning prediction model to paleoclimate data


PalEON Meteorological Data
August 13 2019
The University of Vermont
Charlotte Uden and Brian Beckage

This readme describes paleo meteorological data compiled by PalEON (Paleo Ecological Observatory Network) in 2015. The data was used to drive a number of vegetation models: 

Rollinson, C. R., Liu, Y., Raiho, A., Moore, D. J. P., McLachlan, J., Bishop, D. A., … Dietze, M. C. (2017). Emergent climate and CO 2 sensitivities of net primary productivity in ecosystem models do not agree with empirical data in temperate forests of eastern North America. Global Change Biology. https://doi.org/10.1111/gcb.13626

Meteorology drivers were derived from the CCSM4 fully coupled Last Millennium (p1000, 850-1849) and AR-5 historical (1850-1900) PMIP3 intercomparison and CRUNCEP data product (1901-2010). Details on the bias correction process to align the two CCSM4 products with CRUNCEP as well as artifacts and biases found in the PalEON met drivers can be found in a document describing Phase 1 drivers. Additional figures and animations illustrating the spatial and temporal patterns of the met drivers over the PalEON modeling domain can be found in the “met_qaqc” in the folder with the raw, sub-daily meteorology drivers.

Access to the data was granted by Christy Rollings and downloaded from Cyverse: https://de.cyverse.org/de/?type=data&folder=/iplant/home/crollinson/paleo. 

Downloading instructions:
After creating a Cyverse account, navigate to the paleon folder, select the desired file and hit 'simple download' in the 'download' menue. I had a little trouble untarring the downloaded files. Here's what whorked for me: files will be downloaded in two parts, 'file.tar.bz2' and 'file.tar.bz2.part' Leave some time for the .part file to be incorporated back into the tar.bz2 file, then move it to its new drectory. Use the following command to untarr it: tar xjf file.tar.bz2

Meteorlogical Driver Descriptions: 
For each meteorological driver, daily data is on a grid of half degree resolution from -100 to -60 longitude and 40 to 60 latitude (80 x 30 grid). Drivers run from 850-2010, with one file per month. 

lwdown: incident longwave radiation averaged over the time step of the forcing data (W m-2)

swdown: incident radiation in the showrtwave part of the spectrum averaged over the time step of the forcing data (W m-2)

precipf: the per unit area and time precipitation representing the sum of convective rainfall, stratiform  rainfall, and snowfall (kg m-2 s-1)

psurf: pressure at the surface (Pa)

qair: specific humididity measured at the lowest level of the atmosphere (kg kg-1)

tair: 2 meter near surface air temperature (K)

wind: wind speed measured with a vertical coordinate in height of 10 m  (m s-1)

