import math

def find_distance(p1, p2):
    return math.hypot(p2[0] - p1[0], p2[1] - p1[1])

def get_distance(point_list):
    """Get distance between two points"""
    if len(point_list) >= 2:
        return math.hypot(point_list[1][0] - point_list[0][0], 
                         point_list[1][1] - point_list[0][1])
    return 0

def get_angle(a, b, c):
    """Get angle between three points"""
    import math
    ax, ay = a[0] - b[0], a[1] - b[1]
    cx, cy = c[0] - b[0], c[1] - b[1]
    
    dot_product = ax * cx + ay * cy
    magnitude_a = math.sqrt(ax**2 + ay**2)
    magnitude_c = math.sqrt(cx**2 + cy**2)
    
    if magnitude_a == 0 or magnitude_c == 0:
        return 0
    
    cos_angle = dot_product / (magnitude_a * magnitude_c)
    cos_angle = max(-1, min(1, cos_angle))
    angle = math.acos(cos_angle)
    
    return math.degrees(angle)
