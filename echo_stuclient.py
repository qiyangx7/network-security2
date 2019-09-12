import asyncio

class EchoClient(asyncio.Protocol):
	def __init__(self):
		pass

	def connection_made(self, transport):
		self.transport = transport
		#self.transport.write("Hello World".encode())

	def data_received(self, data):
		print(data)
		data = data.decode()
		data = data.split('<EOL>')
		if mycounter == 0:
			for i in data:
				isp = i.split('\n')
				isp = ' '.join(isp)
				print(isp)
				if 'autograde' in isp:
					self.transport.write("SUBMIT, Qiyang Xie, qxie3@jh.edu, 7, 2345<EOL>\n".encode())
				if('TEST' in isp) and ('OK' in isp):
					self.transport.write("look<EOL>\n".encode())
					mycounter = 1
		else:
			listcom = ['look mirror<EOL>\n', 'get gairpin<EOL>\n', 'unlock chest with hairpin<EOL>\n', 'open chest<EOL>\n', 'get hammer in chest<EOL>\n', 'unlock door with hairpin<EOL>\n', 'open door<EOL>\n']
			if mycounter-1 < len(listcom):
				self.transport.write(listcom[mycounter-1].encode())
				mycounter += 1
			else:
				print(data)


if __name__ == "__main__":
	loop = asyncio.get_event_loop()
	coro = loop.create_connection(EchoClient,'127.0.0.1',8080)
	client = loop.run_until_complete(coro)

	try:
		loop.run_forever()
	except KeyboardInterrupt:
		pass

	#client.close()
	#loop.run_until_complete(client.close())
	loop.close()
