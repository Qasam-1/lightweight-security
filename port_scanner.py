import socket
import threading

# Very small port scanner
# Added threading so it's faster than scanning ports one by one

def scan_port(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)  # prevents hanging forever
        result = sock.connect_ex((host, port))
        if result == 0:
            print(f"[+] Port {port} is OPEN")
        sock.close()
    except:
        pass

if __name__ == "__main__":
    target = input("Enter target IP (example: 127.0.0.1): ")
    ports = range(1, 1025)  # first 1024 ports
    threads = []

    print(f"Scanning {target} ...")

    for port in ports:
        thread = threading.Thread(target=scan_port, args=(target, port))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("Scan complete.")
