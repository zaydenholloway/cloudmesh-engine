class CloudService:
    def __init__(self, name):
        self.name = name
        self.status = "stopped"

    def start(self):
        self.status = "running"
        return f"{self.name} started successfully."

    def stop(self):
        self.status = "stopped"
        return f"{self.name} stopped."

service = CloudService("API Gateway")
print(service.start())
