# General Information
- For more information regarding our club please visit the official [SDSU AI Club webstite](https://aiclub.sdsu.edu/)
- For further information regarding the workshops you can contact me through my email: <hnevarez1285@sdsu.edu>
- For general club questions you can contact our club email: <sdsuaiclub@gmail.com>

# Table of Contents
- [Workshop 1 (Python 1)](#workshop-1)
- [Workshop 2 (Python 2)](#workshop-2)
- [Workshop 3 (Data Science 1)](#workshop-3-data-science-1)
- [Workshop 4 (Data Science 2)](#workshop-4-data-science-2)
- [Workshop 5 (Data Science 3)](#workshop-5-data-science-3)
- [Workshop 6 (Computer Vision 1)](#workshop-6-computer-vision-1)
- [Workshop 7 (Computer Vision 2)](#workshop-7-computer-vision-2)
- [Workshop 8 (Computer Vision 3)](#workshop-8-computer-vision-3)
- [Workshop 9 (K means clustering)](#workshop-9-K-means-clustering)
- [Workshop 10 (Convolutional Neural Network)](#workshop-10-convolutional-neural-network)

# Workshop 1
### Python Introduction
In this workshop we will be going over the basics of using python
- [Click Here](https://hectorenevarez.github.io/AIClubWorkshopsFall20/Workshop1/python_tutorial) to be taken to the beginner python workshop

### Beginner Python tutorial summary:
- **Data Types:** Integer, Float, Complex, Boolean, and Strings
- **List:** Overview of a list, list methods, iterating through lists
- **Dictionaries:** Overview of a dictionary, dictionary methods, iterating through a dictionary
- **If Statements:** Declaring if statements, if-else chains, if boolean statements

### Activity
- For this weeks activity we will be doing coding questions that apply our basic knowledge of the fundamentals we learned in workshop 1
- [Sign up Here](https://www.hackerrank.com/sdsu-ai-club-a1) in order to get started with the activity
- [Hints](https://hectorenevarez.github.io/AIClubWorkshopsFall20/Workshop1/hints): These hints will be useful to you solving the coding problems

# Workshop 2
In this workshop we will be going over more advanced python concepts
- [Click Here](https://hectorenevarez.github.io/AIClubWorkshopsFall20/Workshop2/Advanced_python.html) to be taken to the advanced python workshop<br>
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

If you are interested in the scripts I used to collect the data [Click Here](https://hectorenevarez.github.io/AIClubWorkshopsFall20/tree/master/workshop3-cleaningData/data-collection) but we won't be going over that in this workshop

### Let's get started with the workshop!
This workshop is broken down into two parts
- [Part 1](https://hectorenevarez.github.io/AIClubWorkshopsFall20/Workshop3/pandas_tutorial): For this first part we will go into a very introductory tutorial on pandas that will prepare us enough to begin cleaning our data
- [Part 2](https://colab.research.google.com/drive/1T9qbWtNIG-AwLoF4Uwbp9EoNwLSP9Vlu?usp=sharing): In this part we will be coding from scratch how to clean the data

### Resources Used
- Pandas
- [GlassDoor data](https://hectorenevarez.github.io/AIClubWorkshopsFall20/blob/master/workshop3-cleaningData/data-collection/glassdoor_job.csv) Make sure to download the data so we can use it for our workshop
- [Reference Sheet](https://hectorenevarez.github.io/AIClubWorkshopsFall20/Workshop3/reference) This reference sheet goes over all the pandas functions we used in depth for better understanding during the workshop

### Code used in the workshop
- [Data Cleaning](https://colab.research.google.com/drive/1jomd9YD5EFm4IEM7wD_HQieZtDIXuFnF?usp=sharing): This will take you to the python script we coded during this workshop just incase you need to look over it after the workshop

# Workshop 4 (Data Science 2)
This is the second part of our data science multi-week workshop. In this workshop we will be going over how to plot our data and analyze for our model building
### Exploratory Data Analaysis
- We will analyze our data for better understanding of the features and their correlation
- We will use our previously cleaned data for this workshop

### Resources Used
- Pandas
- Matplotlib
- Numpy
- [Cleaned Data](https://hectorenevarez.github.io/AIClubWorkshopsFall20/blob/master/workshop3-cleaningData/Salary_Data_Cleaned.csv)

### Let's get Started with the workshop!
- [Numpy](https://hectorenevarez.github.io/AIClubWorkshopsFall20/Workshop4/plt_sns_tut#Numpy) First we're going to go over the numpy library to become familiar with numpy arrays
- [Matplotlib](https://hectorenevarez.github.io/AIClubWorkshopsFall20/Workshop4/plt_sns_tut#Matplotlib) Next, we'll go over matplotlibs pyplot module in order to develop an understanding for how we'll use our data to perform exploratory data anlysis
- [Google Colab](https://colab.research.google.com/drive/1PH5IKXM3pYrjTFtdT-BQblCCsozVbiPn?usp=sharing) Finally we will analyze our data using both numpy and matplotlib in order to create graphs that will help us understand relationships between our data

### Code Used in this workshop
- [Explortatory Data Analysis](https://colab.research.google.com/drive/1Jnv9y4Vi2tIEvQclH2K6JHBMYJrf8FRh?usp=sharing): This will take you to the python script we coded during this workshop just incase you need to look over it after the workshop

# Workshop 5 (Data Science 3)
This is the third and final part to the data science multi-week project. In this workshop we will do create the train and test the models
### Model Building
- We will use the features we decided on in our EDA and create models that will predict how much someone will get payed based on job listing
- The machine learning models we'll use are Linear Regression, Lasso Regression, and Random Forest
 
### Resources used
 - Pandas
 - Sklearn
 - Pickly
 - [Reference Sheet](https://hectorenevarez.github.io/AIClubWorkshops/Workshop5/reference)
 
### Let's get started with the workshop
 - [Google Colab](https://colab.research.google.com/drive/1w5YDrzYwqf0ST93rYXVD5yqXrOefgwx1?usp=sharing)
 - [Support Vector Regressor](https://hectorenevarez.github.io/AIClubWorkshopsFall20/Workshop5/reference#Support-Vector-Regression)
 - [Random Forest](https://hectorenevarez.github.io/AIClubWorkshopsFall20/Workshop5/reference#Random-Forest-Regressor)
 
### Code Used in this workshop
 - [Model Building](https://colab.research.google.com/drive/1-I8pxFQLq1IfOKyKOvHQpGH09rZ4saYv?usp=sharing): This will take you to the python script we coded during this workshop just incase you need to look over it after the workshop

# Workshop 6 (Computer Vision 1)
This is the first part of a 4 week-long computer vision workshop. In this workshop we will go over the basics of using opencv for image processing.
### Opencv basic tutorial
In this workshop we will be going over the basic functions of opencv
- [Opencv Workshop](https://hectorenevarez.github.io/AIClubWorkshopsFall20/Workshop6/opencv_tut)

### Resources used
- Opencv
- imutils
- matplotlib
- [Tetris Image](https://hectorenevarez.github.io/AIClubWorkshopsFall20/blob/master/Workshop6-Opencv/tetris_blocks.png)
- [Reference Sheet](https://colab.research.google.com/drive/1WragbmteUW2Z35qed4ydgMRGT9s2jEci?usp=sharing)

### Beginner opencv tutorial summary:
- Loading images
- Cropping images
- resizing images
- rotating images
- **Drawing on images:** rectangle, circle, line, and text

### Activity
- In this activity we will be detecting objects on an image through the use of various built in opencv functions
- [Click here](https://colab.research.google.com/drive/1rl4b77HcGTyPSZIG_Nsnu_s6qfWxysUa?usp=sharing) to be taken to google colab in order to get started

### Code Used
- [Object Detection](https://github.com/HectorENevarez/AIClubWorkshopsFall20/blob/master/Workshop6-Opencv/object_detect.ipynb) This is the script we coded during this workshop just incase you need to look over it after the workshop 

# Workshop 7 (Computer Vision 2)
This is the second part of the computer vision workshop. In this workshop we will expand our knowledge of OpenCV and work with real-time video. We will be creating an application that can track motion allow us to draw by using our webcam.

### Resources Used
- OpenCV
- Numpy
- [Reference Sheet](https://colab.research.google.com/drive/169rZ0wjf-pIuU2IavLbeZ4doOQn0tHsP)

### Code Used
[AirDraw explained](https://colab.research.google.com/drive/1FPH8VNcsJqw15G2IcK4J7DX0ANtbb8hH)<br>
[AirDraw Code Complete](https://github.com/HectorENevarez/AIClubWorkshopsFall20/blob/master/workshop7-Air_Draw/air_draw.py)

# Workshop 8 (Computer Vision 3)
This is the third and final part of our computer vision workshops. In this workshop we will be learning about neural networks and creating a neural network that can be trained to recognize hand written numbers

### Resources Used
- Tensorflow
- Keras
- Matplotlib

### Neural Network introduction
- [Neural Networks](https://colab.research.google.com/drive/1Zqr0T2tMR10vXRl2LhK8dz2yZFD2f-hD?usp=sharing)

### Activity
- We wil be creating a neural network and train it on the MNIST dataset in order to accurately predict hand written numbers
- [Click Here](https://colab.research.google.com/drive/1nfcOd-0HGci9XwfXmwGN9gxO5P9Z7X11?usp=sharing) to begin the activity

### Code Used
[MNIST model building](https://colab.research.google.com/drive/1_dXwSA4kGFTma-pcCVd5OLPval-dAaSr?usp=sharing)

# Workshop 9 (K means clustering)
In this workshop we will be going over unsupervised learning. We will then learn a clustering machine learning model and use it in order to cluster different types of shoppers in a mall.

### Resources Used
- Pandas
- Matplotlib
- Seaborn
- Scikit Learn

### Neural Network introduction
- [K-means Clustering Introduction](https://colab.research.google.com/drive/1HP6Il2fZ3N90ZrumVOPNOVl_RgiFvg2-?usp=sharing)

### Activity
- We will be implementing K-means to cluster different types of mall shoppers
- [Click Here](https://colab.research.google.com/drive/1bViGVwEg1K1tdnNmG2GjS7JKin8Xn5yQ?usp=sharing) to begin the activity

### Code Used
- [K-means](https://colab.research.google.com/drive/11buFc9fokEiInMTvjVz2eR7wJOEyDAmF?usp=sharing)

# Workshop 10 (Convolutional Neural Network)
In this workshop I will be introducing Convolutional Neural Networks. To do so we will first go over the theory of how a CNN is structured and after we will have a live coding session where we try and classify different types of objects using the Cifar-10 dataset.

### Resources Used
- Tensorflow
- Keras
- Numpy
- Matplotlib

### Neural Network introduction
- [Convolutional Neural Networks](https://colab.research.google.com/drive/1zAN-HhsZmBr3suZWHgAlYBytzyxSpkQH?usp=sharing)

### Activity
- We wil be creating a Convolutional Neural Network and train it on the Cifar-10 dataset in order to accurately predict different objects
- [Click Here](https://colab.research.google.com/drive/1ywNVfge-1fus9zseiueP0UlBnzrKHTtw?usp=sharing) to begin the activity

### Code Used
[Convolutional Neural Network applied to Cifar-10](https://colab.research.google.com/drive/1pJlxubM7SIAyWFy9AKGW6lLyNXeMQ3nW?usp=sharing)
