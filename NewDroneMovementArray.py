
def newDroneMovementArray(visionArraySize):
    droneMovementArray = [[0]*visionArraySize[0]]*visionArraySize[1]
   
    #droneVelocity is a list of 3 velocities, x (positive x is forward), y (positive y is to the right) then z (positive z is upwards), in ints (mm/s)
    #droneRotation is a list of 3 rotation speeds along axes, x, y then z (use right hand rule with thumb in the positive directions to determine the postive) in ints (mm/s)
    #droneShape is a 2D array representing the size and shape of the drone. Made of 0's (for empty) and 1's (for occupied) in ints and is sized like the visionArray
    #visionArraySize is a list of two ints that represents the definition of the drone's sight, x first then y.
    #loopTime is the time (in ms) between each loop, which would allow us to determine the distance until the next loop with the speed and rotation.

    #For now, assume that the camera angle is of 0, a.k.a. pointing towards the positive x axis a.k.a. the front of the drone
    #cameraAngle is a list of 3 ints (degrees) representing the theta (around x axis), phi (around y axis) and zeta (around z axis)

    return droneMovementArray

print(newDroneMovementArray(list((2,3))))