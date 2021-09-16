#import libraries
import base64
import json
#third party library in python to access aws
import boto3
import datetime
# define a lambda_handler function
def lambda_handler(event, context):
    
    
    #resource accessed from boto library
    dynamo_db = boto3.resource('dynamodb')
    
    ##access created dynamoDB table name "MyTable"
    table = dynamo_db.Table('MyTable')
        
   
