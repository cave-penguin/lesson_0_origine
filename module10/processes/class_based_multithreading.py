from threading import Thread
import requests

# class Getter(Thread):
#     res = []
#     THE_URL = "https://binaryjazz.us/wp-json/genrenator/v1/genre/"
#     def run(self):
#         response = requests.get(self.THE_URL)
#         Getter.res.append(response.json())

# threads = []
# num_of_threads = 10
# for i in range(num_of_threads):
#     thread = Getter()
#     thread.start()
#     threads.append(thread)

# for thread in threads:
# 	thread.join()

# print(Getter.res)


class Getter(Thread):
	res = []
    
	def __init__(self, url):
		self.THE_URL = url
		super().__init__()

	def run(self):
		response = requests.get(self.THE_URL)
		Getter.res.append(response.json())


threads = []
num_of_threads = 10
for i in range(num_of_threads):
    thread = Getter("https://binaryjazz.us/wp-json/genrenator/v1/genre/")
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

print(Getter.res)
assert len(Getter.res) == num_of_threads
