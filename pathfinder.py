
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
        bg.save("map.png")





class Path():
    def __init__(self, map):
        self.map = map
        self.path = self.collect_path_points()
        self.path_crumbs = self.draw_path(self.path)

    def collect_path_points(self):

        # list of coordinates for each step on my path

        path_points = []

        # the change in elevation for each step I take, which will be needed to discover the most efficient path

        elevation_change = []

        # hardcoded starting points, to be replaced with a random starting point
        
        x_pos = 0
        y_pos = 360

        # current elevation, needed to determine which step to take next
        
        current_elev = int(self.map.elevation_list[y_pos][x_pos])

        # add my first coord to my coord list
        
        path_points.append((x_pos, y_pos))

        # let's replace my hardcoded start point with a list of all start points

        while x_pos < 599:

            # defining my three potential steps
        

            if y_pos == 0:

                step_ahead = abs(current_elev - int(self.map.elevation_list[y_pos][x_pos + 1]))
                step_down = abs(current_elev - int(self.map.elevation_list[y_pos + 1][x_pos + 1]))

                if step_ahead <= step_down:
                    x_pos += 1
                    path_points.append((x_pos, y_pos))
                    elevation_change.append(step_ahead)
                else:
                    x_pos += 1
                    y_pos += 1
                    path_points.append((x_pos, y_pos))
                    elevation_change.append(step_down)

            if y_pos == 599:

                step_up = abs(current_elev - int(self.map.elevation_list[y_pos - 1][x_pos + 1]))
                step_ahead = abs(current_elev - int(self.map.elevation_list[y_pos][x_pos + 1]))

                if step_up <= step_ahead:
                    x_pos += 1
                    y_pos -= 1
                    path_points.append((x_pos, y_pos))
                    elevation_change.append(step_up)
                else:
                    x_pos += 1
                    path_points.append((x_pos, y_pos))
                    elevation_change.append(step_ahead)

            else:

                step_up = abs(current_elev - int(self.map.elevation_list[y_pos - 1][x_pos + 1]))
                step_ahead = abs(current_elev - int(self.map.elevation_list[y_pos][x_pos + 1]))
                step_down = abs(current_elev - int(self.map.elevation_list[y_pos + 1][x_pos + 1]))

            # deciding which of the three potential steps to take, and adding my new coord and elevation to the coord and elevation lists
            
                if step_up <= step_ahead and step_up <= step_down:
                    x_pos += 1
                    y_pos -= 1
                    path_points.append((x_pos, y_pos))
                    elevation_change.append(step_up)
                if step_ahead <= step_up and step_ahead <= step_down:
                    x_pos += 1
                    path_points.append((x_pos, y_pos))
                    elevation_change.append(step_ahead)
                if step_down <= step_up and step_down <= step_ahead:
                    x_pos += 1
                    y_pos += 1
                    path_points.append((x_pos, y_pos))
                    elevation_change.append(step_down)

        return path_points

    # drawing the path on top of my map
    
    def draw_path(self, points):
        rendered_map = Image.open("map.png")
        for point in points:
            rendered_map.putpixel((point), (0, 0, 255, 255))
        rendered_map.show()





if __name__ == "__main__":
    map = Map("elevation_small.txt")
    path = Path(map)
