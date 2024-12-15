import airsim
import time

# Подключение к симулятору
client = airsim.MultirotorClient()
client.confirmConnection()
client.enableApiControl(True, "Drone1") # управление по API, для нескольких дронов нужно указывать имя
client.armDisarm(True, "Drone1") # запуск двигателей

# Взлет
print("Взлет...")
client.takeoffAsync(vehicle_name="Drone1").join()

# Небольшая задержка
time.sleep(2)

# Полет вперед
print("Полет вперед...")
client.moveByVelocityZAsync(5, 0, -2, 3, vehicle_name="Drone1").join() # Движение со скоростью 5 м/с по оси X, 0 м/с по оси Y, на высоте 2 метра в течение 3 секунд

# Полет вправо
print("Полет вправо...")
client.moveByVelocityZAsync(0, 5, -2, 3, vehicle_name="Drone1").join()

# Полет назад
print("Полет назад...")
client.moveByVelocityZAsync(-5, 0, -2, 3, vehicle_name="Drone1").join()

# Полет влево
print("Полет влево...")
client.moveByVelocityZAsync(0, -5, -2, 3, vehicle_name="Drone1").join()

# Зависание
print("Зависание...")
client.hoverAsync(vehicle_name="Drone1").join()

# Посадка
print("Посадка...")
client.landAsync(vehicle_name="Drone1").join()

# Остановка двигателей
client.armDisarm(False, "Drone1")

print("Полет завершен.")