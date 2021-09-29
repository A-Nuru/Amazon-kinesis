#import libraries
import base64
import json
#third party library in python to access aws
import boto3
import datetime
# define a lambda_handler function
def lambda_handler(event, context):
    
    
    try:
        #resource accessed from boto library
        dynamo_db = boto3.resource('dynamodb')
    
        ##access created dynamoDB table name "MyTable"
        table = dynamo_db.Table('MyTable')
    
    
        decoded_data =  [base64.b64decode(record["kinesis"]["data"]).decode("utf-8") for record in event["Records"]]
        print(decoded_data)
        print(json.loads(decoded_data))
        decoded_data_dic = json.loads(decoded_data)
        with table.batch_writer() as batch_writer:
            batch_writer.put_item(Item=decoded_data_dic)

    except Exception as e: 
        print(str(e))
        
   
