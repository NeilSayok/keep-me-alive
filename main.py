#!/usr/bin/env python3
import requests
import datetime

def ping_backend():
    urls = ["https://eventbook.bluelabs.in","https://eventbookbackend-users.onrender.com","https://eventbookbackend-category.onrender.com"]
    
    for url in urls:
        try:
            print(f"{datetime.datetime.now()}: Pinging {url}")
            response = requests.get(url, timeout=30)
            print(f"Response: {response.status_code}")
            
            if response.status_code == 200:
                print("Backend is alive")
            else:
                print(f"⚠️ Unexpected status code: {response.status_code}")
                
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    ping_backend()  # Just ping once, then exit