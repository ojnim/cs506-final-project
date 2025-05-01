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
```
cd code
python3 tsnrdata_to_csv
python3 singletrial_activation
#Run All modeling.ipynb
```

**4. Test Code and a GitHub workflow that runs the test code**

Since the size of original dataset is around 15 GB, the initial stage of preprocessed were completed locally, and 10 subjects out of 77 were sampled for test. The sample data is in data_for_test directory.

```
git clone https://github.com/ojnim/cs506-final-project.git
cd cs506-final-project
make install
make preprocess
make train
```

## Data Preprocessing

This project is based on https://github.com/OpenNeuroDatasets/ds005455.git and some codes and scripts are modified from https://github.com/GttNeuro/Guo-Lab_datapaper.

### Brain Data
The dataset consists of 77 subjects, and for each subject, 
* anatomical image - a brain image that serves as a structural reference for processing functional images
* functional image - a series of brain image captured over multiple runs of experiment. It has lower resolution compare to anatomical image.

In data processing, FSL's preprocessing tool FEAT was used for fMRI data preprocessing and computing the temporal signal-to-noise ratio . FSL is a comprehensive library of analysis tools for functional, structural, and diffusion MRI brain imaging data, developed by the Analysis Group at FMRIB in Oxford.

After preprocessing works (e.g. brain extraction, motion correction, smoothing, and normalization) on Brain data was done through the bash script with preprocessing templates in templates directory, to verify the meaningful voxels to analyze, Temporal Signal-to-Noise Ratio was calculated with nilearn library and saved to csv file with Voxel Value, X, Y, Z, Task, and Subject columns.

From tsnr_voxel_data.csv, the rows whose Voxel Value is NaN are dropped.

Reference: https://github.com/GttNeuro/Guo-Lab_datapaper , https://github.com/DVS-Lab/srndna-datapaper?tab=readme-ov-file 

### Participants & Behavioral Data

**Original Columns** : 'participant_id', 'age', 'sex', 'task_order', 'task_rule', 'AoA', "RT_L1S","RT_L1NS","RT_L2S","RT_L2NS", "ER_L1S","ER_L1NS","ER_L2S","ER_L2NS","raven_score", "CET_4_score", "Chinese_writing", "Chinese_listening", "Chinese_speaking", "Chinese_reading", "English_writing", "English_listening", "English_speaking", "English_reading"
<br>

For the analysis of both Tasks, Reaction Time and Error Rate columns are included since they are collected during the experiment. he columns of self-reported language skills were excluded during the feature selection process since the other column alreay relects the participants' language ability and its subjectivity. However, they were utilized during the correlation analysis in feature selection process to identify which columns shows meaningful relationship with language abilities.

1. Language Task Features<br>
['age', 'AoA', 'CET_4_score','RT_L1S', 'RT_L1NS', 'RT_L2S', 'RT_L2NS','ER_L1S', 'ER_L1NS', 'ER_L2S', 'ER_L2NS']

CET 4 : national English proficiency test for non-English majors in China

2. Cognitive Task Features<br>
['age', 'AoA', 'raven_score', 'RT_L1S', 'RT_L1NS', 'RT_L2S', 'RT_L2NS','ER_L1S', 'ER_L1NS', 'ER_L2S', 'ER_L2NS']

raven score : standardized intelligence test that assesses nonverbal reasoning and problem-solving skills through visual patterns


**More info about Participants & Behavioral Data can be found in data_inspection.ipynb, behavioral_data_analysis.ipynb**

## Visualizations

* Mean z for each task : The mean of single-trial fMRI activation estimates for both tasks. They are averaged across 77 subjects.

<img src="./images/Mean-z_task-CognitiveControl_vmax03.png" width="900">
<img src="./images/Mean-z_task-LanguageControl_vmax03.png" width="900">

* Mean tSNR for each task : The mean temporal Signal-to-Noise Ratio (tSNR) map for both tasks (left: Cognitive, right: Language)
<p>
<img src="./images/Mean-tSNR_CognitiveControl.png" width="380">
<img src="./images/Mean-tSNR_LanguageControl.png" width="380">
</p>

* Distribution of tSNR per participant and task
![image info](./images/Distribution_of_tSNR_per_participant_and_task_redblue.png)
<br>
What we can commonly observe accross different subjects is tSNR values of CogControl taks are higher than the values of LangControl


* 3D visualization of Temporal Signal-to-Noise Ratio
![image info](./images/voxel_3d.gif)


## Modeling
Description of data processing and modeling (what the code does).

1. Brain Activation Analysis

2. Brain Region Analysis

Model : Linear Regression

The reason linear regression was selected is to analyze relationships between continuous variables. In Brain Region Analysis, Dependent variable would be the voxel value, which is a continuous value from brain image.

## Results
Results showing that you achieved your goal.