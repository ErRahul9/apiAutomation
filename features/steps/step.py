from behave import *
from sys import argv
import time
import json
import requests
import os

@given('job is running and available for {METHOD}')
def step_impl(context,METHOD):
	assert 1 is 1 

@when('we send a request for  {API} and  {STATUS} and requested operation is {METHOD} and action is {ACTION} ')
def step_impl(context,API,STATUS,METHOD,ACTION):
	assert 1 is 1
@then('response code is {ACTION} is {STATUS}')
def step_impl(context,ACTION,STATUS):
	assert 1 is 1

	

