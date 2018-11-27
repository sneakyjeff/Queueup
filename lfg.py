import requests
import time
import csv
from bs4 import BeautifulSoup



def getLFGUsers():
	url = "http://www.destinylfg.net/"
	url_data = requests.get(url)
	url_data_parsed = BeautifulSoup(url_data.text, 'html.parser')
	print(url_data_parsed)

	number_of_players = url_data_parsed.find("span", id="online-counter")
	print(number_of_players.text)

def get_active_users(subreddit):
    url = "http://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url)
    content = response.json()
    return content["data"]["accounts_active"]

def main():
	while(True):

		value = get_active_users('leagueconnect')

		with open('workbook.csv', 'a') as csvfile:
			fieldnames = ['subreddit', 'time', '# users']
   			writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
			writer.writerow({'subreddit': 'leagueconnect', 'time': time.ctime(), '# users': value})

		
		print('league connect users at: ' + time.ctime() + ' - ' + str(value))		
		time.sleep(3600)


main()
getLFGUsers()
