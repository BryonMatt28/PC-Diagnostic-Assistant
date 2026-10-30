import memory
import cpu_monitoring
import time



cpu_Monitor = cpu_monitoring.CPUMonitor()
memory_Monitor = memory.MemoryMonitor()

while True:
    cpu_Monitor.get_Cpu_Usage()
    cpu_Monitor.get_Highest_Cpu_Usage()
    cpu_Monitor.check_Cpu_Usage()
    memory_Monitor.get_Ram_Usage()

    print("CPU:", cpu_Monitor.cpu[-1])
    print("RAM:", memory_Monitor.ram[-1])

    time.sleep(5)