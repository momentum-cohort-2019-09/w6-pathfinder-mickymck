
from PIL import Image

bg = Image.new('RGBA', (600, 600), (0, 255, 0, 255))

# bg.show()
    
def create_data_from_raw_data(elevation_list_file):
    with open (elevation_list_file) as file:
        elevation_lines = file.readlines()
        elevation_list = []
        for line in elevation_lines:
            elevation_list.append(line.split())
        print(elevation_list)

create_data_from_raw_data("elevation_small.txt")

# class Map():
#     def __init__(self, raw_file):
#         self.data = create_data_from_raw_data()
#         self.point_collection = self.create_points()


    
# # a method to transform the raw data into a list of lists
#     def create_data_from_raw_data(elevation_list_file):
#         with open (elevation_list_file) as file:
#             elevation_list = file.read().splitlines()
    
#     create_data_from_raw_data("elevation_small.txt")


# # a method to create my points and store them in a list
#     def create_points():
#         points = []
#         for datapoint in self.data:
#             # TODO - remove hard coded data after you get back into it
#             coord = (2,0)
#             elevation = 100
#             map = self
#             point = Point(coord, elevation, map)
#             points.append(point)
#         return points



    

# class Point():
#     def __init__(self, coords, elevation, map)
#         self.coords = coords
#         self.alpha = elevation_to_alpha()
#         self.map = map

#     def elevation_to_alpha(elevation):
#         max_elevation = self.map.max_elevation
#         min_elevation = self.map.min_elevation
#         elevation_range = max_elevation - min_elevation
#         return (elevation/elevation_range) * 255





# def find_max_min(elevation_list_file):

#     max_elevation = int(elevation_list[0])
#     min_elevation = int(elevation_list[0])
#     for elevation in elevation_list:
#         if int(elevation) > max_elevation:
#             max_elevation = int(elevation)
#         if int(elevation) < min_elevation:
#             min_elevation = int(elevation)
#     print(elevation_list)
#     print(max_elevation)
#     print(min_elevation)

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




