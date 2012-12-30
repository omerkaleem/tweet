
from django.http import HttpResponse, Http404
from django.template import Context
from django.template.loader import get_template
from django.shortcuts import render_to_response
import pymongo
from pymongo import MongoClient


##############################################################################
# this function will load the login form using login_page html page, this page
# is using the template base.html
def login(request):
  if request.path=="/validate_login/":
		return render_to_response('login_page.html',{'login_error':"the user name and password is incorrect"})
	return render_to_response('login_page.html') 
###############################login###########################################

# the following function will check if the entered user name and password on
# the login_page.html page exists in the database or not. the login_page.html
# has a form that points to this function.

def validate_login(request):
	conn=MongoClient()
	db=conn.twitter
	for user in db.users.find():	
		if user==db.users.find_one({"name":request.GET['user_name']}) and user==db.users.find_one({"password":request.GET['password']}):
			return render_to_response('home_page.html',{'user_name':request.GET['user_name']})
	
	return HttpResponse(login(request))	
#############################validate_login####################################
# this function will be used to insert tweet in the database			
def submittweet(request):
	#if request.path=="/make_new_account/":
	conn=MongoClient()
	db=conn.twitter
	db.tweet.insert({"name":request.GET['user_name'],"tweet":request.GET['tweet']})
	return HttpResponse()	
############################submit_tweet#######################################
# this function will register a new user by entering their info in the db

def make_new_account(request):
	conn=MongoClient()
	db=conn.twitter
	db.users.insert({"name":request.GET['user_name'],"password":request.GET['password'],"email":request.GET['email']})
	return render_to_response('home_page.html',{'user_name':request.GET['user_name']})	
	

############################make_new_account##################################
