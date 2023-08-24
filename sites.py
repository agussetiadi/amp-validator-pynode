import os
import requests
import threading
import time
import subprocess
import json
import html
from concurrent.futures import ThreadPoolExecutor

class AmpValidator():

	def __init__(self):
		self.urls = [
			'https://food.detik.com/info-kuliner/d-6820681/rumput-laut-kering-di-resto-china-ternyata-dibuat-pakai-sayuran-ini/amp',
			'https://food.detik.com/info-kuliner/d-6787060/fakta-bakcang-hidangan-ikonik-yang-disajikan-saat-festival-peh-cun/amp',
			'https://www.detik.com/edu/perguruan-tinggi/d-6821636/universitas-terbuka-ut-jurusan-yang-tersedia-dan-syarat-masuknya/amp',
			'https://oto.detik.com/motor/d-6821606/harga-honda-vario-160-terbaru-juli-2023-mulai-dari-rp-26-jutaan/amp',
			'https://news.detik.com/berita/d-6471836/pohon-randu-alas-3-abad-ditebang-di-klaten-warga-gelar-ritual-bawa-ingkung/amp'
		]

		self.results = []

		self.sessions = requests.Session()

		self.total_pass = 0
		self.total_fail = 0

	def fetch_all_sites(self):
		with ThreadPoolExecutor(max_workers=3) as executor:
			executor.map(self.fetch_site, self.urls)

	def fetch_site(self, url):
		with self.sessions as session:
			with session.get(url) as response:
				response.encoding = 'utf-8'
				result_text = response.text

				print(f"Read {len(response.content)} from {url}")

				self.results.append({'url': url, 'content': result_text})

	def validate_page(self):
		arg_json = json.dumps(self.results)
		open_code = 'w'

		if not os.path.exists('amp.json'):
			open_code = 'x'

		with open('amp.json', open_code) as file:
			file.write(arg_json)

		process = subprocess.Popen(["node", "demo.js"], stdout=subprocess.PIPE)
		stdout, stderr = process.communicate(timeout=30)
		result_json = json.loads(stdout.decode())

		for row in result_json:
			if row['status'] == 'PASS':
				self.total_pass += 1
				print(f"\033[92mPASS {row['url']}\033[00m")
			else:
				self.total_fail += 1
				print(f"\033[91m{row['status']} {row['url']}\033[00m")
				print(f"\033[91m{row['message']}\033[00m")
	
	def execute(self):
		start_time = time.time()

		self.fetch_all_sites()
		
		duration = time.time() - start_time
		print("\n")
		print("\033[92mSuccess fetch data\033[00m")
		print(f"\033[92mtime {duration}\033[00m")
		print("\n")
		print("AMP Validation starting")
		print("\n")

		self.validate_page()

		print("\n")
		print("RESULT")
		print("\n")
		print(f"\033[92m{self.total_pass} PASS\033[00m")
		print(f"\033[91m{self.total_fail} FAIL\033[00m")