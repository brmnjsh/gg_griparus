# Griparius
gripgains sessions export for personal use

Like Icarus before him, griparus is attempting to fly too close to the grip gains sun. May the Hand of God remain merciful during this journey.

## How
- grab your Authorization token from a request header on one of the many requests made to the gripgains.ca backend. XHR endpoints like "metrics?sessions=all" will have this available
- simply pull down the repo, and run the script: `python griparius.py -t "Bearer token_value"`
- be sure to wrap the auth token in quotes or it'll die
  - `python griparius.py -t Bearer token_value` will die
  - `python griparius.py -t "Bearer token_value"` will(should) succeed

## Thanks
Jincs, havinleung
