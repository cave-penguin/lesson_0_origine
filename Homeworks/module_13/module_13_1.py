import asyncio


async def start_strongman(name, power):
    print(f"Силач {name} начал соревнования.")

    for ball in range(1, 6):
        await asyncio.sleep(power)
        print(f"Силач {name} поднял {ball} шар")

    print(f"Силач {name} закончил соревнования.")


async def start_tournament():

    task_1 = asyncio.create_task(start_strongman("Alex", 5))
    task_2 = asyncio.create_task(start_strongman("Micky", 2))
    task_3 = asyncio.create_task(start_strongman("Denis", 4))

    await task_1
    await task_2
    await task_3


asyncio.run(start_tournament())
