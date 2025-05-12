import requests
import threading
import time

# PERINGATAN: Hanya gunakan ini pada server Anda sendiri atau dengan izin tertulis
# Mengirim traffic ke website tanpa izin adalah ILEGAL

def send_requests(url, requests_count, delay=0):
    success = 0
    for _ in range(requests_count):
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                success += 1
        except:
            pass
        time.sleep(delay)
    print(f"Sent {success} successful requests")

# Contoh penggunaan yang sah (ke server lokal)
if __name__ == "__main__":
    TARGET_URL = "http://localhost:8080"  # Ganti dengan URL target YANG ANDA MILIKI
    REQUESTS_PER_SECOND = 50000000  # Jumlah yang realistis untuk pengujian
    THREADS = 10
    DURATION = 10  # detik
    
    print(f"Starting load test to {TARGET_URL} for {DURATION} seconds")
    
    threads = []
    for _ in range(THREADS):
        t = threading.Thread(target=send_requests, 
                           args=(TARGET_URL, REQUESTS_PER_SECOND*DURATION/THREADS, 1/REQUESTS_PER_SECOND))
        t.start()
        threads.append(t)
    
    for t in threads:
        t.join()
    
    print("Load test completed")