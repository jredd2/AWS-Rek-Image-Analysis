# The main point of this code is to show how to call the Computer Vision API from Python

import boto3

def initialize_rekognition_client():
    # Initialize the AWS Rekognition client with your AWS credentials.
    # Make sure your AWS credentials are configured using AWS CLI or environment variables.
    rekognition = boto3.client('rekognition', region_name='us-east-1')
    return rekognition

def analyze_local_image(rekognition, image_path):
    try:
        with open(image_path, 'rb') as image_file:
            # Use the detect_labels API to analyze the image and detect labels.
            response = rekognition.detect_labels(
                Image={
                    'Bytes': image_file.read()
                },
                MaxLabel=10,
                MinConfidence=75,
                Features=[
                    'GENERAL_LABELS',
                    'IMAGE_PROPERTIES',
                ],
                Settings={
                    'General Labels': {
                        'LabelInclusionFilters': [
                            'Human','Car','Person',
                        ],
                        'LabelExclusionFilters':[
                            'Clothing',
                        ],
                        'LabelCategoryInclusionFilters':[
                            'Animal and Pets',
                        ],
                        'LabelCategoryExclusionFilters':[
                            'Outdoors',
                        ]
                    },
                    'ImageProperties':{
                        'MaxDominantColors': 10
                    }
                }
            )
            print(response)
            # Display moderation labels
            print("Image Properties for {}: ".format(image_path))
            for label in response['ModerationLabels']:
                print("- {} (Confidence: {}%)".format(label['Name'], label['Confidence']))

    except Exception as e:
        print("Error analyzing the image: {}".format(e))

if __name__ == "__main__":
    # Initialize the Rekognition client
    rekognition = initialize_rekognition_client()

    # List of local image paths to analyze
    image_paths = ["/Users/jessiereddjr./Documents/Docker-Logo-2013.png"]  # Add your image file paths here

    for image_path in image_paths:
        analyze_local_image(rekognition, image_path)
