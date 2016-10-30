import telepot
import time
import requests
import urllib
import urllib2
import json
from watson_developer_cloud import NaturalLanguageClassifierV1

#natural_language_classifier = NaturalLanguageClassifierV1(
#	username = ''
#	password= ''
#)

welcomeMsg = 'Welcome to TravelBot. It sends you latest ticket prices,tempratures of the places you want to visit, the activities you can do there and the best possible suitable packages for your needs! Type /help for more info.'

helpMsg = '1. Type "tickets" deparure destination for tickets 2. Type "weather" destination for weather 3. Type "Activities" destination to see the activities in that area'

ticks = 'tickets'
acts = 'activities'
packs = 'packages'
temp = 'weather'
def handle(msg):
	print msg
	chat_id = msg['from']['id']
	command = msg['text']
	if command == '/start':
		bot.sendMessage(chat_id,welcomeMsg)
		return 
		
	if command == '/help':
		bot.sendMessage(chat_id,helpMsg)
		return 
	if ticks.lower() in command.lower():
		bot.sendMessage(chat_id,'Tickets')
		first_word = command.split()[0]
		second_word = command.split()[1]
		third_word = command.split()[2]
		bot.sendMessage(chat_id,'Hey here is your link\n'+'http://www.britishairways.com/en-gb/destinations/'+second_word+'/flights-to-'+second_word)
		
		return 	
	if temp.lower() in command.lower():
		bot.sendMessage(chat_id,'Weather')
		first_word = command.split()[0]
		second_word = command.split()[1]
		url = 'http://api.openweathermap.org/data/2.5/forecast/Moscow?id=524901&APPID=a26524e13fd724411501e93ef445f9bc'
		weatherdata=urllib2.urlopen(url)
		response=json.load(weatherdata)
		maxi=response['list'][0]['main']['temp_max']
		mini=response['list'][0]['main']['temp_min']
		bot.sendMessage(chat_id,'Maximum Temprature in '+second_word+' is'+str(maxi)+'K and minimum is '+str(mini)+'K' )		bot.sendMessage(chat_id,'Temprature in '+second_word+' is http://openweathermap.org/find?q='+second_word)
		return 
		
	if acts.lower() in command.lower():
		bot.sendMessage(chat_id,'Activities')
		first_word = command.split()[0]
		second_word = command.split()[1]
		bot.sendMessage('Here are your list of activities !\n https://www.timeout.com/'+second_word+'/en/things-to-do')

		return 
	if packs.lower() in command.lower():
		bot.sendMessage(chat_id,'Packages')
		first_word = command.split()[0]
		second_word = command.split()[1]
		url = 'http://terminal2.expedia.com/x/packages?departureDate=2016-10-02&originAirport=SEA&destinationAirport=LHR&returnDate=2016-10-09&regionid=6000479&apikey=taOzcHFB0CATpL0MKlWSnhlw8MXnQy6j'
		data = json.load(urllib2.urlopen(url))
		bot.sendMessage(chat_id,'Thompson,2229LC,\n Fairmount Olympic 2524LC,\n Hotel FIVE 7802LC, Marquee Hotel 1765LC,\n The Roosevelt 1857LC')
		return
		
		
bot = telepot.Bot('YOUR ID HERE')
bot.message_loop(handle)
print 'listening'

while 1:
	time.sleep(10)
	
