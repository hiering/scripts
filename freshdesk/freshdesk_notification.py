#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import eventlet
import requests
import json
import time

import ctypes

domain = "radymo"
api_key = "You API-key"
password = "You password"

def notification():
	user32 = ctypes.windll.LoadLibrary('user32.dll')
	user32.MessageBoxW(0, 'Нова заявка', 'Freshdesk', 0)

def get_data():
	timeout = eventlet.Timeout(10)
	try:
		data = requests.get("https://"+ domain +".freshdesk.com/api/v2/tickets", 
			auth = (api_key, password))
		return data
	except eventlet.timeout.Timeout:
		return None
	finally:
		timeout.cancel()

def check_tickets():
	data = get_data()
	if not data is None:
		tickets = json.loads(data.content)
		for i in tickets:
			if i["responder_id"] == None:
				notification()
				break

def main():
	while True:
		check_tickets()
		time.sleep(60 * 5)


if __name__ == "__main__":
	main()
