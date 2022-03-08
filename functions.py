def volume_and_area(length):
    volume_of_cube = length * length * length  #give the function meaning through the formule
    area_of_cube = 6 * length * length
    return volume_of_cube, area_of_cube     #close the function
volume, area = volume_and_area(5)                        #call the function (need to use the name of the function)with the variablems
print(f"Volume = {volume} and Area = {area}")
volume, area = volume_and_area(10)
print(f"Volume = {volume} and Area = {area}")
volume, area = volume_and_area(20)
print(f"Volume = {volume} and Area = {area}")
