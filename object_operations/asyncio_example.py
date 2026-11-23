import time
from timeit import main
import asyncio

def sync_fetch_data():
    print("Start fetching data...")
    time.sleep(2)
    print("Done fetching data.")
    return {"data": 1}

def test_sync_fetch_data():
    start_time = time.time()
    print("Before fetching data")
    data1 = sync_fetch_data()
    data2 = sync_fetch_data()
    data3 = sync_fetch_data()
    end_time = time.time()
    print(f"Data fetched: {data1}, {data2}, {data3}")
    print(f"Total time taken: {end_time - start_time}")

async def async_fetch_data():
    print("Start fetching data...")
    await asyncio.sleep(2)
    print("Done fetching data.")
    return {"data": 1}

async def test_async_fetch_data():
    start_time = time.time()
    print("Before fetching data")
    results = await asyncio.gather(
        async_fetch_data(),
        async_fetch_data(),
        async_fetch_data()
    )
    end_time = time.time()
    print(f"Data fetched: results: {results}")
    print(f"Total time taken: {end_time - start_time}")

if __name__ == "__main__":
    print("Testing synchronous data fetching:")
    test_sync_fetch_data()
    
    print("\nTesting asynchronous data fetching:")
    asyncio.run(test_async_fetch_data())