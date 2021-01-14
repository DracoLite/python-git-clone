import asyncio
import aiohttp
import json
import datetime
import time

RawData = open('F000.json')
Data = json.load(RawData)
RawData.close()

time.sleep(5)

async def ARequest(Requests , http : str) -> str:
    async with Requests.get(http) as Response:
        return Response.status
 
async def ArequestPatcher( Requests, ReqAmnt : int, http : str) -> list:
    pack = []
    for i in range(ReqAmnt):
        pack += [ARequest(Requests=Requests , http=http)]
    return pack

async def main() -> None:
    async with aiohttp.ClientSession() as Arequest:
        if Data['lmnt'] :
            await lmnt(Arequest, Data['http'], asyncio.get_event_loop())
        PackedTasks = await ArequestPatcher(Arequest ,Data['ReqAmnt'],  Data['http'])
        Responses = await asyncio.gather(*PackedTasks)
        print(Responses)

async def lmnt(ASRequest, http , loop) -> None:
    while True:
        print(datetime.datetime.now() - start)
        if (start - datetime.datetime.now()).total_seconds() < 0 :
            print("start")
            time.sleep(5)
            while True:
                loop.create_task(ARequest(ASRequest, http))
            

start = datetime.datetime(year=2021,month=1,day=24,hour=8,minute=30,second=0,microsecond=0)
asyncio.get_event_loop().run_until_complete(main())
