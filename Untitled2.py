#!/usr/bin/env python
# coding: utf-8

# In[2]:


# imports boto3
import boto3
# get the service resource
sqs = boto3.resource('sqs')


# In[3]:


# create the queue. This returns an SQS.Queue instance
queue = sqs.create_queue(QueueName='test-asmithfk', Attributes={'DelaySeconds': '5'})


# In[4]:


# You can now access identifiers and attributes
print(queue.url)
print(queue.attributes.get('DelaySeconds'))


# In[ ]:




