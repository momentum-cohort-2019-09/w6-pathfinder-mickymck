
from PIL import Image

class Map():
    def __init__(self, raw_file):
        self.elevation_list = self.create_data_from_raw_data(raw_file)
        self.max_elevation = self.find_max()
        self.min_elevation = self.find_min()
        self.alpha_list = self.elevation_to_alpha(self.elevation_list)
        self.map_drawing = self.create_map(self.elevation_list, self.alpha_list)

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

# transforms my elevations into their relative alpha values

    def elevation_to_alpha(self, elevation_list):
        alpha_list = []
        for elevation_row in self.elevation_list:
            for datapoint in elevation_row:
                alpha_value = int(datapoint)
                alpha_list.append(round(((alpha_value - self.min_elevation) / (self.max_elevation - self.min_elevation)) * 255))
        return alpha_list

# combined my create_point and my draw_map methods into one method, which collects my x and y coords, and uses them to map out my elevation values

    def create_map(self, elevation_list, alpha_list):
        points = []
        bg = Image.new('RGBA', (600, 600), (0, 0, 0, 255))
        map = Image.new('RGBA', (600, 600), (0, 0, 0, 255))
        for y_pos, elevation_row in enumerate(self.elevation_list):
            for x_pos, datapoint in enumerate(elevation_row):
                map.putpixel((x_pos, y_pos), (255, 255, 255, self.alpha_list[int(datapoint)]))
        bg.paste(map, (0,0), map)
        # bg.show()





class Path():
    def __init__(self, map):
        self.map = map
        self.path_points = self.collect_path_points()

    def collect_path_points(self):
        # list of coordinates for each step on my path
        path_points = []

        # list of elevations for each step on my path
        elevations = []

        # the change in elevation for each step I take, which will be needed to discover the most efficient path
        elevation_change = []

        # hardcoded starting points, to be replaced with a random starting point
        x_pos = 0
        y_pos = 200

        # add my first elevation to my elevation list
        elevations.append(self.map.elevation_list[y_pos][x_pos])

        # add my first coord to my coord list
        path_points.append((x_pos, y_pos))

        # current elevation, needed to determine which step to take next
        current_elev = int(elevations[-1])

        # # current x position, to track when I've hit the end of the map
        # current_x = [x_pos]
        # print(current_x[-1])

        # defining my three potential steps
        step_N = abs(current_elev - int(self.map.elevation_list[y_pos - 1][x_pos + 1]))
        step_E = abs(current_elev - int(self.map.elevation_list[y_pos][x_pos + 1]))
        step_S = abs(current_elev - int(self.map.elevation_list[y_pos + 1][x_pos + 1]))

        # deciding which of the three potential steps to take, and adding my new coord and elevation to the coord and elevation lists
        while x_pos < 600:
            if step_N <= step_E and step_N <= step_S:
                path_points.append((x_pos + 1, y_pos - 1))
                elevation_change.append(step_N)
                x_pos += 1
                y_pos -= 1
            if step_E <= step_N and step_E <= step_S:
                path_points.append((x_pos + 1, y_pos))
                elevation_change.append(step_E)
                x_pos += 1
            if step_S <= step_N and step_S <= step_E:
                path_points.append((x_pos + 1, y_pos + 1))
                elevation_change.append(step_S)
                x_pos += 1
                y_pos += 1

        print(path_points)

# pick a starting point on the west side of the map (hardcode 0, 299 for now)

# add that coordinate to a list

# take a step forword to 1, and either 299, 300, or 301 (depending on elevation change)

# for each step I take, collect the coordinates and store them in a list

# continue until I reach the east end of the map

# color each set of coordinates in my list to be blue, and add it to the map
    


# class Point():
#     def __init__(self, coords, elevation):
#         self.coords = coords

# Map("elevation_small.txt")

if __name__ == "__main__":
    map = Map("elevation_small.txt")
    path = Path(map)
