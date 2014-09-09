import requests, json
import constants as C

# Variables
access_token  = ""
refresh_token = ""


# API Functions

def get(url_resource):
	_make("get", url_resource)

def post(url_resource, body):
	_make("post", url_resource, body)

def put(url_resource, body):
	_make("put", url_resource, body)

def delete(url_resource, body=body):
	_make("delete", url_resource, body)

def gen_payload(fields, accepted_fields):
	payload = {}

	# TODO Be careful with nested fields
	for k, v in fields:
		if k in accepted_fields:
			payload[k] = v

	return payload

def authenticate():
	return requests.post(C.API_URL + "/users/_auth/")

def renew_tokens(access_token, refresh_token):
	headers = {
		'Access-Token' : access_token,
	  'Refresh-Token': refresh_token
	}
	url = C.API_URL + "/users/_renew_both_tokens"
	return requests.post(url, headers=headers).json()
	# return post(url, headers=headers)

def semantics_get(url):
	res  = get(url)
	data = res.json()
	file = open(C.SEMANTICS_FILE, 'w')
	file.write(data)
	file.close()
	return data


# Private Functions

def _make(method, url_resource, body=body, headers=headers):
	if not headers:
		headers = {
			'Content-Type': 'application/json',
			'Access-Token': access_token
		}

	url = C.API_URL + url_resource
	api_func = requests[method]
	res = api_func(url, data=json.dumps(body), headers=headers)

	if res.status_code == C.STATUS_AUTHENTICATION_FILE:
		print "renew_tokens"
		# renew_tokens()
		# res = api_func(url, data=json.dumps(body), headers=headers)

	# elif res.status_code == C.STATUS_AUTHORISATION_FILE:
	# 	# do_something

	return res.json()

