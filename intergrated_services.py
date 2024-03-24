import geopy.distance
from datetime import datetime

class Service:
    def __init__(self, name, location, service_type):
        self.name = name
        self.location = location
        self.service_type = service_type

class User:
    def __init__(self, name, location):
        self.name = name
        self.location = location

class Scheduler:
    def __init__(self):
        self.services = []

    def add_service(self, service):
        self.services.append(service)

    def find_nearest_service(self, user_location, service_type):
        nearest_service = None
        min_distance = float('inf')
        
        for service in self.services:
            if service.service_type == service_type:
                distance = geopy.distance.distance(user_location, service.location).km
                if distance < min_distance:
                    min_distance = distance
                    nearest_service = service
        
        return nearest_service

    def schedule_service(self, user, service_type, scheduled_time):
        nearest_service = self.find_nearest_service(user.location, service_type)
        if nearest_service:
            print(f"Scheduled {service_type} service at {nearest_service.name} for {user.name} at {scheduled_time}.")
            # Implement scheduling logic here
        else:
            print(f"No {service_type} service available nearby.")

if __name__ == "__main__":
    # Initialize some sample services
    garage_service = Service("Ole miss connection's Garage", ( 0.4861231, 35.2681088), "Garage")
    electrical_service = Service("Koslim's Electric", ( 0.4861231, 35.2681088), "Electrical")
    plumbing_service = Service("Ole pris capital Masters", ( 0.4861231, 35.2681088), "Plumbing")
    # Add more services as needed

    # Initialize scheduler and add services
    scheduler = Scheduler()
    scheduler.add_service(garage_service)
    scheduler.add_service(electrical_service)
    scheduler.add_service(plumbing_service)
    # Add more services as needed

    # Simulate a user's request for a service
    user_location = (40.7128, -74.0060)  # User's current location (latitude, longitude)
    user = User("Isaac Kipruto", user_location)
    service_type = "Garage"  # Type of service requested
    scheduled_time = datetime.now()  # Time at which service is scheduled

    # Schedule the requested service
    scheduler.schedule_service(user, service_type, scheduled_time)
