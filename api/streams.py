import api

# Variables
accepted_fields = ["name, description", "type", "tags", "private", "unit", "accuracy",
	"min_val", "max_val", "polling", "uri", "polling_freq", "location", "parser", "data_type",
	"resource", "resource.resource_type", "resource.uuid", "location.lon", "location.lat"]


# Public API

def get_streams():
	return api.get("/streams/")

def get_stream(id):
	return api.get("/streams/" + id)

def get_streams_ids_from_query(query):
	pass

def create_stream(name, **fields):
	payload = api.gen_payload(fields.items(), accepted_fields)
	payload['name'] = name
	payload['user_id'] = user_id
	return api.post("/streams", payload)

def create_streams_from_resource(resource_id):
	res = api.get("/resources/" + resource_id)
	# streams = []
	# for s in res["streams"]:
	# 	streams.push(s)
	return res

def update_stream(id, **fields):
	payload = api.gen_payload(fields.items(), accepted_fields)
	payload['id'] = id
	payload['user_id'] = user_id
	return api.put("/streams", payload)

def delete_stream(id):
	return api.delete("/streams/" + id)

def subscribe(stream_id, callback):
	pass


# Private Functions
