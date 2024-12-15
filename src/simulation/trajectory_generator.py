import airsim
import numpy as np
from src.utils.kafka_producer_wrapper import KafkaProducerWrapper

class TrajectoryGenerator:
    def __init__(self):
        self.client = airsim.MultirotorClient()
        self.client.confirmConnection()
        self.client.enableApiControl(True)
        self.client.armDisarm(True)
        self.producer = KafkaProducerWrapper()

    def takeoff(self):
        self.client.takeoffAsync().join()

    def land(self):
        self.client.landAsync().join()
        self.client.armDisarm(False)
        self.client.enableApiControl(False)
        self.producer.close()

    def fly_and_send_trajectory(self, waypoints, speed=5):
        for point in waypoints:
            self.client.moveToPositionAsync(point[0], point[1], point[2], speed).join()
            message = {'position': {'x': point[0], 'y': point[1], 'z': point[2]}}
            self.producer.send_message(message)

    def generate_waypoints(self):
        radius = 10
        points = []
        for angle in np.linspace(0, 2 * np.pi, num=20):
            x = radius * np.cos(angle)
            y = radius * np.sin(angle)
            z = -10
            points.append([x, y, z])
        return points

if __name__ == "__main__":
    generator = TrajectoryGenerator()
    generator.takeoff()
    waypoints = generator.generate_waypoints()
    generator.fly_and_send_trajectory(waypoints)
    generator.land()