# 12-PyGeoAI
# A. Introduction
### Broad Theme : Climate action 
Finding solutions to challenges related to urban flood, forest fire, wind speed, drought, ecology, and forest fragmentation (SDG #13)
### Assigned Theme and Regoin of Interest
**Prediction of Forest Fires (Nowcasting) using a transformer based Deep Learning architecture called EarthFormer. We have fine-tuned the model and used a dataset manually prepared by us for the assigned ROI of Uttarakhand.**

# B. Methodology
1. Implement the EarthFormer. ✅
2. Test on their dataset. ✅
3. Prepare dataset.
4. Train EarthFormer on Our dataset.
5. Increase dataset for better predictions, fine-tune EarthFormer.
6. Predict.

## B1. DL Architecture
EarthFormer
![image](https://user-images.githubusercontent.com/56718090/235289478-a6fce54d-62e3-4272-8e51-500211cb8461.png)
(Image Source : [EarthFormer Paper](https://assets.amazon.science/89/ad/cb9c23dd4bb69b8e03bbbecdb4b8/earthformer-exploring-space-time-transformers-for-earth-system-forecasting.pdf))
## A2. Data Preparation
The data that is to be used has to be in the form of single-channel arrays of dimension N x L x B x T. Here, the meanings of the variables ar ethe following:

N = Batch Size

L = Length of a single image patch

B = Breadth of a single image patch

T = number of images (at T different time intervals) for the particular location.

For our case, we are taking the following values: L = B = 384, T = 13.

So, we need to generate single-channel (0-255 or 8 bit) images with each pixel having a value denoting the intensity of fire in the region. We are taking 13 snapshots of the region at time intervals of 5 days. We are calculating the single channel fire intensity using NBR and dNBR.

### a) NBR (Normalised Burn Ratio)
This is an index designed to highlight burnt areas in large fire zones. The formula combines the use of both near infrared (NIR) and shortwave infrared (SWIR) wavelengths.

Healthy vegetation shows a very high reflectance in the NIR, and low reflectance in the SWIR portion of the spectrum. This is the opposite of what is seen in areas devastated by fire. Freshly burnt areas show a low reflectance in the NIR and high reflectance in the SWIR, i.e. the difference between the spectral responses of healthy vegetation and burnt areas reach their peak in the NIR and the SWIR regions of the spectrum.

To benefit from the magnitude of spectral difference, NBR uses the ratio between NIR and SWIR bands, according to the formula shown below. A high NBR value indicates healthy vegetation while a low value indicates bare ground and recently burnt areas. Non-burnt areas are normally attributed to values close to zero.

![image](https://user-images.githubusercontent.com/56718090/235289287-b2f150b4-77bb-4ccf-abbb-e185707e70c1.png)

(Image Source : [UN SPIDER Knowledge Portal](https://un-spider.org/advisory-support/recommended-practices/recommended-practice-burn-severity/in-detail/normalized-burn-ratio))
### b) dNBR or ΔNBR (Burn Severity)
The difference between the pre-fire and post-fire NBR obtained from the images is used to calculate the delta NBR (dNBR or ∆NBR), which then can be used to estimate the burn severity. A higher value of dNBR indicates more severe damage, while areas with negative dNBR values may indicate regrowth following a fire. The formula used to calculate dNBR is illustrated below:
<center><img src="https://user-images.githubusercontent.com/56718090/235289270-f407ab8a-65ea-47bb-a9f6-4aff93c95a3f.png"></center>

dNBR values can vary from case to case, and so, if possible, interpretation in specific instances should also be carried out through field assessment; in order to obtain the best results. However, the United States Geological Survey (USGS) proposed a classification table to interpret the burn severity, which can be seen below (Table 1).
<center><img src="https://user-images.githubusercontent.com/56718090/235288848-806595d2-b716-40f8-aa54-3bd2582c07b9.png"></center>

(Image Source : [UN SPIDER Knowledge Portal](https://un-spider.org/advisory-support/recommended-practices/recommended-practice-burn-severity/in-detail/normalized-burn-ratio))

### c) Data Sources
1. SEVIR Dataset (for model testing)
2. Custom Dataset Prepared from Google Earth Engine

### d) Data Preparation Steps
**STEP-1) Area Selection (Uttarakhand)**
![image](https://user-images.githubusercontent.com/56718090/235291566-8d9551b4-c39b-487f-8e30-72acf4c7ddc7.png)
**STEP-2) Satellite Imagery of Selected Area (Before Forest Fire)**
![image(1)](https://user-images.githubusercontent.com/56718090/235291574-ce605f5d-ddd4-480f-8d84-e71de3792f9f.png)
**STEP-3) Satellite Imagery of Selected Area (After Forest Fire)**
![image(2)](https://user-images.githubusercontent.com/56718090/235291581-762d4fe2-67b1-479b-ab4d-4584396ae24c.png)
**STEP-4) Satellite Imagery of Selected Area (Before Forest Fire, with Cloud Mask Removed)**
![image(3)](https://user-images.githubusercontent.com/56718090/235291585-87bdce82-30a8-4174-8f80-8cf5a20395ac.png)
**STEP-5) Satellite Imagery of Selected Area (After Forest Fire, with Cloud Mask Removed)**
![image(4)](https://user-images.githubusercontent.com/56718090/235291589-d868922a-3882-45c9-adb8-1fec1db34590.png)
**STEP-6) Calculated dNBR (Gray Scale)**
![image(5)](https://user-images.githubusercontent.com/56718090/235291595-744ae6f0-f3dd-4962-80fc-e3c809af226d.png)
**STEP-7) Calculated dNBR (Classified)**
![image(6)](https://user-images.githubusercontent.com/56718090/235291602-78092320-742e-4733-af35-eca9c64a2648.png)
**STEP-8) Area Selection for Image Export**
![image(7)](https://user-images.githubusercontent.com/56718090/235291606-041a9dd0-ef9e-4434-b8d1-9309da8323bc.png)

The above steps have to be repeated for different areas and for different intervals of time for each of the areas.
### e) DL Model Training and Testing

# B. Observations
# C. Results

<hr>

## References
1. NBR and dNBR : [USGS.gov Landsat Normalised Burn Ratio](https://www.usgs.gov/landsat-missions/landsat-normalized-burn-ratio), [UN SPIDER Knowledge Portal](https://un-spider.org/advisory-support/recommended-practices/recommended-practice-burn-severity/in-detail/normalized-burn-ratio)
2. [EarthFormer (Paper)](https://assets.amazon.science/89/ad/cb9c23dd4bb69b8e03bbbecdb4b8/earthformer-exploring-space-time-transformers-for-earth-system-forecasting.pdf)
3. [SEVIR Dataset (Paper)](https://proceedings.neurips.cc/paper/2020/file/fa78a16157fed00d7a80515818432169-Paper.pdf)
