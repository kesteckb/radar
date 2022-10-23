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

# Create a list of coordinates for pixels in the bottom corners of the detected boxes
def find_corners(box: list, corners:list) -> list:
    for coordinate in box:
        x, y = coordinate
        # TODO: Check for inbounds
        offsets = [5, 7]
        for offset in offsets:
            # Checks that the pixel is in bottom corners based on surrounding yellow pixels
            if (x, y - offset) in box and (((x - offset, y) in box) or ((x + offset, y) in box)):
                pix[x, y] = (255, 0, 0)
                corners.append(coordinate)
    
    return corners

# Group corner pixels together
def get_ref_points(corners, ref_points):
    for idx, coordinate in enumerate(corners):
        x, y = coordinate
        for num in range(idx + 1, len(corners)):
            x_2, y_2 = corners[num]               
            if (x_2 < (x - 10) or x_2 > (x + 10)) and (y_2 >= (y - 1) and y_2 <= (y + 1)):
                if (coordinate, (x_2, y_2)) not in ref_points:
                    ref_points.append((coordinate, (x_2, y_2)))
                    pix[x, y] = (0, 0, 255)
    
    return ref_points



# Main
box = make_box([])
corners = find_corners(box, [])
ref_points = get_ref_points(corners, [])
im.save("new.png")
    
    