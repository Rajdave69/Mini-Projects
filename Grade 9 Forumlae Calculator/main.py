class Init:
    def __init__(self):
        selection = int(input("""
        1. Polynomials
        2. Circles
        3. Surface Area/Volume
        4. Statistics
        5. Probability
        """))

pi = 22/7


class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    class Polynomial:
        def __init__(self, a, b, c):
            self.a = a
            self.b = b
            self.c = c

    class Circle:
        def __init__(self, radius1 = None, radius2 = None, length = None, angle = None):
            self.radius1 = radius1
            self.radius2 = radius2
            self.length = length
            self.angle = angle


        def area(self):
            return pi * self.radius1 ** 2

        def circumference(self):
            return 2 * pi * self.radius1

        def diameter(self):
            return self.radius1 * 2

        def sector_angle(self):
            return (180 * self.length) / (pi * self.radius1)

        def sector_area(self):
            return (self.angle/2) * self.radius1 ** 2

        def circular_ring_area(self):
            return pi * (self.radius1 ** 2 - self.radius2 ** 2)

    class SurfaceAreaVolume:
        def __init__(self, length = None, breadth = None, height = None, radius = None, base_perimeter = None, slant_height = None):
            self.length = length
            self.breadth = breadth
            self.height = height
            self.radius = radius
            self.base_perimeter = base_perimeter
            self.slant_height = slant_height

        def cuboid_lsa(self):
            return 2 * self.height * (self.length + self.breadth)

        def cuboid_tsa(self):
            return 2 * (self.length * self.breadth + self.length * self.height + self.breadth * self.height)

        def cuboid_volume(self):
            return self.length * self.breadth * self.height


        def cube_lsa(self):
            return 6 * self.length ** 2

        def cube_tsa(self):
            return 6 * self.length ** 2

        def cube_volume(self):
            return self.length ** 3


        def cylinder_lsa(self):
            return 2 * (pi * self.radius * self.height)

        def cylinder_tsa(self):
            return 2 * pi * self.radius * (self.radius + self.height)

        def cylinder_volume(self):
            return pi * self.radius ** 2 * self.height


        def pyramid_lsa(self):
            return 0.5 * self.base_perimeter * self.slant_height

        def pyramid_tsa(self):
            return 0.5 * self.base_perimeter * self.slant_height + self.base_perimeter/4 * self.base_perimeter/4

        def pyramid_volume(self):
            return 1/3 * self.base_perimeter/4 * ((self.base_perimeter/4) * (self.base_perimeter/4)) * self.height


        def prism_lsa(self):
            return self.base_perimeter * self.height

        def prism_tsa(self):
            return self.base_perimeter * self.height * 2 * self.base_perimeter

        def prism_volume(self):
            return self.base_perimeter * self.height


        def cone_lsa(self):
            return pi * self.radius * (self.radius + self.slant_height)

        def cone_tsa(self):
            return pi * self.radius * (self.radius + self.slant_height)

        def cone_volume(self):
            return 1/3 * (pi * self.radius ** 2 * self.height)


        def hemisphere_lsa(self):
            return 2 * pi * self.radius ** 2

        def hemisphere_tsa(self):
            return 3 * pi * self.radius ** 2

        def hemisphere_volume(self):
            return 2/3 * pi * self.radius ** 3


        def sphere_lsa(self):
            return 4 * pi * self.radius ** 2

        def sphere_tsa(self):
            return 4 * pi * self.radius ** 2

        def sphere_volume(self):
            return 4/3 * pi * self.radius ** 3

    class Statistics:
        def __init__(self, sum_of_values, number_of_values, terms_given_in_data, mean, largest_data_value, smallest_data_value, item_given_in_data, ):
            pass








