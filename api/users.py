import api

# Variables
# accepted_fields = ["email", "firstname", "lastname", "description", "private", "access_token", "refresh_token"]
accepted_fields = ["email", "firstname", "lastname", "description", "private"]


# Public API

def get_users():
	return api.get("/users/")

def get_user(username):
	return api.get("/users/" + username)

def create_user(username, password, **fields):
	payload = api.gen_payload(fields.items(), accepted_fields)
	payload['username'] = username
	payload['password'] = password
	# return api.post("/users", payload)
	return api.authenticate(payload)

def create_user_openid():
	url = signup_openid()
	print url

	return json.dumps({
		'access_token' : raw_input("Type here the access_token:"),
		'refresh_token': raw_input("Type here the refresh_token:")
	})

def signup_openid():
	return api.authenticate()

def update_user(username, **fields):
	payload = api.gen_payload(fields.items(), accepted_fields)
	payload['username'] = username
	return api.put("/users/" + username)

def delete_user(username):
	return api.delete("/users/" + username)


# Private Functions
