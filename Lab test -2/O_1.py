"""
Ray-Casting Point-in-Polygon Algorithm for Agritech Geofencing

This implementation uses the ray-casting algorithm to determine if points lie within
polygonal regions. Points on edges are treated as inside the polygon.

Algorithm Overview:
1. Cast a ray from the point horizontally to the right (positive x-direction)
2. Count the number of times the ray intersects with polygon edges
3. If the count is odd, the point is inside; if even, it's outside
4. Special handling for points on edges (counted as inside)

Edge Cases Handled:
- Points exactly on polygon edges
- Horizontal edges (no intersection)
- Vertical edges (proper intersection counting)
- Points at polygon vertices
"""

from typing import List

def point_in_polygon(poly, pts) -> List[bool]:
    """
    Determine if points lie within a polygon using ray-casting algorithm.
    
    Args:
        poly: List of (x, y) tuples representing polygon vertices in order
        pts: List of (x, y) tuples representing query points
        
    Returns:
        List[bool]: Boolean values indicating if each point is inside the polygon
    """
    if not poly or len(poly) < 3:
        return [False] * len(pts)
    
    result = []
    
    for px, py in pts:
        is_inside = False
        n = len(poly)
        
        # Cast ray from point to the right
        for i in range(n):
            x1, y1 = poly[i]
            x2, y2 = poly[(i + 1) % n]
            
            # Check if point is on the current edge
            if is_point_on_edge(px, py, x1, y1, x2, y2):
                is_inside = True
                break
            
            # Check for ray intersection with edge
            if ray_intersects_edge(px, py, x1, y1, x2, y2):
                is_inside = not is_inside
        
        result.append(is_inside)
    
    return result


def is_point_on_edge(px, py, x1, y1, x2, y2):
    """
    Check if a point lies exactly on an edge.
    
    Args:
        px, py: Point coordinates
        x1, y1, x2, y2: Edge coordinates
        
    Returns:
        bool: True if point is on the edge
    """
    # Handle vertical edges
    if x1 == x2:
        return px == x1 and min(y1, y2) <= py <= max(y1, y2)
    
    # Handle horizontal edges
    if y1 == y2:
        return py == y1 and min(x1, x2) <= px <= max(x1, x2)
    
    # Handle diagonal edges using cross product
    # Point is on line if cross product is 0 and point is within edge bounds
    cross_product = (px - x1) * (y2 - y1) - (py - y1) * (x2 - x1)
    
    if abs(cross_product) > 1e-10:  # Not on the line
        return False
    
    # Check if point is within the edge bounds
    return (min(x1, x2) <= px <= max(x1, x2) and 
            min(y1, y2) <= py <= max(y1, y2))


def ray_intersects_edge(px, py, x1, y1, x2, y2):
    """
    Check if a horizontal ray from the point intersects with an edge.
    
    Args:
        px, py: Point coordinates
        x1, y1, x2, y2: Edge coordinates
        
    Returns:
        bool: True if ray intersects the edge
    """
    # Ray is horizontal, so we only consider edges that cross the ray's y-level
    if y1 == y2:  # Horizontal edge - no intersection
        return False
    
    # Check if edge crosses the horizontal line at py
    if not (min(y1, y2) < py < max(y1, y2)):
        return False
    
    # Calculate x-coordinate of intersection
    if x1 == x2:  # Vertical edge
        intersection_x = x1
    else:
        # Linear interpolation
        t = (py - y1) / (y2 - y1)
        intersection_x = x1 + t * (x2 - x1)
    
    # Ray goes to the right, so intersection must be to the right of the point
    return intersection_x > px


def parse_input():
    """Parse input in the format: poly=[(0,0),(4,0),(4,4),(0,4)], pts=[(2,2),(5,5)]"""
    print("Enter input in format: poly=[(x1,y1),(x2,y2),...], pts=[(px1,py1),(px2,py2),...]")
    print("Example: poly=[(0,0),(4,0),(4,4),(0,4)], pts=[(2,2),(5,5)]")
    
    user_input = input().strip()
    
    try:
        # Find the poly and pts sections
        poly_start = user_input.find('poly=[')
        pts_start = user_input.find('pts=[')
        
        if poly_start == -1 or pts_start == -1:
            raise ValueError("Missing poly= or pts= in input")
        
        # Extract polygon coordinates
        poly_end = user_input.find(']', poly_start)
        poly_str = user_input[poly_start + 6:poly_end]  # Skip 'poly=['
        
        # Parse polygon coordinates
        poly_coords = []
        # Split by '),(' to get individual coordinate pairs
        coord_pairs = poly_str.split('),(')
        for i, pair in enumerate(coord_pairs):
            # Clean up parentheses
            pair = pair.replace('(', '').replace(')', '')
            if pair.strip():
                x, y = map(float, pair.split(','))
                poly_coords.append((x, y))
        
        # Extract points coordinates
        pts_end = user_input.find(']', pts_start)
        pts_str = user_input[pts_start + 5:pts_end]  # Skip 'pts=['
        
        # Parse points coordinates
        pts_coords = []
        coord_pairs = pts_str.split('),(')
        for pair in coord_pairs:
            pair = pair.replace('(', '').replace(')', '')
            if pair.strip():
                x, y = map(float, pair.split(','))
                pts_coords.append((x, y))
        
        return poly_coords, pts_coords
        
    except (ValueError, IndexError) as e:
        print(f"Invalid input format: {e}")
        print("Using default values...")
        return [(0, 0), (4, 0), (4, 4), (0, 4)], [(2, 2), (5, 5)]


if __name__ == "__main__":
    print("=== Ray-Casting Point-in-Polygon Algorithm for Agritech Geofencing ===\n")
    
    # Get input from user in the specified format
    poly, pts = parse_input()
    
    # Calculate results
    result = point_in_polygon(poly, pts)
    
    # Display results in the exact format requested
    print(f"\nInput")
    print(f"poly={poly}, pts={pts}")
    print(f"\nOutput")
    print(f"{result}")
    print(f"\nAcceptance Criteria: Edges counted as inside")
    

   

