# celery_django
1. Install dependencies like celery, celery-beat
2. specify SQS in the broker URL  broker_url = 'sqs://aws_access_key_id:aws_secret_access_key@'                    
3. Configure the broker_transport_options setting:                                                                       
 BROKER_TRANSPORT_OPTIONS = {
    'region': 'region name',
    'visibility_timeout': 60,  # 1 minutes
    'polling_interval': 5,     # 5 seconds
    'queue_name_prefix': 'sqs-celery-example-'
}                                                                                                                                                                                                      4.  specify the task and schedule in app.conf.beat_schedule  
