import logging
import memory
import cpu_monitoring
import time
import logger

usage_Report = logger.LoggerSystem()
cpu_Monitor_Percent = cpu_monitoring.CPUMonitor()
cpu_Monitor = cpu_monitoring.CPUMonitor()
memory_Monitor = memory.MemoryMonitor()


usage_Report.log_startup()

while True:
    cpu_Monitor.get_Cpu_Usage()
    cpu_Monitor_Percent.get_Cpu_Usage_Perc()
    cpu_Monitor.get_Highest_Cpu_Usage()
    cpu_Monitor.check_Cpu_Usage()
    memory_Monitor.get_Ram_Usage()

    print("CPU:", cpu_Monitor.cpu[-1])
    print("RAM:", memory_Monitor.ram[-1])
    
    usage_Report.log_diagnostics(cpu_Monitor_Percent.cpu_perc[-1], memory_Monitor.ram[-1])

    time.sleep(5)