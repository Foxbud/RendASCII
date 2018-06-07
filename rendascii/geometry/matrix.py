"""
This file is part of RendASCII which is released under MIT.
See file LICENSE.txt for full license details.
"""


import math
from rendascii.geometry import X, Y, Z, W


IDENTITY_3D = (
      (1.0, 0.0, 0.0, 0.0,),
      (0.0, 1.0, 0.0, 0.0,),
      (0.0, 0.0, 1.0, 0.0,),
      (0.0, 0.0, 0.0, 1.0,),
      )


def compose(matrix_a, matrix_b):
  return tuple(
      tuple(
        sum(
          tuple(
            matrix_a[i][k] * matrix_b[k][j]
            for k
            in range(len(matrix_b))
            )
          )
        for j
        in range(len(matrix_b[0]))
        )
      for i
      in range(len(matrix_a))
      )


def transpose(matrix):
  return tuple(
      tuple(
        matrix[j][i]
        for j
        in range(len(matrix[0]))
        )
      for i
      in range(len(matrix))
      )


def transform_3d(matrix, vec):
  return tuple(
      sum(
        tuple(
          matrix[i][j] * vec[j]
          for j
          in range(len(vec))
          )
        )
      for i
      in range(len(vec))
      )


def scaling_3d(scalar):
  return (
      (scalar, 0.0, 0.0, 0.0,),
      (0.0, scalar, 0.0, 0.0,),
      (0.0, 0.0, scalar, 0.0,),
      (0.0, 0.0, 0.0, 1.0,),
      )


def translation_3d(vector):
  return (
      (1.0, 0.0, 0.0, vector[X],),
      (0.0, 1.0, 0.0, vector[Y],),
      (0.0, 0.0, 1.0, vector[Z],),
      (0.0, 0.0, 0.0, 1.0,),
      )


def rotation_3d(theta, axis):
  x = axis[X]
  y = axis[Y]
  z = axis[Z]
  s = math.sin(theta)
  c = math.cos(theta)
  o = (1 - c)
  return (
      (o * x * x + c, o * y * x - z * s, o * z * x + y * s, 0.0,),
      (o * x * y + z * s, o * y * y + c, o * z * y - x * s, 0.0,),
      (o * x * z - y * s, o * y * z + x * s, o * z * z + c, 0.0,),
      (0.0, 0.0, 0.0, 1.0,),
      )

def projection_3d(near, far, fov, ratio):
  cot = 1 / math.tan(fov / 2)
  d = far - near
  return (
      (cot / ratio, 0.0, 0.0, 0.0,),
      (0.0, cot, 0.0, 0.0,),
      (0.0, 0.0, far / d, -far * near / d,),
      (0.0, 0.0, 1.0, 0.0,),
      )
