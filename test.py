import sys
from toio.simple import SimpleCube



def test():
    with SimpleCube(name="304") as cube:
        targets = [(20, -60, 180), (122, -66, 90), (124, 58, 0), (25, 60, 270)]
        print("name:", cube.get_cube_name())
        print("battery:", cube.get_battery_level())
        print(cube.get_current_position())
        for x, y, degree in targets:
            cube.set_orientation(speed=-30, degree=degree)
            cube.move_to(speed=30, x=x, y=y)
            print("position:", x, y, cube.get_current_position())
        # x, y = cube.get_current_position()
        # print("position:", x, y)
        # cube.move_to(speed=30, x=50, y=0)
        # #print(cube.get_current_position())
        # cube.set_orientation(speed=30, degree=180)
        # print(cube.get_current_position())
        # cube.move(30, 1)
        # print(cube.get_current_position())
        # cube.spin(60, 1)
        cube.stop_motor()

if __name__ == "__main__":
    sys.exit(test())