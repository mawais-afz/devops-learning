import asyncio
import time

async def say_something(delay, what):
    """Coroutine that waits for a specified time and prints a message"""
    await asyncio.sleep(delay)
    print(what)

async def fetch_data(url):
    """Simulate fetching data from a URL"""
    print(f"Start fetching from {url}")
    await asyncio.sleep(2)  # Simulate network delay
    print(f"Finished fetching from {url}")
    return f"Data from {url}"

async def process_data(data):
    """Simulate processing of fetched data"""
    print(f"Start processing {data}")
    await asyncio.sleep(1)  # Simulate processing time
    print(f"Finished processing {data}")
    return f"Processed {data}"

async def main():
    # Example 1: Running multiple coroutines concurrently
    print("\nExample 1: Running multiple coroutines")
    await asyncio.gather(
        say_something(1, "Hello"),
        say_something(2, "World"),
        say_something(3, "Async")
    )

    # Example 2: Chaining coroutines
    print("\nExample 2: Chaining coroutines")
    urls = [
        "http://example.com/1",
        "http://example.com/2",
        "http://example.com/3"
    ]
    
    # Create tasks for fetching data
    fetch_tasks = [fetch_data(url) for url in urls]
    fetched_data = await asyncio.gather(*fetch_tasks)
    
    # Process the fetched data
    process_tasks = [process_data(data) for data in fetched_data]
    processed_results = await asyncio.gather(*process_tasks)
    
    print("\nFinal results:")
    for result in processed_results:
        print(result)

if __name__ == "__main__":
    # Run the async main function
    start_time = time.time()
    asyncio.run(main())
    end_time = time.time()
    print(f"\nTotal execution time: {end_time - start_time:.2f} seconds")
