import psutil
class CPUMonitor:



    def __init__(self):
        self.cpu = []
        self.cpu_perc = []

    def get_Cpu_Usage(self):
        cpu_usage = psutil.cpu_percent(interval=1, percpu=True)
        self.cpu.append(cpu_usage)
        self.clear_Oldest_Entry()
        return cpu_usage

    def get_Cpu_Usage_Perc(self):
        cpu_usage_perc = psutil.cpu_percent(interval=1)
        self.cpu_perc.append(cpu_usage_perc)
        self.clear_Oldest_Entry()
        return cpu_usage_perc

    def get_Highest_Cpu_Usage(self):
        if self.cpu:
            highest_usage = max(self.cpu[-1])
            return highest_usage
        else:
            return None

    def clear_Oldest_Entry(self):
        if len(self.cpu) > 60:
            self.cpu.pop(0) 

        if len(self.cpu_perc) > 1:
            self.cpu_perc.pop(0)       

    def check_Cpu_Usage(self):
        highest_cpu = self.get_Highest_Cpu_Usage()   

        if highest_cpu is None:
            print("No CPU usage data available.")
        elif highest_cpu <= 80:
            print("CPU usage is within normal limits.")
        else:
            print("Warning: High CPU usage detected!")
            return highest_cpu


