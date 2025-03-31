YOUTUBE LINK: link

# Language and Cognition : the neural relationship

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

* Motion Correction : MCFLIRT
* Slice - Timing Correction : None (default)
* Smoothing - Spatial smoothing FWMH (mm) : default 5.0
* Registration and Normalization : Degree of Freedom 12

Summary registration, FMRI to standard space <br>
![image info](./images/registration.png)


source: https://andysbrainbook.readthedocs.io/en/latest/fMRI_Short_Course/fMRI_04_Preprocessing.html


### Behavioral Data

1. Missing Data handeling

Since there wasn't null value in behavioral data, this step was skipped

2. Processing data for Correlation matrix

To apply correlation function, columns were grouped into different categories, such as Language_RT, Language_ER, chinese_skills, english_skills


**More info about data can be found in data_inspection.ipynb**

## Data Modeling Method
Detailed description of data modeling methods used so far.

## Preliminary Results & Visualization of Data

### Brain Data
Followings are the resuls from the 1st-level analysis of brain data with sub-001 of Cognitive Control

* Time series graph of BOLD. Left is Switch and Right is Not Switch <br>
![image info](./images/DesignMatrix.png)

![image info](./images/1st-level_analysis.png)

Red areas in the following image are the voxels which are statistically significant for each contrast <br>
![image info](./images/voxel_activation.png)

### Behavior / Participants Data

![image info](./images/AoARavenCET.png)

For midterm report, I focused on analyzing the correlation between various participant data variables to identify the most relevant features for modeling with brain data. Below, I summarize the key correlation patterns observed in the dataset.

![image info](./images/AoA.png)

AoA & English skills Correlation: 
'AoA & English_writing': -0.1444502987593527, 
'AoA & English_listening': -0.15784105846389884, 
'AoA & English_speaking': -0.030329450569710547, 
'AoA & English_reading': -0.15499353085527676, 
'AoA & raven_score': -0.35462051263438893, 
'AoA & CET_4_score': -0.23428551589392765

RTL1S_Chinese_correlation: 
'RT_L1S & Chinese_writing': -0.17181157875905817,
'RT_L1S & Chinese_listening': -0.13034266083903212, 
'RT_L1S & Chinese_speaking': -0.19216220392790564, 
'RT_L1S & Chinese_reading': -0.049387453437041456


RTL1NS_Chinese_correlation:  
'RT_L1NS & Chinese_writing': -0.14431948221685217, 
'RT_L1NS & Chinese_listening': -0.10066014422042956, 
'RT_L1NS & Chinese_speaking': -0.13552622556975719, 
'RT_L1NS & Chinese_reading': -0.05409748262747915


RTL2S_English_correlation: 
'RT_L2S & English_writing': -0.15608745106689872, 
'RT_L2S & English_listening': -0.26285325959694766, 
'RT_L2S & English_speaking': -0.249225000279765, 
'RT_L2S & English_reading': -0.07517967683065574


RTL2NS_English_correlation: 
'RT_L2NS & English_writing': -0.13785607761363033, 
'RT_L2NS & English_listening': -0.22679407408979357, 
'RT_L2NS & English_speaking': -0.23930748130690666, 
'RT_L2NS & English_reading': -0.0905329915511562

![image info](./images/RavenRT.png)

raven_RT_correlations: 
'raven_score & RT_L1S': -0.10192948032642571, 
'raven_score & RT_L1NS': -0.1627018508981041, 
'raven_score & RT_L2S': -0.21882178716367187, 
'raven_score & RT_L2NS': -0.21413055014757756

![image info](./images/RavenER.png)

raven_ER_correlations: 
'raven_score & ER_L1S': -0.027472844891422755, 
'raven_score & ER_L1NS': -0.04825089641629403, 
'raven_score & ER_L2S': -0.2367312466937776, 
'raven_score & ER_L2NS': -0.23652282254830348

![image info](./images/CET4RT.png)

cet_4_RT_correlations: 
'CET_4_score & RT_L1S': 0.02146256794702048, 
'CET_4_score & RT_L1NS': 0.031085003279216688, 
'CET_4_score & RT_L2S': -0.053926295229138145, 
'CET_4_score & RT_L2NS': -0.07319903667206928

![image info](./images/CET4ER.png)

cet_4_ER_correlations: 
'CET_4_score & ER_L1S': -0.09920154371578252, 
'CET_4_score & ER_L1NS': -0.10498877572452256, 
'CET_4_score & ER_L2S': -0.24290970386183677, 
'CET_4_score & ER_L2NS': -0.272698476085984


From this data analysis, the patterns I observed are

**Raven Score** : standardized intelligence test that assesses nonverbal reasoning and problem-solving skills through visual patterns. <br>
* Raven Score is modestly correlated with English proficiency, particularly in reading and writing.
* Higher cognitive ability (Raven Score) and English proficiency (CET 4 Score) are linked to lower error rates in second-language processing.

**CET 4 score** : national English proficiency test for non-English majors in China <br>
* CET 4 Score exhibits stronger correlations with all English skills compare to Raven score, 
![image info](./images/RavenCET_English.png)


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
