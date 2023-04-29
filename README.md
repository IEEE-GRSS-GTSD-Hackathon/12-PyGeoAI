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

# DL Architecture
EarthFormer
![image](https://user-images.githubusercontent.com/56718090/235289478-a6fce54d-62e3-4272-8e51-500211cb8461.png)
(Image Source : [EarthFormer Paper][https://assets.amazon.science/89/ad/cb9c23dd4bb69b8e03bbbecdb4b8/earthformer-exploring-space-time-transformers-for-earth-system-forecasting.pdf])
# Data Preparation
The data that is to be used has to be in the form of single-channel arrays of dimension N x L x B x T. Here, the meanings of the variables ar ethe following:

N = Batch Size

L = Length of a single image patch

B = Breadth of a single image patch

T = number of images (at T different time intervals) for the particular location.

For our case, we are taking the following values: L = B = 384, T = 13.

So, we need to generate single-channel (0-255 or 8 bit) images with each pixel having a value denoting the intensity of fire in the region. We are taking 13 snapshots of the region at time intervals of 5 days. We are calculating the single channel fire intensity using NBR and dNBR.

## NBR (Normalised Burn Ratio)
The Normalized Burn Ratio (NBR) is an index designed to highlight burnt areas in large fire zones. The formula is similar to NDVI, except that the formula combines the use of both near infrared (NIR) and shortwave infrared (SWIR) wavelengths.

Healthy vegetation shows a very high reflectance in the NIR, and low reflectance in the SWIR portion of the spectrum (Figure 2) - the opposite of what is seen in areas devastated by fire. Recently burnt areas demonstrate low reflectance in the NIR and high reflectance in the SWIR, i.e. the difference between the spectral responses of healthy vegetation and burnt areas reach their peak in the NIR and the SWIR regions of the spectrum.
![image](https://user-images.githubusercontent.com/56718090/235289287-b2f150b4-77bb-4ccf-abbb-e185707e70c1.png)
To benefit from the magnitude of spectral difference, NBR uses the ratio between NIR and SWIR bands, according to the formula shown below. A high NBR value indicates healthy vegetation while a low value indicates bare ground and recently burnt areas. Non-burnt areas are normally attributed to values close to zero.
## dNBR or ΔNBR (Burn Severity)
The difference between the pre-fire and post-fire NBR obtained from the images is used to calculate the delta NBR (dNBR or ∆NBR), which then can be used to estimate the burn severity. A higher value of dNBR indicates more severe damage, while areas with negative dNBR values may indicate regrowth following a fire. The formula used to calculate dNBR is illustrated below:
![image](https://user-images.githubusercontent.com/56718090/235289270-f407ab8a-65ea-47bb-a9f6-4aff93c95a3f.png)
dNBR values can vary from case to case, and so, if possible, interpretation in specific instances should also be carried out through field assessment; in order to obtain the best results. However, the United States Geological Survey (USGS) proposed a classification table to interpret the burn severity, which can be seen below (Table 1).
![image](https://user-images.githubusercontent.com/56718090/235288848-806595d2-b716-40f8-aa54-3bd2582c07b9.png)

# Data Sources
1. https://gisgeography.com/wildfire-maps-real-time/
2. https://archive.ics.uci.edu/ml/datasets/forest+fires

<hr>

### References
1. NBR and dNBR : https://www.usgs.gov/landsat-missions/landsat-normalized-burn-ratio, https://un-spider.org/advisory-support/recommended-practices/recommended-practice-burn-severity/in-detail/normalized-burn-ratio
2. EarthFormer (Paper) : https://assets.amazon.science/89/ad/cb9c23dd4bb69b8e03bbbecdb4b8/earthformer-exploring-space-time-transformers-for-earth-system-forecasting.pdf
3. SEVIR Dataset (Paper) : https://proceedings.neurips.cc/paper/2020/file/fa78a16157fed00d7a80515818432169-Paper.pdf
