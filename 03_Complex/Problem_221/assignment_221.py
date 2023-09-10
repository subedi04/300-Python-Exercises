'''
Write A Python Program To Get RAM and CPU Usage Of Computer
'''
import psutil

def get_ram_usage():
    # Get RAM usage
    ram = psutil.virtual_memory()
    return {
        "total": ram.total,
        "used": ram.used,
        "free": ram.free,
        "percent_used": ram.percent
    }

def get_cpu_usage():
    # Get CPU usage percentage
    return psutil.cpu_percent(interval=1)

if __name__ == "__main__":
    ram_usage = get_ram_usage()
    cpu_usage = get_cpu_usage()

    print("RAM Usage:")
    print(f"Total: {ram_usage['total']} bytes")
    print(f"Used: {ram_usage['used']} bytes")
    print(f"Free: {ram_usage['free']} bytes")
    print(f"Percent used: {ram_usage['percent_used']}%")

    print("\nCPU Usage:")
    print(f"{cpu_usage}%")
