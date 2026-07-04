#!/usr/bin/env python3

import json
import yaml

config = {
	"server": "prod",
	"port": 80,
	"Status": "active"
}

with open ("config.json", "w") as json_file:
	json.dump(config, json_file, indent = 4)

with open ("config.json", "r") as json_file:
	config = json.load(json_file)

config["Status"] = "maintenance"

with open ("config.yaml", "w") as yaml_file:
	yaml.dump(config, yaml_file, sort_keys = False)

