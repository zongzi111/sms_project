'''
Author: Zongzi haolin1021@gmail.com
Date: 2022-12-16 11:28:08
LastEditors: Zongzi haolin1021@gmail.com
LastEditTime: 2022-12-16 11:31:06
FilePath: /sms_project/sms/sms/settings/settings copy.py
Description: 
'''

from .base import * # NOQA

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True