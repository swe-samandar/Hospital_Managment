import asyncio, time

async def get(url_num):
	print(f"{url_num}-URLga so'rov yuborildi")
	await asyncio.sleep(1)
	print(f"{url_num}-URLdan javob keldi")
  
async def main():
    await asyncio.gather(get(1), get(2), get(3), get(4), get(5))
  
# start = time.time()
# asyncio.run(main())  
# end = time.time()
# total = end - start
# print(f"Sarflangan umumiy vaqt: {total} soniya")



def get_(url_num):
	print(f"{url_num}-URLga so'rov yuborildi")
	time.sleep(1)
	print(f"{url_num}-URLdan javob keldi")
  
  
start = time.time()
for i in range(1, 6):
	get_(i)

end = time.time()
total = end - start
print(f"Sarflangan umumiy vaqt: {total} soniya")