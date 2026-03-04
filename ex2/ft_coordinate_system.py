#!/usr/bin/env python3
import math


def distance_math(position1: tuple[int, int, int],
                  position2: tuple[int, int, int]
                  ) -> float:
    """Return the Euclidean distance between two 3D integer positions."""
    # tuples unpacking
    x1, y1, z1 = position1
    x2, y2, z2 = position2
    # Euclidean formula
    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
    return distance


def parse_coords(coords: str) -> tuple[int, int, int] | None:
    """Parse a 'x,y,z' string into a 3D integer tuple.

    Print an error and return None if parsing fails.
    """
    try:
        parts = coords.split(",")
        # tuple unpacking and conversion to int
        if len(parts) != 3:
            print("Invalid coordinates: expected 3 values.")
            return None
        x = int(parts[0])
        y = int(parts[1])
        z = int(parts[2])
        res = (x, y, z)
        return res
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")
        return None


def main() -> None:
    """Run a small demo of tuple coordinates, parsing, and distances."""
    print("=== Game Coordinate System ===\n")
    origin = (0, 0, 0)
    tuple_pos = (10, 20, 5)
    print(f"Position created: {tuple_pos}")
    print(f"Distance between {origin} and {tuple_pos}"
          f": {distance_math(origin, tuple_pos):.2f}\n")
    str_coords = "3,4,0"
    print(f'Parsing coordinates: "{str_coords}"')
    parsed_coords = parse_coords(str_coords)
    if parsed_coords is not None:
        print(f"Parsed position: {parsed_coords}")
        print(f"Distance between {origin} and {parsed_coords}"
              f": {distance_math(origin, parsed_coords):.1f}\n")
    abc = "abc,def,ghi"
    print(f'Parsing invalid coordinates: "{abc}"')
    parse_coords(abc)
    print("\nUnpacking demonstration:")
    if parsed_coords is not None:
        x, y, z = parsed_coords
        print(f"Player at x={x}, y={y}, z={z}")
        print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    main()
