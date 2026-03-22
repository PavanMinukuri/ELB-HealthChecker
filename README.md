# ELB-HealthChecker
# ELBHealthChecker-SwetaP


## Load Balancer Health Checker (AWS Lambda + SNS)
### Objective
Design a Lambda function that checks the health of EC2 instances behind an Elastic Load Balancer (ELB).
If any instances are unhealthy, the function sends a notification via SNS (Simple Notification Service).
The function runs automatically every 10 minutes using CloudWatch Events.

##  Load Baclancer Image
<img width="1654" height="835" alt="image" src="https://github.com/user-attachments/assets/d5875216-57a8-4c2d-a9d0-664d0be7f03f" />

## Step-by-Step Guide
### 1. Create an SNS Topic
- Go to SNS in AWS Console.
- Create a Standard topic 
- Create a subscription → choose Email → enter your email.
- Confirm the subscription via the email link.
- <img width="1566" height="777" alt="image" src="https://github.com/user-attachments/assets/b39d5d39-da36-4617-b738-4ae3690205e2" />


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
-<img width="1558" height="817" alt="image" src="https://github.com/user-attachments/assets/01431305-2487-4671-9f14-9f03929f1db1" />
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
-<img width="1484" height="716" alt="image" src="https://github.com/user-attachments/assets/859a6a09-bc1f-4983-aec3-73b25508e2b6" />

# How It Works
- CloudWatch triggers the Lambda every 10 minutes.
- Lambda checks the health of EC2 instances behind the ELB.
- If any are unhealthy, Lambda sends a message to the SNS topic.
- SNS delivers the alert to my email (swetatiwari7@yahoo.com).
- <img width="1417" height="587" alt="image" src="https://github.com/user-attachments/assets/0abe69f5-916a-4fc7-a626-ba79f0af2b54" />
- <img width="895" height="309" alt="image" src="https://github.com/user-attachments/assets/f29b6384-dab3-4326-a6a8-af110a83c940" />
### lambda error Notification:
<img width="1425" height="806" alt="image" src="https://github.com/user-attachments/assets/95b471b2-7e8b-4a6f-ab3d-451476ed0c15" />


