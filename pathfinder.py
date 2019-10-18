
from PIL import Image

# import numpy as np

bg = Image.new('RGBA', (600, 600), (0, 255, 0, 255))

# bg.show()

class Map():
    def __init__(self, raw_file):
        self.elevation_list = self.create_data_from_raw_data(raw_file)
        self.max_elevation = self.find_max()
        self.min_elevation = self.find_min()
        self.point_collection = self.create_points()

# imports the txt file, uses readlines to create one array while keeping the lines separate, looping through each string in that list and splitting each list item in the string, so that is is an array of strings, ultimately resulting in an array of 600 arrays or 600 strings, so that each array is a new row, and each string is at a unique index—column—within its row

    def create_data_from_raw_data(self, raw_file):
        with open (raw_file) as file:
            elevation_lines = file.readlines()
            elevation_list = []
            for line in elevation_lines:
                elevation_list.append(line.split())
            return elevation_list

# discover the highest elevation, to be used in the point method to convert to alpha

    def find_max(self):
        max_elevation = int(self.elevation_list[0][0])
        for elevation_row in self.elevation_list:
            for elevation in elevation_row:
                if int(elevation) > max_elevation:
                    max_elevation = int(elevation)
        return max_elevation

# discover the lowest elevation, to be used in the point method to convert to alpha

    def find_min(self):
        min_elevation = int(self.elevation_list[0][0])
        for elevation_row in self.elevation_list:
            for elevation in elevation_row:
                if int(elevation) < min_elevation:
                    min_elevation = int(elevation)
        return min_elevation

# a method to create my points and store them in a list

    def create_points(self):
        points = []

        # read up on this enumerate method
        
        for y_pos, elevation_row in enumerate(self.elevation_list):
            for x_pos, datapoint in enumerate(elevation_row):
                coord = (x_pos, y_pos)
                points.append(coord)
        print(points)
        elevation = int(datapoint)
        map = self
        point = Point(coord, elevation, map)
        points.append(point)



    

class Point():
    def __init__(self, coords, elevation, map):
        self.coords = coords
        self.alpha = self.elevation_to_alpha(elevation)
        self.map = map

    def elevation_to_alpha(self, elevation):
        max_elevation = self.map.max_elevation
        min_elevation = self.map.min_elevation
        elevation_range = max_elevation - min_elevation
        print((elevation/elevation_range) * 255)


Map("elevation_small.txt")


# find_max_min("elevation_small.txt")

# create a Map class

# create a Point class

# Map class to-do list:
#   initialize
#   convert the raw file to data in the form I want it (a list of lists)
#   go through data to find the max and min elevations
#   convert each data point to a member of the Point class
#   draw each point

# what is passed in to create a Map?
#   raw file

# Point class to-do list:
#   initialize
#   make each Point a coordinate/alpha value pair by assigning alpha 0 to lowest elevation and alpha 255 to highest elevation

# what is passed in to create a Point?
#   - coordinate
#   - elevation

# write a method that converts elevation data into an alpha value, and then in the initializer, call that function




