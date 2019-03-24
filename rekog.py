import boto3

if __name__ == "__main__":

    bucket='rekognition-raizen'
    photo='image.jpg'
    
    s3 = boto3.resource('s3')
    data = open(photo, 'rb')
    s3.Bucket(bucket).put_object(Key=photo, Body=data)

    client=boto3.client('rekognition', region_name='us-east-1')

  
    response=client.detect_text(Image={'S3Object':{'Bucket':bucket,'Name':photo}})

                        
    textDetections=response['TextDetections']
    print response
    print 'Detected text'
    for text in textDetections:
            print 'Detected text:' + text['DetectedText']
            print 'Confidence: ' + "{:.2f}".format(text['Confidence']) + "%"
            print 'Id: {}'.format(text['Id'])
            if 'ParentId' in text:
                print 'Parent Id: {}'.format(text['ParentId'])
            print 'Type:' + text['Type']
            print

