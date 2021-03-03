from InstagramAPI import *
import time

login = 'niggvard'
password = 'arsenpoter7777777'

log = InstagramAPI(login, password)
log.login()

while True:
	log.follow('9009373')#egorkreed
	log.follow('3667119749')#karnaval
	log.follow('1829634788')#dava
	log.follow('2485931655')#a4
	log.follow('705805118')#morgenshtern
	log.follow('1098513252')#karinakross
	log.follow('1388636732')#adushkina
	print('адыхаю')
	time.sleep(300)
	log.unfollow('9009373')#egorkreed
	log.unfollow('3667119749')#karnaval
	log.unfollow('1829634788')#dava
	log.unfollow('2485931655')#a4
	log.unfollow('705805118')#morgenshtern
	log.unfollow('1098513252')#karinakross
	log.unfollow('1388636732')#adushkina
	print('отписался')
	time.sleep(20)
	continue

