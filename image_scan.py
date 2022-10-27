from PIL import Image
from statistics import mean

# Open the FLIR image
im = Image.open("images/object_detect.png")

# Get pixel access to the image
pix = im.load()

# Set dimensions of the image
X_SIZE = im.size[0]
Y_SIZE = im.size[1]

# Ensure that a function is not trying to access out of bounds
def pixel_is_inbounds(pixel_x: int, pixel_y: int, offset_x: int, offset_y: int) -> bool:
    pass

# Create a list of coordinates that make up the yellow detections box
def make_box(box: list) -> list:
    # Scan from left to right, bottom to top
    for y_ref in range(Y_SIZE-1, 0, -1):
        for x_ref in range(X_SIZE):
            # Add yellow pixels to list: 'box'
            r, g, b = pix[x_ref, y_ref]
            if r > 190 and g > 190 and b < (.6 * r) and b < (.6 * g):
                box.append((x_ref, y_ref))

    return box

# Average corners
def corner_average(pair, corners, useful_corners):
    x_coords = []
    y_coords = []
    x, y = pair
    for corner in corners:
        corner_x, corner_y = corner
        if abs(corner_x - x) < 4 and abs(corner_y - y) < 4:
            x_coords.append(corner_x)
            y_coords.append(corner_y)
        print(x_coords, y_coords)
    useful_corners.append((round(mean(x_coords)), round(mean(y_coords))))
    return useful_corners

# Create a list of coordinates for pixels in the bottom corners of the detected boxes
def find_corners(box: list, corners:list) -> list:
    for coordinate in box:
        x, y = coordinate
        # TODO: Check for inbounds
        offsets = [5, 6, 7, 8]
        for offset in offsets:
            # Checks that the pixel is in bottom corners based on surrounding yellow pixels
            if (x, y - offset) in box and (((x - offset, y) in box) or ((x + offset, y) in box)):
                pix[x, y] = (255, 0, 0)             
                corners.append(coordinate)
    
    return corners

# Group corner pixels together
def get_ref_points(corners: list, ref_points: list) -> list:
    for idx, coordinate in enumerate(corners):
        x, y = coordinate
        for num in range(idx + 1, len(corners)):
            x_2, y_2 = corners[num]               
            if (x_2 < (x - 10) or x_2 > (x + 10)) and (y_2 >= (y - 2) and y_2 <= (y + 2)):
                if (coordinate, (x_2, y_2)) not in ref_points:
                    ref_points.append((coordinate, (x_2, y_2)))
                    pix[x, y] = (0, 0, 255)
    
    return ref_points

def neighbor_present(bogeys: list, point: tuple) -> bool:
    x, y = point
    
    if not bogeys:
        return False

    for bogey in bogeys:
        coord_x, coord_y = bogey
        if abs(coord_x - x) < 5 and abs(coord_y - y) < 5:
            return True
    
    return False

# Main
box = make_box([])
corners = find_corners(box, [])
ref_points = get_ref_points(corners, [])

bogeys = []
for pair in ref_points:
    first_point, second_point = pair
    first_x, first_y = first_point
    second_x, second_y = second_point

    midpoint = (round((first_x + second_x) / 2), round((first_y + second_y) / 2))

    if not neighbor_present(bogeys, midpoint):
        pix[midpoint[0], midpoint[1]] = (255, 0, 255)
        bogeys.append(midpoint)


print(bogeys)
im.save("new.png")