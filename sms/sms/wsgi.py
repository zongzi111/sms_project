'''
Author: Zongzi haolin1021@gmail.com
Date: 2022-12-16 11:17:47
LastEditors: Zongzi haolin1021@gmail.com
LastEditTime: 2022-12-16 11:28:31
FilePath: /sms_project/sms/sms/wsgi.py
Description: 
'''
"""
WSGI config for sms project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sms.settings.develop')

application = get_wsgi_application()
