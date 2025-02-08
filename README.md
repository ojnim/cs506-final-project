# Language and Cognition : the neural relationship

## Description

This project aims to understand the relationship between language and cognition in the perspective of neuroscience. Specifically, I want to study how much language and cognitive activity are interconnected and influence each other when people are performing the task which requires both ability. 

## Question & Goal
Based on the data inspection result, I formed one question I want to explore through final project.

**In Language Control task, how would self-reported language proficiency score be related to the activation of brain region and reaction time?**

In addition to the project question, there are several goals I want to achieve.

1. Understand how Language and Cognitive activity works together for the tasks that require both
2. Gain experience with processing fMRI image data

Regarding the fMRI data from Cognitive Control task, I would form a research question after I compare the data from Language Control task during data cleaning process.

## Dataset
The dataset that would be used in this project would be "An fMRI dataset for investigating language control and cognitive control in bilinguals" https://github.com/OpenNeuroDatasets/ds005455/tree/main

This dataset is consisted of 77 Chinese-English bilingual's fMRI experiment result and participants data. Each participant completed two tasks during the experiment : language switching task to assess language control and rule switching task to evaluate cognitive control. 

This repository ( https://github.com/GttNeuro/Guo-Lab_datapaper ) contains information about the language control task and cognitive control task.

Language Control : 'naming in L1'
-suggest image and name it

Cognitive Control : 'pressing the same direction'
-press

1. structual imaging data

2. task-related functional imaging data

3. behavioral data from the participants - participant responses and performance metrics


## Modeling Method, Visualization, and Test Plan
Considering the self-reported language proficiency score is an interval variabe, I am considering to use linear regression model primarily. 

For training model, I would use 80% of the data (~62 people), and I would use remaining 20% (15 people) to test model.


## To-Dos
1. Data Inspection & Understanding
2. Data Cleaning
3. Feature Extraction
4. Model Training
5. Result Interpretation


## Back Up Plan (Dataset)
Just in case the project contains a problem which prevents the completion, I would use the data below and plan new project.

General Language Understanding
https://www.kaggle.com/datasets/thedevastator/nli-dataset-for-sentence-understanding?select=qnli_train.csv

Stanford Natural Language Inference
https://www.kaggle.com/datasets/stanfordu/stanford-natural-language-inference-corpus