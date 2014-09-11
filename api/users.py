import api

# Variables
accepted_fields = ["username", "password", "email", "firstname", "lastname", "description", "private"]


# Public API

def get_all():
	return api.get("/users/")['users']

def get(username):
	return api.get("/users/" + username)

def update(username, **fields):
	payload = api.gen_payload(fields.items(), accepted_fields)
	# payload['username'] = username
	return api.put("/users/" + username, payload)

def remove(username):
	return api.delete("/users/" + username)

# def create(data):
# 	payload = api.gen_payload(data, accepted_fields)
# 	# if payload['error']: return payload['error']
# 	api.authenticate(payload)
# 	return get(payload['username'])

# def create(username, password, **fields):
# 	data = fields.items()
# 	data['username'] = username
# 	data['password'] = password
# 	return create(data)

def create(username, password, **fields):
	# data = fields.items()
	fields['username'] = username
	fields['password'] = password
	payload = api.gen_payload(fields.items(), accepted_fields)
	# if payload['error']: return payload['error']
	api.authenticate(payload)
	return get(payload['username'])

# TODO Test this function and improve if necessary
def create_openid():
	url = api.authenticate()
	print "Open the next URL on your browser:"
	print url

	return json.dumps({
		'access_token' : raw_input("Type here the access_token:"),
		'refresh_token': raw_input("Type here the refresh_token:")
	})


# Private Functions
