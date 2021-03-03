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

# from carla import VehicleLightState as vls

# import argparse
# import logging
from numpy import random

def main():
    actor_list = []

    try:
        # Creat client to send requests.
        client = carla.Client('localhost',2000)
        client.set_timeout(2.0)

        # Current world
        world = client.get_world()
        bp_lib = world.get_blueprint_library()
        bp = random.choice(bp_lib.filter('vehicle'))

        # Get spawn points
        transform = random.choice(world.get_map().get_spawn_points())
       
        # Change rotation
        transform.rotation.yaw = 90.0
        print(transform)

        # Spawn
        vehicle = world.spawn_actor(bp, transform)

        
        if vehicle is None:
            print('None vehicle')
        else:
            # Add it to list
            actor_list.append(vehicle)
            print('created %s' % vehicle.type_id)
            
            vehicle.set_location(carla.Location(x=0.0, y=-50.0, z=0.0))
            print(vehicle.get_location()) # Why get_location return 0.0 0.0

            # Attach a RGB camera, location is relative to the vehicle
            camera_bp = bp_lib.find('sensor.camera.rgb')
            camera_transform = carla.Transform(carla.Location(x=1.5, z=2.4))
            camera = world.spawn_actor(camera_bp, camera_transform, attach_to=vehicle)

            # Add it to list
            actor_list.append(camera)
            print('created %s' % camera.type_id)
            
            # Image save to disk
            camera.listen(lambda image: image.save_to_disk('_out_rgb/%06d.png' % image.frame))
            
            # Set velocity 
            vehicle.set_target_velocity(carla.Vector3D(x=0.0, y=-3.0, z=0.0))
        time.sleep(10)
    finally:

        vehicle.destroy()
        camera.destroy()
        print('done.')
        



if __name__ == '__main__':

    main()

