import json


THRESHOLD = .8


def lambda_handler(event, context):
    # Getting outputs from last task
    event = json.loads(event["body"])
    # Grab the inferences from the event
    inferences = eval(event['inferences'])
    
    # Check if any values in our inferences are above THRESHOLD
    meets_threshold = any(prob >= THRESHOLD for prob in inferences)
    
    # If our threshold is met, pass our data back out of the
    # Step Function, else, end the Step Function with an error
    if meets_threshold:
        pass
    else:
        raise("THRESHOLD_CONFIDENCE_NOT_MET")

    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }