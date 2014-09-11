import requests, json
from config.constants import *

# Variables

access_token  = ""
refresh_token = ""

default_headers = {
	'Content-Type': "application/json",
	'Access-Token': access_token
}


# API Functions

def get(url_resource):
	return _make("get", url_resource)

def post(url_resource, body):
	return _make("post", url_resource, body)

def put(url_resource, body):
	return _make("put", url_resource, body)

def delete(url_resource, body={}):
	return _make("delete", url_resource, body)


# Custom API Functions

def semantics_get(url):
	res  = get(url)
	data = res.json()
	file = open(SEMANTICS_FILE, 'w')
	file.write(data)
	file.close()
	return data


# Authentication and Users Creation

def authenticate():
	return requests.post(API_URL + "/users/_auth/")

def authenticate(body):
	json = post("/users/", body)
	access_token  = json['access_token']
	refresh_token = json['refresh_token']
	default_headers['Access-Token'] = access_token
	return json

def renew_tokens(access_token, refresh_token):
	headers = {
		'Access-Token' : access_token,
	  'Refresh-Token': refresh_token
	}
	url = API_URL + "/users/_renew_both_tokens"
	return requests.post(url, headers=headers).json()
	# return post(url, headers=headers)


# Auxiliary Functions

def gen_payload(fields, accepted_fields):
	payload = {}

	# TODO Be careful with nested fields
	for k, v in fields:
		if k in accepted_fields:
			payload[k] = v
		# else:
		# 	return {'error': k + " is not an accepted field"}
		# 	throw exception

	return payload


# Private Functions

def _make(method, url_resource, body={}, headers=default_headers):
	url  = API_URL + url_resource
	func = getattr(requests, method)
	res  = func(url, data=json.dumps(body), headers=headers)

	if res.status_code == STATUS_AUTHENTICATION_FAIL:
		print "renew_tokens"
		# renew_tokens()
		# res = func(url, data=json.dumps(body), headers=headers)

	# elif res.status_code == STATUS_AUTHORISATION_FAIL:
	# 	# do_something
	# print url
	return res.json()
