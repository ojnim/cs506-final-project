YOUTUBE LINK: link

# Language and Cognition : the neural relationship

## Preliminary Visualization of Data

## Data Processing Method

### Brain Data
The dataset consists of 77 subjects, and for each subject, 
* anatomical image - a brain image that serves as a structural reference for processing functional images
* functional image - a series of brain image captured over multiple runs of experiment. It has lower resolution compare to anatomical image.

In data processing, I used FEAT, FSL's preprocessing tool. FSL is a comprehensive library of analysis tools for functional, structural, and diffusion MRI brain imaging data, developed by the Analysis Group at FMRIB in Oxford.

Detailed description of data processing done so far.

1. Brain Extraction

Since the original image includes skull and non-brain area, we need to remove those area to focus on brain tissue. FSL has brain extraction tool for preprocessing the data.

One variable I experimented with was Fractional intensity threshold, which decides the brain outline estimate and how much to remove. The default value is 0.5, and smaller values give larger brain outline estimate. Among 0.7, 0.5, 0.3, 0.2, and 0.1, the value 0.2 resulted the best skullstripped image with removing skull and not missing brain tissue.

* original data 
![image info](./images/brain_original.png)
* data after bet (Fractional Intensity Threshold = 0.2)
![image info](./images/brain_bet.png)

2. Other preprocessing settings

Followings are the setting values for preprocessing

1) Motion Correction : MCFLIRT
2) Slice - Timing Correction : None (default)
3) Smoothing - Spatial smoothing FWMH (mm) : default 5.0
4) Registration and Normalization : Degree of Freedom 12

![image info](./images/registration.png)

source: https://andysbrainbook.readthedocs.io/en/latest/fMRI_Short_Course/fMRI_04_Preprocessing.html

3. 1st-Level Analysis

Left is Switch and Right is Not Switch
![image info](./images/DesignMatrix.png)


![image info](./images/1st-level_analysis.png)

Red areas in the following image are the voxels which are statistically significant for each contrast
![image info](./images/voxel_activation.png)

### Behavioral Data

- No null value in behavioral data

## Data Modeling Method
Detailed description of data modeling methods used so far.

## Preliminary results
Preliminary results. 
(e.g. we fit a linear model to the data and we achieve promising results, 
or we did some clustering and we notice a clear pattern in the data)

We expect to see preliminary code in your project repo at this point.


## Next Steps

1. Preprocess the remaining dataset with the same setting

bash script to run the analysis

the result would be the basis of the group analysis

2. Feature Extraction

* Extract relevant features from structural and task-related functional imaging data
* Process behavioral data (e.g. reaction times, error rate, task_order, task_rule )

3. Model Training
* Apply linear regression using language proficiency scores, Age of English Acquisition, and extracted fMRI features
* Optimize the model with evaluation

4. Result Interpretation
* Visualiza key findings using statistical plots and brain activation maps



**Reference** <br>
fMRI short course with fsl https://andysbrainbook.readthedocs.io/en/latest/fMRI_Short_Course/fMRI_Intro.html

Machine learning in fMRI https://www.ehu.eus/ccwintco/uploads/f/f5/Feature_extraction_uji_2010.pdf
