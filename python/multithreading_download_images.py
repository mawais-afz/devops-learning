import requests
import os
import threading
import time

def download_image(url, filename):
    # Create images directory if it doesn't exist
    os.makedirs('images', exist_ok=True)
    
    # Add a random seed query parameter to get different images
    full_url = f"{url}?random={filename}"
    
    response = requests.get(full_url)
    if response.status_code == 200:
        open(f"images/image_{filename}.jpg", 'wb').write(response.content)
        print(f"Downloaded image_{filename}.jpg successfully")
    else:
        print(f"Failed to download image_{filename}.jpg. Status code: {response.status_code}")

# Create a list to store threads
threads = []

# Complete URL for Picsum Photos API
urls = "https://picsum.photos/2000/3000"

# Create and start threads for each download
start_time = time.time()
for i in range(5):
    thread = threading.Thread(target=download_image, args=(urls, i))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

end_time = time.time()
print(f"Total execution time: {end_time - start_time:.2f} seconds")
print("All downloads completed!")
