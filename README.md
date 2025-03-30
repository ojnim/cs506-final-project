# Language and Cognition : the neural relationship

## Preliminary Visualization of Data

## Data Overview
The dataset consists of 77 subjects, and for each subject, 
* anatomical image - a brain image that serves as a structural reference for processing functional images
* functional image - a series of brain image captured over multiple runs of experiment. It has lower resolution compare to anatomical image.

## Data Processing Method

### Brain Data
In data processing, I used FEAT, FSL's preprocessing tool. FSL is a comprehensive library of analysis tools for functional, structural, and diffusion MRI brain imaging data, developed by the Analysis Group at FMRIB in Oxford.

Detailed description of data processing done so far.

1. Brain Extraction

Since the original image includes skull and non-brain area, we need to remove those area to focus on brain tissue. FSL has brain extraction tool for preprocessing the data.

One variable I experimented with was Fractional intensity threshold, which decides the brain outline estimate and how much to remove. The default value is 0.5, and smaller values give larger brain outline estimate. Among 0.7, 0.5, 0.3, 0.2, and 0.1, the value 0.2 resulted the best skullstripped image with removing skull and not missing brain tissue.

* original data 

* data after bet (Fractional Intensity Threshold = 0.2)


2. Motion Correction

3. Slice - Timing Correction

None

4. Smoothing

Spatial smoothing FWMH (mm) : default 5.0

5. Registration and Normalization

Degree of Freedom

source: https://andysbrainbook.readthedocs.io/en/latest/fMRI_Short_Course/fMRI_04_Preprocessing.html

### Behavioral Data

## Data Modeling Method
Detailed description of data modeling methods used so far.

## Preliminary results
Preliminary results. 
(e.g. we fit a linear model to the data and we achieve promising results, 
or we did some clustering and we notice a clear pattern in the data)

We expect to see preliminary code in your project repo at this point.


## Next Steps

Feature Extraction<br>
* Extract relevant features from structural and task-related functional imaging data
* Process behavioral data (e.g. reaction times, error rate, task_order, task_rule )

Model Training<br>
* Apply linear regression using language proficiency scores, Age of English Acquisition, and extracted fMRI features
* Optimize the model with evaluation

Result Interpretation<br>
* Visualiza key findings using statistical plots and brain activation maps



**Reference** <br>
fMRI short course with fsl https://andysbrainbook.readthedocs.io/en/latest/fMRI_Short_Course/fMRI_Intro.html

Machine learning in fMRI https://www.ehu.eus/ccwintco/uploads/f/f5/Feature_extraction_uji_2010.pdf
