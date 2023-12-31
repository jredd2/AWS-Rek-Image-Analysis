<br>![Alt Text](pexels-cottonbro-studio-8090125.jpg)</br>
# :mag_right: Analyzing an Image using AWS Rekognition :mag:

### Objectives: Use AWS Rekognition AI to Analyze a local image in python:

1. Leverage AWS Rekognition service API to analyze local images on your computer.
2. Detect Labels within photos to include .jpg and .png files
3. Utilize AWS CLI and Python SDK boto3
4. Create an interactive GUI for our application
   
## Prerequisites:

1. AWS Account Free Tier for 12 months
2. AWS User account with Administrative Access and AWS Rekognition permissions
3. AWS SDK for Python and AWS CLI
4. Programmatic Access to AWS Service API
   
<br>![Alt Text](awsrek.png)</br>

## :eye_speech_bubble: What is AWS Rekognition?
Rekognition is an AWS API service that can automate the analysis and recognition of images and videos by using machine learning. Rekognition is a powerful tool for facial recognition, facial comparisons, content moderation, custom labels, and video segment detection to name a few. An example of a great use case for this might be if you’re creating a social media application and want a fast and easy way to moderate content on your site for offensive or inappropriate images, ads, or videos.

###<h3>Analyzing Images Using the Service</h3>

### 1. Importing Libraries:

This section imports the necessary libraries:

* _boto3_: The AWS SDK for Python that provides access to AWS services, including Amazon Rekognition.
* _tkinter_: The standard Python interface to the Tk GUI toolkit.
* _filedialog_: Part of the tkinter library, it's used for opening file dialogs.

### 2. Function to Detect Labels:


This function takes the path of an image file as an argument, initializes the Rekognition client, and uses it to detect labels in the image. It returns the list of detected labels.

### 3. Function to Analyze the Image:


This function opens a file dialog to let the user select an image. If an image is selected, it calls the detect_labels_local_file function to detect labels. It then updates the result text widget with the detected labels.

### 4. Creating the GUI:


This section creates the main GUI window using tk.Tk(). It sets the window title, creates a "Select Image" button that calls the analyze_image function when clicked, and a text widget for displaying the results.

### 5. Running the GUI:


This line starts the main loop of the GUI, which allows the user to interact with the application. The code overall provides a simple GUI for selecting an image and detecting labels in that image using Amazon Rekognition. Detected labels are displayed in the GUI.

Issues: One of the issues I faced when running the application in github actions is the loop that I have in the last line of my application would not allow for completion of the workflow. In order to resolve this for the time being I have commented this line until it can be further investigated. 

Results
The output is a list of labels from the image selected from my computer.


