import boto3
import requests
from acquisition import camera
import time 

bucket='rekognition-raizen'
photo='image.jpg'
s3 = boto3.resource('s3')
WAIT_TIME = 10

def tell_db(payload):
    return

def is_plate(text):
    if len(text) == 8 and text[3] == '-':
        return True
    
    return False

while True:
    webcam = camera.init_camera()
    for i in range(2):
        camera.save_ss(webcam, filename)
        time.sleep(1)
    camera.stop_camera(webcam)

    data = open(photo, 'rb')
    s3.Bucket(bucket).put_object(Key=photo, Body=data)

    client=boto3.client('rekognition', region_name='us-east-1')

    response=client.detect_text(Image={'S3Object':{'Bucket':bucket,'Name':photo}})    
    textDetections=response['TextDetections']
    for text in textDetections:
        if text['Confidence'] > 0.9 and is_plate(text['DetectedText']):
            tell_db(text['DetectedText'])

    time.sleep(WAIT_TIME)