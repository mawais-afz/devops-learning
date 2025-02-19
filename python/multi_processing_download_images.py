import multiprocessing
import requests
import os
import time
import uuid

def download_image(url, filename):
    os.makedirs('images', exist_ok=True)
    full_url = f"{url}?random={filename}"
    response = requests.get(full_url)
    if response.status_code == 200:
        open(f"images/image_{filename}.jpg", 'wb').write(response.content)
        print(f"Downloaded image_{filename}.jpg successfully")
    else:
        print(f"Failed to download image_{filename}.jpg. Status code: {response.status_code}")


url = "https://picsum.photos/2000/3000"

# total_time = 0
# for i in range(5):
#     start_time = time.time()
#     download_image(url, i)
#     end_time = time.time()
#     print(f"Time taken to download image_{i}.jpg: {end_time - start_time:.2f} seconds")
#     total_time += end_time - start_time

# print(f"Total time taken to download 5 images: {total_time:.2f} seconds")



def main():
    # URL for Picsum Photos API
    url = "https://picsum.photos/2000/3000"
    
    # Create a pool of processes
    processes = []
    start_time = time.time()
    
    # Create and start processes for each download
    for i in range(5):
        p = multiprocessing.Process(target=download_image, args=(url, i))
        processes.append(p)
        p.start()
    
    # Wait for all processes to complete
    for p in processes:
        p.join()
    
    end_time = time.time()
    print(f"\nTotal time taken to download 5 images: {end_time - start_time:.2f} seconds")

if __name__ == '__main__':
    main()