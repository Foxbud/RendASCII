"""
TBA.
"""


from rendascii.geometry import X, Y


def generate_aabb(poly):
  bound_min_x = None
  bound_min_y = None
  bound_max_x = None
  bound_max_y = None

  for vertex in poly:
    if bound_min_x is None or vertex[X] < bound_min_x:
      bound_min_x = vertex[X]
    if bound_min_y is None or vertex[Y] < bound_min_y:
      bound_min_y = vertex[Y]
    if bound_max_x is None or vertex[X] > bound_max_x:
      bound_max_x = vertex[X]
    if bound_max_y is None or vertex[Y] > bound_max_y:
      bound_max_y = vertex[Y]

  return (
      (bound_min_x, bound_min_y,),
      (bound_max_x, bound_max_y,),
      )


def aabb_contains_point(aabb, point):
  return (
      aabb[0][X] < point[X] < aabb[1][X]
      and aabb[0][Y] < point[Y] < aabb[1][Y]
      )


def poly_contains_point(poly, point):
  start = _edge(point, poly[-1], poly[0]) < 0
  for i in range(len(poly) - 1):
    if (_edge(point, poly[i], poly[i + 1]) <= 0) != start:
      return False
  return True


def interpolate_attribute(poly, attributes, point):
  v0 = poly[0]
  v1 = poly[1]
  v2 = poly[2]

  # Calculate baycentric weights.
  area_t = _double_area(v0, v1, v2)
  w0 = _double_area(point, v1, v2) / area_t
  w1 = _double_area(point, v2, v0) / area_t
  w2 = _double_area(point, v0, v1) / area_t

  return (
      w0 * attributes[0]
      + w1 * attributes[1]
      + w2 * attributes[2]
      )


def _edge(vec, line_s, line_e):
  # Check which side of line a vector lies on (sign).
  return (
      (vec[X] - line_e[X]) * (line_s[Y] - line_e[Y])
      - (line_s[X] - line_e[X]) * (vec[Y] - line_e[Y])
      )


def _double_area(v0, v1, v2):
  area = (
      v0[X] * v1[Y] + v1[X] * v2[Y] + v2[X] * v0[Y]
      - v0[X] * v2[Y] - v2[X] * v1[Y] - v1[X] * v0[Y]
      )
  if area < 0:
    area = -area
  return area
