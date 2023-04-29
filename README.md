# 12-PyGeoAI
Climate action – finding solutions to challenges related to urban flood, forest fire, wind speed, drought, ecology, and forest fragmentation (SDG #13)

https://archive.ics.uci.edu/ml/datasets/forest+fires

# Methodology
1. Implement the EarthFormer.
2. Check on their dataset.
3. Prepare dataset.
4. Train EarthFormer on Our dataset.
5. Increase dataset for better predictions, fine-tune EarthFormer.
6. Predict.

# Architecture
EarthFormer

# Data Preparation
The data that is to be used has to be in the form of single-channel arrays of dimension N x L x B x T. Here, the meanings of the variables ar ethe following:
N = Batch Size
L = Length of a single image patch
B = Breadth of a single image patch
T = number of images (at T different time intervals) for the particular location.

# Data Sources
https://gisgeography.com/wildfire-maps-real-time/
