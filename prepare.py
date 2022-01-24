import json

file_path = 'start_points_sample.txt'

def geojson_loader():
	with open(file_path) as f:
	    json_content = json.load(f)

	return json_content

if __name__ == '__main__':
	a = geojson_loader()
	print(type(a))