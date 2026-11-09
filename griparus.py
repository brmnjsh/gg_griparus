import csv
import getopt
import sys
import time

import requests

# reference format
# {
#   "date_time": "2026-11-09T20:23:06+00:00",
#   "gripper": "micro",
#   "side": "right",
#   "weight_lbs": 45,
#   "reps": [
#     51
#   ]
# }

args = sys.argv[1:]
options = "ht:"
long_options = ["Help", "Token="]

try:
    arguments, values = getopt.getopt(args, options, long_options)
    for currentArg, currentVal in arguments:
        if currentArg in ("-h", "--Help"):
            print("-t (--Token): the gripgains.ca request header Authorization token you can get when making various requests. It is required to get your data. See README for further details.")
        elif currentArg in ("-t", "--Token"):
            print("requesting gripper metrics...")
            # grab data from json and convert to array of dics
            # pulling from url
            token = currentVal
            headers = {
                "Authorization": token
            }
            response = requests.get('https://gripgains.ca/api/metrics?sessions=all', headers=headers)
            grip_sessions = response.json()['metrics']

            filter_fields=['date_time','gripper','reps','weight', 'side']
            gripper_metrics = []

            # sort grip sessions and grab required keys
            for grip_session in grip_sessions:
                grip_session_data = { key: grip_session[key] for key in grip_session if key in filter_fields}
                gripper_metrics.append(grip_session_data)

            # convert to csv and save for use to import to powercurve
            print("generating csv...")
            keys = gripper_metrics[0].keys()
            timestr = time.strftime("%Y%m%d-%H%M%S")
            with open(f"runs/gripper-sessions-{timestr}.csv", 'w', newline='') as output_file:
                dict_writer = csv.DictWriter(output_file, keys)
                dict_writer.writeheader()
                dict_writer.writerows(gripper_metrics)

            print("csv succesfully created!")
        else:
            print("token required, see documentation for further details")
except getopt.error as err:
    print(str(err))
