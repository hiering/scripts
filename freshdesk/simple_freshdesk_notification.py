#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json

import ctypes

api_key = ""
domain = ""
password = ""

r = requests.get("https://"+ domain +".freshdesk.com/api/v2/tickets", 
	auth = (api_key, password))

response = json.loads(r.content)

for i in response:
	if i["responder_id"] == 27000113598:
		pass
		# notification
