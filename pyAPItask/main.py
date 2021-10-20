import aiohttp
import asyncio
import time
from collections import namedtuple
from operator import attrgetter


# Create namedtruples (just convenient)
Service = namedtuple('Service', ('name', 'url'))
Service_time = namedtuple('Service_time', ('name', 'resp_time', 'res'))

SERVICES = (
    Service('etherscan', 'https://api.etherscan.io/api?module=proxy&action=eth_blockNumber&apikey=YourApiKeyToken'),
    Service('blockcypher', 'https://api.blockcypher.com/v1/eth/main')
)


async def fetch(session, url, service_name):

    """ simple timer + fetch response result with data """

    start_timer = time.perf_counter()
    async with session.get(url) as resp:

        response = await resp.json()
        if response.get("height") == None:
            res = response.get("result")
            res = int(res,16) # translation of number systems
        else: 
            res = response.get("height")

        end_timer = time.perf_counter() 
        time_to_response = end_timer - start_timer

        return Service_time(service_name, time_to_response, res)


async def main():

    async with aiohttp.ClientSession() as session:

        """ Asynchronous data acquisition and printing """

        tasks = []
        for service in SERVICES:
            tasks.append(asyncio.ensure_future(fetch(session, service.url, service_name=service.name)))

        services_with_times = await asyncio.gather(*tasks)

        sorted(services_with_times, key=attrgetter('resp_time'), reverse=True)
        time_diff = services_with_times[0].resp_time - services_with_times[1].resp_time
        print(f"{services_with_times[1].name} faster {services_with_times[0].name} diff: {time_diff} sec")

        if services_with_times[0].res == services_with_times[1].res:
            print(f"Data is same { services_with_times[0].res }")
        else:
            print(f"Data NOT same. f{services_with_times[0].name} {services_with_times[0].res} and {services_with_times[1].name} {services_with_times[1].res}")
            
if __name__ == "__main__":
    asyncio.run(main())
