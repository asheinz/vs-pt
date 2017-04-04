import pytest
from src import location as Location

def test_geo_within():
    test_polygon = [[0,0],[0,1],[1,2],[2,1],[1,0]]
    test_point = [0.5, 0.5]
    false_point = [3, 3]

    test_response = Location.geo_within(test_polygon, test_point)
    false_response = Location.geo_within(test_polygon, false_point)

    assert test_response == True
    assert false_response == False