import api

# Variables
# accepted_fields = ["email", "firstname", "lastname", "description", "private", "access_token", "refresh_token"]
accepted_fields = ["username", "password", "email", "firstname", "lastname", "description", "private"]


# Public API

def get_all():
	return api.get("/users/")

def get(username):
	return api.get("/users/" + username)

def create(data):
	payload = api.gen_payload(data, accepted_fields)
	# if payload['error']: return payload['error']
	return api.authenticate(payload)

def create(username, password, **fields):
	data = fields.items()
	data['username'] = username
	data['password'] = password
	return create(data)

def create_openid():
	url = signup_openid()
	print url

	return json.dumps({
		'access_token' : raw_input("Type here the access_token:"),
		'refresh_token': raw_input("Type here the refresh_token:")
	})

def signup_openid():
	return api.authenticate()

def update(username, **fields):
	payload = api.gen_payload(fields.items(), accepted_fields)
	payload['username'] = username
	return api.put("/users/" + username)

def remove(username):
	return api.delete("/users/" + username)


# Private Functions
