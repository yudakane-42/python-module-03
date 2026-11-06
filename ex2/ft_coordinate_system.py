#! /usr/bin/env python3

import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        line = input("Enter new coordinates as floats in format 'x,y,z': ")
        parts = line.split(",")
        if len(parts) != 3:
            print("Invalid syntax")
            continue
        i = 0
        try:
            x = float(parts[i])
            i += 1
            y = float(parts[i])
            i += 1
            z = float(parts[i])
            return x, y, z
        except ValueError as e:
            print(f"Error on parameter '{parts[i]}': {e}")


def coordinate_system() -> None:
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")
    pos = get_player_pos()
    print(f"Got a first tuple: {pos}")
    print(f"It includes: X={pos[0]}, Y={pos[1]}, Z={pos[2]}")
    distance = math.sqrt(pos[0] ** 2 + pos[1] ** 2 + pos[2] ** 2)
    print(f"Distance to center: {round(distance, 4)}")

    print("\nGet a second set of coordinates")
    pos2 = get_player_pos()
    x = pos2[0] - pos[0]
    y = pos2[1] - pos[1]
    z = pos2[2] - pos[2]
    distance2 = math.sqrt(x ** 2 + y ** 2 + z ** 2)
    print(f"Distance between the 2 sets of coordinates: {round(distance2, 4)}")


if __name__ == "__main__":
    coordinate_system()
