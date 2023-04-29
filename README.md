# 12-PyGeoAI
### Broad Theme : Climate action 
Finding solutions to challenges related to urban flood, forest fire, wind speed, drought, ecology, and forest fragmentation (SDG #13)
### Assigned Theme and Regoin of Interest
**Prediction of Forest Fires (Nowcasting) using a transformer based Deep Learning architecture called EarthFormer. We have fine-tuned the model and used a dataset manually prepared by us for the assigned ROI of Uttarakhand.**

# Methodology
1. Implement the EarthFormer. ✅
2. Test on their dataset. ✅
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

For our case, we are taking the following values: L = B = 384, T = 13.

So, we need to generate single-channel (0-255 or 8 bit) images with each pixel having a value denoting the intensity of fire in the region. We are taking 13 snapshots of the region at time intervals of 5 days. We are calculating the single channel fire intensity using NBR and dNBR.

## NBR (Normalised Burn Ratio)

## dNBR or ΔNBR (Burn Severity)
![image](https://user-images.githubusercontent.com/56718090/235288848-806595d2-b716-40f8-aa54-3bd2582c07b9.png)

# Data Sources
1. https://gisgeography.com/wildfire-maps-real-time/
2. https://archive.ics.uci.edu/ml/datasets/forest+fires

<hr>

### References
1. NBR and dNBR : https://www.usgs.gov/landsat-missions/landsat-normalized-burn-ratio, https://un-spider.org/advisory-support/recommended-practices/recommended-practice-burn-severity/in-detail/normalized-burn-ratio
2. EarthFormer (Paper) : https://assets.amazon.science/89/ad/cb9c23dd4bb69b8e03bbbecdb4b8/earthformer-exploring-space-time-transformers-for-earth-system-forecasting.pdf
3. SEVIR Dataset (Paper) : https://proceedings.neurips.cc/paper/2020/file/fa78a16157fed00d7a80515818432169-Paper.pdf
