#!/usr/bin/env python3

# Created By: Kent Gatera
# Date: Dec. 7, 2022
# This program calculates the length, width and area of a triangle.


def calc_area(length: float, width: float) -> float:
    area = length * width
    return area


def calc_width(length: float, area: float) -> float:
    width = area / length
    return width


def calc_length(width: float, area: float) -> float:
    length = area / width
    return length


def calc_perimeter(width: float, length: float) -> float:
    perimeter = (length + width) * 2
    return perimeter


def main():
    try:
        user_path = int(
            input(
                "What do you want to calculate?.\n"
                "A. Press (1) if you want to calculate the area of the rectangle.\n"
                "B. Press (2) if you want to calculate the width of the rectangle.\n"
                "C. Press (3) if you want to calculate the length of the rectangle.\n"
                "D. Press (4) if you want to calculate the perimeter of the rectangle.\n>> "
            )
        )
        if user_path == 1:
            user_length_str = float(
                input("What is the length of the rectangle? (cm): ")
            )
            user_width_str = float(input("What is the width of the rectangle? (cm): "))
            try:
                user_length = float(user_length_str)
                user_width = float(user_width_str)
                if user_length <= 0 or user_width <= 0:
                    print("Invalid measurements.\nRestarting...")
                    return main

                ans_area = calc_area(length=user_length, width=user_width)
                print(
                    f"The area of a triangle of length ({user_length}) * width ({user_width}) = {ans_area} cm^2."
                )

            except ValueError:
                print("Invalid measurements")

        elif user_path == 2:
            user_length_str = float(
                input("What is the length of the rectangle? (cm): ")
            )
            user_area_str = float(input("What is the area of the rectangle? (cm): "))
            try:
                user_length = float(user_length_str)
                user_area = float(user_area_str)
                if user_length <= 0 or user_area <= 0:
                    print("Invalid measurements.\nRestarting...")
                    return main

                ans_width = calc_width(length=user_length, area=user_area)
                print(
                    f"The width of a triangle of area ({user_area}) cm^2 / length ({user_length}) cm is {ans_width} cm."
                )

            except ValueError:
                print("Invalid measurements")

        elif user_path == 3:
            user_width_str = float(input("What is the width of the rectangle? (cm): "))
            user_area_str = float(input("What is the area of the rectangle? (cm): "))
            try:
                user_width = float(user_width_str)
                user_area = float(user_area_str)
                if user_width <= 0 or user_area <= 0:
                    print("Invalid measurements.\nRestarting...")
                    return main

                ans_length = calc_length(width=user_width, area=user_area)
                print(
                    f"The length of a triangle of area ({user_area}) cm^2 / width ({user_width}) cm is {ans_length} cm."
                )
            except ValueError:
                print("Invalid measurements")

        elif user_path == 4:
            user_length_str = float(
                input("What is the length of the rectangle? (cm): ")
            )
            user_width_str = float(input("What is the width of the rectangle? (cm): "))
            try:
                user_length = float(user_length_str)
                user_width = float(user_width_str)
                if user_width <= 0 or user_length <= 0:
                    print("Invalid measurements.\nRestarting...")
                    return main

                ans_perimeter = calc_perimeter(width=user_width, length=user_length)
                print(
                    f"The perimeter of a triangle of length ({user_length}) cm and width ({user_width}) cm is {ans_perimeter} cm."
                )

            except ValueError:
                print("Invalid measurements")

        else:
            print("Pick a valid number displayed.")
        main()

    except ValueError:
        print("Pick a valid number displayed.")


if __name__ == "__main__":
    main()
