#!/usr/bin/env python

import sys
import json
import requests

# Check if all parameters provided & exit if not
if len(sys.argv) < 4:
	print '{} <url> <source> <target>'.format(sys.argv[0])
	sys.exit(1)

# Init variables
in_progress = False

# Extract parameters
(url, source, target) = sys.argv[1:4]

# Extract login & password from cozy config
(username, password) = map(lambda s: s.strip(), open('/etc/cozy/couchdb.login').readlines())

# Get all replications
replications = requests.get('{}/_active_tasks'.format(url), auth=(username, password)).json()

# Check all replications to found right one
for replication in replications:
	repl_type = replication['type']
	repl_source = replication['source']
	repl_target = replication['target']
	# If it's the right one & save progress status variable
	if (repl_type == 'replication' and repl_source == source and repl_target == target):
		in_progress = True

# Launch sync if not in progress
if in_progress:
	print 'In progress'
else:
	print 'Need to launch sync'
	payload = {
		'source': source,
		'target': target,
		'continuous': True
	}
	headers = { 'Content-type': 'application/json' }
	print requests.post('{}/_replicate'.format(url),
			json=payload,
			headers=headers,
			auth=(username, password)).json()
