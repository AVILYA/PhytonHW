import math

def square(side):

  if not isinstance(side, (int, float)):
    return "Error: Input must be a number."
  
  area = side * side
  if side == int(side):
    return int(area)
  else:
    return math.ceil(area)


side_length = 5.2
area = square(side_length)
print(f"Площадь квадрата со стороной {side_length}: {area}")

side_length = 5
area = square(side_length)
print(f"Площадь квадрата со стороной {side_length}: {area}")

side_length = "abc"
area = square(side_length)
print(f"Площадь квадрата со стороной {side_length}: {area}")

side_length = 5.0
area = square(side_length)
print(f"Площадь квадрата со стороной {side_length}: {area}")