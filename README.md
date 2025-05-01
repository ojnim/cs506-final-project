YOUTUBE LINK: 

# Language and Cognition : the neural relationship

## How to Build and Run the code

**WARNING : the size of the dataset is around 15GB**

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
python3 singletrial_plot
python3 tsnr_plot
python3 tsnr_plot_box
```
3.  Reproduce Result
* fMRI preprocessing
```
bash code/fMRIprep
bash code/tsnrdata_to_csv
```
4. **Test Code and a GitHub workflow that runs the test code**

Since the size of original dataset is around 15 GB, most of the preprocessing work was done locally and data for test run was uploaded in data_for_test directory.

```
git clone https://github.com/ojnim/cs506-final-project.git
cd cs506-final-project
make install
make train
```

## Data Preprocessing

This project is based on https://github.com/OpenNeuroDatasets/ds005455.git and some codes and scripts are modified from https://github.com/GttNeuro/Guo-Lab_datapaper.

### Brain Data
The dataset consists of 77 subjects, and for each subject, 
* anatomical image - a brain image that serves as a structural reference for processing functional images
* functional image - a series of brain image captured over multiple runs of experiment. It has lower resolution compare to anatomical image.



### Participants & Behavioral Data

**Raven Score** : standardized intelligence test that assesses nonverbal reasoning and problem-solving skills through visual patterns. <br>

**CET 4 score** : national English proficiency test for non-English majors in China <br>


## Visualizations

* Mean z for each task
![image info](./images/Mean-z_task-CognitiveControl_vmax03.png)
![image info](./images/Mean-z_task-LanguageControl_vmax03.png)

* Mean tSNR for each task
<p>
<img src="./images/Mean-tSNR_CognitiveControl.png" width="400">
<img src="./images/Mean-tSNR_LanguageControl.png" width="400">
</p>

* Distribution of tSNR per participant and task
![image info](./images/Distribution_of_tSNR_per_participant_and_task_redblue.png)
<br>
What we can commonly observe accross different subjects is tSNR values of CogControl taks are higher than the values of LangControl


* 3D visualization of Temporal Signal-to-Noise Ratio
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

1. Brain Activation Analysis

2. Brain Region Analysis

## Results
Results showing that you achieved your goal.







## Data Processing Method

### Brain Data
In data processing, I used FEAT, FSL's preprocessing tool. FSL is a comprehensive library of analysis tools for functional, structural, and diffusion MRI brain imaging data, developed by the Analysis Group at FMRIB in Oxford.

Detailed description of data processing done so far.

1. Brain Extraction

2. Other preprocessing settings
