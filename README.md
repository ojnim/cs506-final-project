# Language and Cognition : the neural relationship

## Description

This project aims to understand the relationship between language and cognition in the perspective of neuroscience. Specifically, I want to study how language and cognitive activity are interconnected and influence each other when individuals perform tasks requiring both abilities. 

## Research Question & Goals
Based on the preliminary data inspection, I formulated the following research question for my final project:

**In the Language Control task, how do self-reported language proficiency scores and Age of English Acquisition relate to brain region activation and reaction time?**

Additionally, I intend to develop a research question regarding the fMRI data from the Cognitive Control task after comparing it with the Language Control task data during the data cleaning process.

In addition to the research question, there are several goals I want to achieve on a personal level.
1. Understand how Language and Cognitive activity works together for the tasks that require both
2. Gain experience in processing fMRI image data

## Dataset
The dataset that would be used in this project would be "An fMRI dataset for investigating language control and cognitive control in bilinguals" https://github.com/OpenNeuroDatasets/ds005455/tree/main

This dataset consists of fMRI experimental results and participant data from 77 Chinese-English bilinguals. During functional MRI scanning, each participant completed two tasks: <br>
1. Language Control : 'naming in L1'<br>
Participants were shown images and asked to name the object in their first language (L1). <br>
2. Cognitive Control : 'pressing the same direction'<br>
Participants were shown right or left arrows and asked to press a button corresponding to the same direction.

Further details about these tasks are available in https://github.com/GttNeuro/Guo-Lab_datapaper 

**Data**
1. structual imaging data(anatomical)

2. task-related functional imaging data(functional)

3. behavioral data from the participants - participant responses and performance metrics


## Modeling Method, Visualization, and Test/Evaluation Plan
Since the self-reported language proficiency score is an interval variable, I plan to use a **linear regression model** as the primary approach.

For **model training and testing**, I will:
* Use 80% of the data (~62 participants) for training.
* Use 20% of the data (15 participants) for testing.

For the evaluation of model,
* Mean Squared Error : measures the average squared differences between actual and predicted values
* R-squared Score : indicates the proportion of variance in the dependent variable explained by the model

Followings are the candidates for **data visualization** 
* Scatter Plots : relationships between self-reported proficiency, age of acquisition, and reaction time
* Heatmap : correlation matrices between different brain regions and behavioral metrics
* Boxplots/Violin Plots : compare brain activation intensities across different language proficiency levels
* Dimensionality Reduction : demonstrate patterns in high-dimensional fMRI data<br>


## Steps
1. Data Inspection & Understanding
Since I do not have a background on neuroscience, I would spend most of my time learning how to process fMRI data and use for analysis.

**Reference**
fMRI short course with fsl https://andysbrainbook.readthedocs.io/en/latest/fMRI_Short_Course/fMRI_Intro.html

Machine learning in fMRI https://www.ehu.eus/ccwintco/uploads/f/f5/Feature_extraction_uji_2010.pdf


2. Data Cleaning 
* Handle missing data

3. Feature Extraction
* Normalization of fMRI data

4. Model Training
* Linear regression with language proficiency score and features from normalized fMRI data

5. Result Interpretation


## Back Up Plan (Dataset)
Just in case the project contains a problem which prevents the completion, I would use the data below and plan new project.

General Language Understanding
https://www.kaggle.com/datasets/thedevastator/nli-dataset-for-sentence-understanding?select=qnli_train.csv

Stanford Natural Language Inference
https://www.kaggle.com/datasets/stanfordu/stanford-natural-language-inference-corpus