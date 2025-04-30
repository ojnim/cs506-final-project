YOUTUBE LINK: 

# Language and Cognition : the neural relationship

## How to Build and Run the code

1.  Initial setup for reproduction

```
git clone https://github.com/ojnim/cs506-final-project.git
cd cs506-final-project
make install
datalad clone https://github.com/OpenNeuroDatasets/ds005455.git data
cd data
datalad get *
mkdir -p ../data/derivatives/figure
```
2. Reproduce Figures

```
cd code
python singletrial_plot
python tsnr_plot
python tsnr_plot_box
```
3.  Reproduce Result
* fMRI preprocessing
```
bash /code/fMRIprep
bash /code/tsnrdata_to_csv
```
4. Test Code and a GitHub workflow that runs the test code

Just test a few things you think are important - no need to overdo it on the testing front, since that’s not the focus of the project.


## Visualizations of data

* Mean z for each task
![image info](./images/Mean-z_task-CognitiveControl_vmax03.png)
![image info](./images/Mean-z_task-LanguageControl_vmax03.png)

* Mean tSNR for each task
![image info](./images/Mean-tSNR_CognitiveControl.png)
![image info](./images/Mean-tSNR_LanguageControl.png)

* Distribution of tSNR per participant and task
![image info](./images/Distribution_of_tSNR_per_participant_and_task_redblue.png)
<br>
What we can commonly observe accross different subjects is tSNR values of CogControl taks are higher than the values of LangControl

![image info](./images/voxel_3d.gif)

## Data Processing

### fMRI data

For the brain data

The templates for FSL group processing can be found in templates directory in.

1. Compute tsnr

tsnr is 

* compute_tsnr
* compute_mean_tsnr
* tsnr_plot
* tsnr_plot_box



Reference: https://github.com/GttNeuro/Guo-Lab_datapaper , https://github.com/DVS-Lab/srndna-datapaper?tab=readme-ov-file 

2. transform data into analyzable format in python

* tsnrdata_to_csv

The csv file produced from tsnrdata_to_csv would contain

Voxel Value
X,Y,Z
Task
Subject

3. 



### Behavioral data

1. Language Task

2. Cognitive Task

**More info about data can be found in data_inspection.ipynb**

## Modeling
Description of data processing and modeling (what the code does).

## Results
Results showing that you achieved your goal.







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

## Data Modeling Method

1. The General Linear Model - for brain data

With a GLM, we can use one ore more regressors, or independent variables, to fit a model to some outcome measure, or dependent variable. To do this we compute numbers called beta weights, which are the relative weights assigned to each regressor to best fit the data. Any discrepancies between the model and the data are called residuals.

In FEAT analysis, the number of EV(Explanatory Variables) would be the number of regressors, and other settings, such as Basic shape, Convolution, Phase, temporal derivative, temporal filtering, would influence on beta weights and residuals for the general linear modeling.


## Preliminary Results & Visualization of Data

### Brain Data

**RESULT**

* Followings are the results from the 1st-level analysis of brain data with sub-001 of Cognitive Control

Time series graph of BOLD. Left is Switch and Right is Not Switch <br>
![image info](./images/DesignMatrix.png)

* The result from the general linear model<br>
The red line(data) is the original BOLD graph, and green(cope partial model fit) and blue(full model fit) lines are the results of the GLM. 
![image info](./images/1st-level_analysis.png)

* Red areas in the following image are the voxels which are statistically significant for each contrast <br>
![image info](./images/voxel_activation.png)


**Raven Score** : standardized intelligence test that assesses nonverbal reasoning and problem-solving skills through visual patterns. <br>

**CET 4 score** : national English proficiency test for non-English majors in China <br>



4. Result Interpretation
* Visualize key findings using statistical plots and brain activation maps to highlight meaningful patterns and relationships between brain activity and language proficiency.
