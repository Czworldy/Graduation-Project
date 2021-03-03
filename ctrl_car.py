import glob
import os
import sys
import time

try:
    sys.path.append(glob.glob('A:/CARLA_0.9.10_2/WindowsNoEditor/PythonAPI/carla/dist/carla-*%d.%d-%s.egg' % (
        sys.version_info.major,
        sys.version_info.minor,
        'win-amd64' if os.name == 'nt' else 'linux-x86_64'))[0])
except IndexError:
    pass

import carla

from carla import VehicleLightState as vls

import argparse
import logging
from numpy import random

def main():
     actor_list = []

     try:
         # Creat client to send requests.
         client = carla.Client('localhost',2000)
         client.set_timeout(2.0)

         world = client.get_world()

         bp_lib = world.get_blueprint_library()

         bp = random.choice(bp_lib.filter('vehicle'))

         



    


if __name__ == '__main__':

    main()

