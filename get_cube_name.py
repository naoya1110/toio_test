import sys
from toio.simple import SimpleCube

def get_cube_name():
    with SimpleCube() as cube:
        print("cube name:", cube.get_cube_name())

if __name__ == "__main__":
    sys.exit(get_cube_name())