import psutil

class MemoryMonitor:



    def __init__(self):
        self.ram = []

    def get_Ram_Usage(self):
        ram_usage = psutil.virtual_memory().percent
        self.ram.append(ram_usage)
        self.clear_Oldest_Entry()
        return ram_usage
    
    def clear_Oldest_Entry(self):
        if len(self.ram) > 60:
            self.ram.pop(0)


             