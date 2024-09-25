import math

initilization = input().split()
spy_coordinates = (int(initilization[0]), int(initilization[1]))
devices = int(initilization[2])
device_info = []
for i in range(devices):
    info = input().split()
    device_info.append(info)

def is_detected(x, y, r):
    devices_detected = 0

    for device in device_info:
        device_x, device_y, device_radius = int(device[0]), int(device[1]), int(device[2])
        distance_squared = (device_x - x) ** 2 + (device_y - y) ** 2
        radius_sum_squared = (r + device_radius) ** 2

        if distance_squared < radius_sum_squared:
            devices_detected += 1

    if devices_detected > 2:
        return True
    
    return False
left, right = 0, 10000
result_radius = 0

while left <= right:
    mid = (left + right) // 2
    if is_detected(spy_coordinates[0], spy_coordinates[1], mid):
        right = mid - 1
    else:
        result_radius = mid
        left = mid + 1

print(result_radius)