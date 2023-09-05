import json
import sagemaker
import base64
from sagemaker.serializers import IdentitySerializer

# Fill this in with the name of your deployed model
ENDPOINT = 'image-classification-2023-09-05-14-18-41-991'

def lambda_handler(event, context):

    event = event['body']
    # Decode the image data
    image = base64.b64decode(event['image_data'])

    # Instantiate a Predictor
    session = sagemaker.session.Session()
    predictor = sagemaker.predictor.Predictor(ENDPOINT, session)

    # For this model the IdentitySerializer needs to be "image/png"
    predictor.serializer = IdentitySerializer("image/png")
    
    # Make a prediction:
    inferences = predictor.predict(image)
    
    # We return the data back to the Step Function    
    event["inferences"] = inferences.decode('utf-8')
    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }