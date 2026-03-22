import boto3
import os

def lambda_handler(event, context):
    # Read environment variables
    elb_name = os.environ['ELB_NAME']
    sns_topic_arn = os.environ['SNS_TOPIC_ARN']

    # Create AWS clients
    elb_client = boto3.client('elb')
    sns_client = boto3.client('sns')

    # Get instance health from ELB
    response = elb_client.describe_instance_health(LoadBalancerName=elb_name)
    instance_states = response['InstanceStates']

    # Collect unhealthy instances
    unhealthy = [i['InstanceId'] for i in instance_states if i['State'] != 'InService']

    # If any unhealthy, publish to SNS
    if unhealthy:
        message = f"Unhealthy instances detected in ELB {elb_name}: {', '.join(unhealthy)}"
        sns_client.publish(
            TopicArn=sns_topic_arn,
            Subject="ELB Health Alert",
            Message=message
        )
        return {"status": "alert_sent", "details": message}
    else:
        return {"status
