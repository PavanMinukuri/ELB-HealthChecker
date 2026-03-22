# ELB-HealthChecker
# ELBHealthChecker


## Load Balancer Health Checker (AWS Lambda + SNS)
### Objective
Design a Lambda function that checks the health of EC2 instances behind an Elastic Load Balancer (ELB).
If any instances are unhealthy, the function sends a notification via SNS (Simple Notification Service).
The function runs automatically every 10 minutes using CloudWatch Events.

##  Load Baclancer Image
<img width="1112" height="566" alt="image" src="https://github.com/user-attachments/assets/fb6e0fc2-e72a-4740-a83b-daa3480d3159" />




## Step-by-Step Guide
### 1. Create an SNS Topic
- Go to SNS in AWS Console.
- Create a Standard topic 
- Create a subscription → choose Email → enter your email.
- Confirm the subscription via the email link.
- <img width="1778" height="747" alt="image" src="https://github.com/user-attachments/assets/3d710c2b-35e5-41a5-912d-0a89fc9b3bf1" />



### 2. Create a Lambda Function
- Go to Lambda → Create function.
- Choose Author from scratch.
- Name: ELBHealthChecker.
- Runtime: Python 3.14
- Create the function.
-<img width="1487" height="493" alt="image" src="https://github.com/user-attachments/assets/25cc19fe-4404-4f95-9b0b-be2c29a22fb9" />

## 3. Add IAM Role Permissions
- Go to IAM → Roles.
- Create a role with:
- Elastic Load Balancing ReadOnly policy.
- AmazonSNSFullAccess policy.
- Attach this role to your Lambda function.
-<img width="1143" height="561" alt="image" src="https://github.com/user-attachments/assets/b6f8f497-acb9-4158-b996-fd2e6c28e182" />

-<img width="1564" height="711" alt="image" src="https://github.com/user-attachments/assets/9a4f4761-ca16-4cda-9140-0c9da4b492e8" />


## 4. Add Environment Variables
In Lambda → Configuration → Environment variables:
- ELB_NAME → your load balancer name.
- SNS_TOPIC_ARN → ARN of the SNS topic you created.

## 5. Python Code (lambda_function.py)
### Added in the lambda_function.py file in the repo itself.

## 6. Schedule with CloudWatch
- Go to CloudWatch → Rules → Create rule.
- Choose Schedule → Fixed rate of 10 minutes.
- Target → your Lambda function.
-<img width="1546" height="573" alt="image" src="https://github.com/user-attachments/assets/3f438608-61cf-40d6-99de-5ede071431d5" />
-<img width="1214" height="571" alt="image" src="https://github.com/user-attachments/assets/ac062046-f8e1-4c18-91bf-847b7f12428a" />


# How It Works
- CloudWatch triggers the Lambda every 10 minutes.
- Lambda checks the health of EC2 instances behind the ELB.
- If any are unhealthy, Lambda sends a message to the SNS topic.



