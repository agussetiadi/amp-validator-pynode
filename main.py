import os
import command
import requests
import subprocess
import html
import json
from html.parser import HTMLParser
from nodejs import node
from sites import AmpValidator

# urls = [
# 	'https://food.detik.com/info-kuliner/d-6820681/rumput-laut-kering-di-resto-china-ternyata-dibuat-pakai-sayuran-ini/amp',
# 	'https://food.detik.com/info-kuliner/d-6787060/fakta-bakcang-hidangan-ikonik-yang-disajikan-saat-festival-peh-cun/amp',
# 	'https://www.detik.com/edu/perguruan-tinggi/d-6821636/universitas-terbuka-ut-jurusan-yang-tersedia-dan-syarat-masuknya/amp',
# 	'https://oto.detik.com/motor/d-6821606/harga-honda-vario-160-terbaru-juli-2023-mulai-dari-rp-26-jutaan/amp'
# ]

# req = requests.get(urls)
# req.encoding = 'utf-8'

# if is not os.path.isdir('amp-pages'):
# 	os.mkdir()

# p = subprocess.Popen(["node", "demo.js", "-p", req.text], stdout=subprocess.PIPE)
# r = p.communicate()

# print(r)

# with open('amp.html', 'x') as f:
# 	f.write(req.content)

if __name__ == '__main__':
	amp_validator = AmpValidator()
	amp_validator.execute()