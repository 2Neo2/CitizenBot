import asyncio
from rnis import RNIS


login    = "login"
password = "password"
token    = '123.456.789'


async def help():
    rnis = RNIS(login=login, password=password)
    rnis.Help.find
    await rnis.close


async def bad_call():
    """Плохой вызов"""
    rnis = RNIS(login=login, password=password, token=token)
    await rnis.check_token
    d = await rnis.API.Geo.Route.read(uuid='432a3dba-0b94-11ef-b21c-02a520c86c1c')
    api = rnis.API
    d = await api.Geo.Route.read(uuid='432a3dba-0b94-11ef-b21c-02a520c86c1c')
    print(d)
    await rnis.close


async def good_call():
    """Хороший вызов"""
    async with RNIS(login=login, password=password, token=token) as rnis:
        d = await rnis.API.Geo.Route.read(uuid='432a3dba-0b94-11ef-b21c-02a520c86c1c')
        api = rnis.API
        d = await api.Geo.Route.read(uuid='432a3dba-0b94-11ef-b21c-02a520c86c1c')
        print(d)


def main():
    ioloop = asyncio.new_event_loop()
    ioloop.run_until_complete(help())
    ioloop.close()


if __name__ == '__main__':
    main()