# AIClubWorkshops
This repo houses the various workshops we will be going over for SDSU's AI club for the fall 2020 semester

# Table of Contents
- [Workshop 1](#workshop-1)</summary>
    + [Python Introduction](#python-introduction)
    + [Beginner Python tutorial summary:](#beginner-python-tutorial-summary-)
    + [Activity](#activity)
- [Workshop 2](#workshop-2)
    + [Advanced Python tutorial summary:](#advanced-python-tutorial-summary-)
- [Workshop 3 (Data Science 1)](#workshop-3--data-science-1-)
    + [Cleaning data](#cleaning-data)
    + [Resources Used](#resources-used)
    + [Let's get started with the workshop!](#let-s-get-started-with-the-workshop-)
    + [Code used in the workshop](#code-used-in-the-workshop)
- [Workshop 4 (Data Science 2)](#workshop-4--data-science-2-)
    + [Exploratory Data Analaysis](#exploratory-data-analaysis)
    + [Resources Used](#resources-used-1)
    + [Let's get Started with the workshop!](#let-s-get-started-with-the-workshop-)
    + [Code Used in this workshop](#code-used-in-this-workshop)
- [Workshop 5 (Data Science 3)](#workshop-5--data-science-3-)
    + [Model Building](#model-building)
    + [Resources used](#resources-used)
    + [Let's get started with the workshop](#let-s-get-started-with-the-workshop)
    + [Code Used in this workshop](#code-used-in-this-workshop-1)
- [Workshop 6 (Computer Vision 1)](#workshop-6--computer-vision-1-)
    + [Opencv basic tutorial](#opencv-basic-tutorial)
    + [Resources used](#resources-used-1)
    + [Beginner opencv tutorial summary:](#beginner-opencv-tutorial-summary-)
    + [Activity](#activity-1)
    + [Code Used](#code-used)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'></a></i></small>

# Workshop 1
### Python Introduction
In this workshop we will be going over the basics of using python
- [Click Here](https://hectorenevarez.github.io/AIClubWorkshops/Workshop1/python_tutorial) to be taken to the beginner python workshop

### Beginner Python tutorial summary:
- **Data Types:** Integer, Float, Complex, Boolean, and Strings
- **List:** Overview of a list, list methods, iterating through lists
- **Dictionaries:** Overview of a dictionary, dictionary methods, iterating through a dictionary
- **If Statements:** Declaring if statements, if-else chains, if boolean statements

### Activity
- For this weeks activity we will be doing coding questions that apply our basic knowledge of the fundamentals we learned in workshop 1
- [Sign up Here](https://www.hackerrank.com/sdsu-ai-club-a1) in order to get started with the activity
- [Hints](https://hectorenevarez.github.io/AIClubWorkshops/Workshop1/hints): These hints will be useful to you solving the coding problems

# Workshop 2
In this workshop we will be going over more advanced python concepts
- [Click Here](https://github.com/HectorENevarez/AIClubWorkshops/blob/master/workshop2-Python_Two/Advanced_python.ipynb) to be taken to the advanced python workshop<br>
- [Google Colab Introduction](https://colab.research.google.com/notebooks/intro.ipynb)

### Advanced Python tutorial summary:
- **Loops:** For loops and while loops, loop use case, looping through data structures
- **modules:** Importing modules, giving modules an alias usnig "as"
- **Functions:** defining a functions, arguements and parameters, arbitrary arguements, returning values
- **Lambda Functions:** Syntax, use case, if-else chains
- **Main Function:** \_\_name__ == "\_\_main__", creating main function

# Workshop 3 (Data Science 1)
Our goal with this 3 part workshop is to create a tool that can estimate software engineer salaries. The main purpose of this 3 part workshop is to develop and understand the different roles involved in a typical data science job.

### Cleaning data
- Data collection and data cleaning are said to be the most important and time consuming parts of a data scientists role
- in this workshop we will be going over how to clean the data
- The data was previously collected so we can easily use it for this project

If you are interested in the scripts I used to collect the data [Click Here](https://github.com/HectorENevarez/AIClubWorkshops/tree/master/workshop3-cleaningData/data-collection) but we won't be going over that in this workshop

### Resources Used
- Pandas
- [GlassDoor data](https://github.com/HectorENevarez/AIClubWorkshops/blob/master/workshop3-cleaningData/data-collection/glassdoor_job.csv) Make sure to download the data so we can use it for our workshop
- [Reference Sheet](https://github.com/HectorENevarez/AIClubWorkshops/blob/master/workshop3-cleaningData/reference.ipynb) This reference sheet goes over all the pandas functions we used in depth for better understanding during the workshop

### Let's get started with the workshop!
This workshop is broken down into two parts
- [Part 1](https://github.com/HectorENevarez/AIClubWorkshops/blob/master/workshop3-cleaningData/Pandas-Tutorial.ipynb): For this first part we will go into a very introductory tutorial on pandas that will prepare us enough to begin cleaning our data
- [Part 2](https://colab.research.google.com/notebooks/intro.ipynb): In this part we will be coding from scratch how to clean the data

### Code used in the workshop
- [Data Cleaning](https://github.com/HectorENevarez/AIClubWorkshops/blob/master/workshop3-cleaningData/data-cleaning.py): This will take you to the python script we coded during this workshop just incase you need to look over it after the workshop

# Workshop 4 (Data Science 2)
This is the second part of our data science multi-week workshop. In this workshop we will be going over how to plot our data and analyze for our model building
### Exploratory Data Analaysis
- We will analyze our data for better understanding of the features and their correlation
- We will use our previously cleaned data for this workshop

### Resources Used
- Pandas
- Matplotlib
- Seaborn
- [Cleaned Data](https://github.com/HectorENevarez/AIClubWorkshops/blob/master/workshop3-cleaningData/Salary_Data_Cleaned.csv)

### Let's get Started with the workshop!
- [Google Colab](https://colab.research.google.com/notebooks/intro.ipynb)

### Code Used in this workshop
- [Explortatory Data Analysis](https://github.com/HectorENevarez/AIClubWorkshops/blob/master/Workshop4-EDA/Exploratory_Data_Analysis.ipynb): This will take you to the python script we coded during this workshop just incase you need to look over it after the workshop

# Workshop 5 (Data Science 3)
This is the third and final part to the data science multi-week project. In this workshop we will do create the train and test the models
### Model Building
- We will use the features we decided on in our EDA and create models that will predict how much someone will get payed based on job listing
- The machine learning models we'll use are Linear Regression, Lasso Regression, and Random Forest
 
### Resources used
 - Pandas
 - Matplotlib
 - Numpy
 - Sklearn
 
### Let's get started with the workshop
 - [Google Colab](https://colab.research.google.com/notebooks/intro.ipynb)
 - [Linear Regression](https://docs.google.com/presentation/d/1OE7mU9YThVaxI2YEwmZIL_7L9zrPfVJuMC2NchNdzqw/edit?usp=sharing)
 - [Lasso Regression](google.com)
 - [Random Forest](https://docs.google.com/presentation/d/1k7ZIhzCLB-C0TVyiBadRUIlthqWuctoAV3BWcTUBtbQ/edit?usp=sharing)
 
### Code Used in this workshop
 - [Model Building](https://github.com/HectorENevarez/AIClubWorkshops/blob/master/Workshop5-ModelBuilding/ModelBuilding.ipynb): This will take you to the python script we coded during this workshop just incase you need to look over it after the workshop

# Workshop 6 (Computer Vision 1)
This is the first part of a 3 week-long computer vision workshop. In this workshop we will go over the basics of using opencv for image processing.
### Opencv basic tutorial
In this workshop we will be going over the basic functions of opencv
- [Opencv Workshop](https://github.com/HectorENevarez/AIClubWorkshops/blob/master/Workshop6-Opencv/opencv_tut.ipynb)

### Resources used
- Opencv
- imutils
- matplotlib
- [Tetris Image](https://github.com/HectorENevarez/AIClubWorkshops/blob/master/Workshop6-Opencv/tetris_blocks.png)
- [Reference Sheet](https://github.com/HectorENevarez/AIClubWorkshops/blob/master/Workshop6-Opencv/Reference.ipynb)

### Beginner opencv tutorial summary:
- Loading images
- Cropping images
- resizing images
- rotating images
- **Drawing on images:** rectangle, circle, line, and text

### Activity
- In this activity we will be detecting objects on an image through the use of various built in opencv functions
- [Click here](https://colab.research.google.com) to be taken to google colab in order to get started

### Code Used
- [Object Detection](https://github.com/HectorENevarez/AIClubWorkshops/blob/master/Workshop6-Opencv/object_detect.ipynb) This is the script we coded during this workshop just incase you need to look over it after the workshop 
