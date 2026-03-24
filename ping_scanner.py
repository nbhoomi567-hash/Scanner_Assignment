import subprocess
import platform
import re

def ping_host(host):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    
    try:
        result = subprocess.run(
            ['ping', param, '4', host],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=10
        )

        if result.returncode == 0:
            print(f"{host} is Reachable")

            # Extract average time
            avg_time = re.search(r'Average = (\d+ms)', result.stdout)
            if avg_time:
                print("Average Time:", avg_time.group(1))
        else:
            print(f"{host} is NOT reachable")

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    print("=== Ping Scanner ===")
    
    choice = input("Multiple hosts? (y/n): ")
    
    if choice == 'y':
        hosts = input("Enter hosts separated by space: ").split()
        for host in hosts:
            ping_host(host)
    else:
        host = input("Enter host: ")
        ping_host(host)