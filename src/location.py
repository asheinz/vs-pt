from flask import request, make_response, jsonify
import data as DATA
import json
import matplotlib.path as mplPath

def post_location():
    lon = float(request.form.get('longitude'))
    lat = float(request.form.get('latitude'))

    data = check_location(lon, lat)

    return jsonify(data)

def check_location(lon, lat):
    """Receives a request
    """
    data = query_data()

    states = [
        i['state'] for i in data 
                if geo_within([[float(c) for c in p] for p in i['border']], 
                              [lon, lat]
        )
    ]

    return states

def query_data():
    """Requests data from our json file.
    returns: an array of objects
    """
    # Note, the json file isn't interpreted as a proper json file (array 
    # with objects/dicts seperated by commas)
    loc = './data/states.json'
    
    data = [json.loads(line.rstrip('\n')) for line in open(loc)]
    
    return data

def geo_within(polygon, point):
    """Checks to see if a point is within a polygon.
    
    args:
     -  polygon: a list of points describing a polygon
     -  point: a list of coordinates ([lon, lat])
    returns: a bool (True if the point is within the polygon, or False)
    """
    bbPath = mplPath.Path(polygon)
    return bbPath.contains_point(point)