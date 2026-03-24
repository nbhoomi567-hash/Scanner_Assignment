import subprocess

def check_nmap():
    try:
        subprocess.run(['nmap', '--version'], stdout=subprocess.PIPE)
        return True
    except:
        return False

def run_scan(target, option):
    try:
        if option == '1':
            cmd = ['nmap', '-sn', target]
        elif option == '2':
            cmd = ['nmap', target]
        elif option == '3':
            cmd = ['nmap', '-sV', target]
        else:
            print("Invalid choice")
            return

        result = subprocess.run(
            cmd,
            stdout=subprocess.PIPE,
            text=True
        )

        print(result.stdout)

        save = input("Save output? (y/n): ")
        if save == 'y':
            with open("nmap_output.txt", "w") as f:
                f.write(result.stdout)

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    print("=== Nmap Scanner ===")
    
    if not check_nmap():
        print("Nmap is not installed!")
        exit()

    target = input("Enter target IP: ")

    print("""
1. Host Discovery
2. Port Scan
3. Service Detection
""")

    choice = input("Enter choice: ")
    run_scan(target, choice)