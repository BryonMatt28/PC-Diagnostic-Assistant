import psutil

cpu = []

def get_cpu_usage():
   cpu_usage = psutil.cpu_percent(interval=1, percpu=True)
   cpu.append(cpu_usage)
get_cpu_usage()



def get_highest_cpu_usage():
    if cpu:
        highest_usage = max(cpu[0])
        return highest_usage
    else:
        return None

highest_cpu = get_highest_cpu_usage()

if highest_cpu == None:
    print("No CPU usage data available.")
elif highest_cpu <= 80:
    print("CPU usage is within normal limits.")
else:
    print("Warning: High CPU usage detected!")

    