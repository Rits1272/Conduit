'''
This is a simple exception. In Django REST Framework,
any time you want to create a custom exception, you 
inherit from APIException. All you have to do then is 
specify the default_detail and status_code properties. 
'''
from rest_framework.exceptions import APIException

class ProfileDoesNotExist(APIException):
    status_code = 400
    default_detail = 'The requested profile does not exist.'