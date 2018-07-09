#!/usr/bin/env python


from aiogps import gps
import asyncio


async def getdata():
	gpsd = gps.GPS()
	await gpsd.connect()
	await gpsd.stream(gps.WATCH_ENABLE|gps.WATCH_NEWSTYLE)
	

	async for data in gpsd:
		print(data)

if __name__ == '__main__':
	asyncio.get_event_loop().run_until_complete(getdata())