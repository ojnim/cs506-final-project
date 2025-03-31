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

### Behavioral / Participant Data

Since the data is already cleaned and preprocessed by the data uploader and the null value was not found in the dataset, the original data was used for the analysis.

**More info about data can be found in data_inspection.ipynb**

## Data Modeling Method

1. The General Linear Model - for brain data

With a GLM, we can use one ore more regressors, or independent variables, to fit a model to some outcome measure, or dependent variable. To do this we compute numbers called beta weights, which are the relative weights assigned to each regressor to best fit the data. Any discrepancies between the model and the data are called residuals.

In FEAT analysis, the number of EV(Explanatory Variables) would be the number of regressors, and other settings, such as Basic shape, Convolution, Phase, temporal derivative, temporal filtering, would influence on beta weights and residuals for the general linear modeling.

2. Correlation - for behavioral/participants data

Correlation analysis is used to measure the strength and direction of the relationship between different variables. In this study, correlation analysis was performed to assess the relationships between cognitive scores, language proficiency measures, and reaction times. Pearson correlation coefficients were computed to quantify these relationships, providing insights into potential dependencies among variables.

For instance, correlations were examined between Raven's Progressive Matrices scores and English proficiency measures (writing, listening, speaking, and reading), as well as between CET 4 scores and the same language skills. Additionally, age of acquisition (AoA) was correlated with various language and cognitive measures to investigate its impact on learning outcomes. 

This method helps in selecting relevant features for further modeling and understanding the underlying structure of the data before applying more complex analytical techniques.

## Preliminary Results & Visualization of Data

### Brain Data
Stats
* Number of original EVs:2
* EV1: SWITCH, EV2: NOTSWITCH
* Basic shape: Custom (3 column format)
* Convolution: Double_Gamma HRF
* Phase: 0
* NO temporal derivative, temporal filtering

Contrasts & F-tests
* Contrast: 1, F-tests: 0

Post-stats
* Thresholding: Cluster
* Z threshold: 3.1
* P threshold: 0.05

**RESULT**

* Followings are the results from the 1st-level analysis of brain data with sub-001 of Cognitive Control

Time series graph of BOLD. Left is Switch and Right is Not Switch <br>
![image info](./images/DesignMatrix.png)

* The result from the general linear model<br>
The red line(data) is the original BOLD graph, and green(cope partial model fit) and blue(full model fit) lines are the results of the GLM. 
![image info](./images/1st-level_analysis.png)

* Red areas in the following image are the voxels which are statistically significant for each contrast <br>
![image info](./images/voxel_activation.png)

### Behavior / Participants Data

For midterm report, I focused on analyzing the correlation between various participant data variables to identify the most relevant features for modeling with brain data. Below, I summarize the key correlation patterns observed in the dataset.

![image info](./images/AoA.png)

* Age of Acquisition (AoA) & English Skills Correlations <br>
AoA showed negative correlations with all English skills, with the strongest effects in listening (-0.1578), reading (-0.1550), and writing (-0.1445). This suggests that earlier exposure to English is associated with better language proficiency. Additionally, AoA negatively correlated with Raven Score (-0.3546) and CET 4 Score (-0.2343), implying that early language acquisition may be linked to higher cognitive and language proficiency.


![image info](./images/AoARavenCET.png)

Raven Score & CET 4 Score Correlation: 0.233705913960944 <br>

* Chinese Langauge RT Correlations <br>
Both RT_L1S and RT_L1NS exhibited negative correlations with Chinese language skills. The strongest effects were seen in speaking (-0.1922 for RT_L1S, -0.1355 for RT_L1NS) and writing (-0.1718 for RT_L1S, -0.1443 for RT_L1NS), indicating that faster reaction times may be associated with better proficiency in Chinese. Reading was the least correlated.

* English Langauge RT Correlations <br>
RT_L2S and RT_L2NS negatively correlated with English skills, particularly in listening (-0.2629 for RT_L2S, -0.2268 for RT_L2NS) and speaking (-0.2492 for RT_L2S, -0.2393 for RT_L2NS). This suggests that faster reaction times are linked to better English proficiency, particularly in oral and auditory skills. Reading was also the one which is least correlated.

**Raven Score** : standardized intelligence test that assesses nonverbal reasoning and problem-solving skills through visual patterns. <br>

![image info](./images/RavenRT.png)
![image info](./images/RavenER.png)

Raven Score negatively correlated with all reaction time measures, with the strongest effects observed in RT_L2S (-0.2188) and RT_L2NS (-0.2141). This suggests that higher cognitive ability is associated with faster reaction times, particularly for second-language processing. The Raven Score also negatively correlated with error rates, with the strongest effects in ER_L2S (-0.2367) and ER_L2NS (-0.2365), implying that higher nonverbal reasoning ability reduces errors in second-language processing. Higher cognitive ability (Raven Score) and English proficiency (CET 4 Score) are linked to lower error rates in second-language processing.

**CET 4 score** : national English proficiency test for non-English majors in China <br>

![image info](./images/CET4RT.png)
![image info](./images/CET4ER.png)

CET 4 Score exhibited weak correlations with reaction times, with a small negative effect on RT_L2S (-0.0539) and RT_L2NS (-0.0732). This suggests that English proficiency has a minor impact on reaction time performance. Stronger negative correlations were found between CET 4 Score and error rates, particularly for ER_L2S (-0.2429) and ER_L2NS (-0.2727), suggesting that higher English proficiency reduces errors in second-language tasks.

* CET 4 Score exhibits stronger correlations with all English skills compare to Raven score except reading. 

![image info](./images/RavenCET_English.png)


## Next Steps

1. Preprocess the remaining dataset with the same setting

The initial preprocessing was performed only on subject sub-001. To ensure consistency across all subjects, the same preprocessing settings must be applied to the remaining 76 subjects. A Bash script will be developed to automate both preprocessing and first-level analysis for all participants.

2. Feature Extraction

Relevant features will be extracted from both structural and task-related functional imaging data to capture meaningful patterns related to brain structure and function.

3. Data Analysis with modeling
* 2nd-level analysis with brain data : Compute subject-wise parameter and contrast estimates by averaging first-level analysis results
* 3rd-level analysis with brain data : Conduct a group-level analysis to calculate the standard error and mean of contrast estimates. Perform statistical significance tests to determine whether the observed contrast estimates are meaningful.
* Apply linear regression using language proficiency scores, Age of English Acquisition, and extracted fMRI features
* Optimize the model with evaluation

4. Result Interpretation
* Visualize key findings using statistical plots and brain activation maps to highlight meaningful patterns and relationships between brain activity and language proficiency.



**Reference** <br>
fMRI short course with fsl https://andysbrainbook.readthedocs.io/en/latest/fMRI_Short_Course/fMRI_Intro.html

Machine learning in fMRI https://www.ehu.eus/ccwintco/uploads/f/f5/Feature_extraction_uji_2010.pdf
