#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import csv
import json
import sys

layers={}

with open(sys.argv[1]) as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader :
		activitysectors=[row["Secteur d'activité"]]
		if row["Comptoir d'éch."] == "Oui" :
			activitysectors.append("Comptoirs d'échange")
		for activitysector in activitysectors :
			if not layers.has_key(activitysector) :
				layers[activitysector]={"type" : "FeatureCollection", "features" : []}
		
			name=row["Nom"]
			lon=row["Longitude"].replace(",",".")
			lat=row["Latitude"].replace(",",".")
			if lon == "" or lat == "" :
				continue

			feature={"type" : "Feature", "properties" : {"name" : name}}
			feature["geometry"]={"type" : "Point", "coordinates" : [float(lon), float(lat)]}
			if row["Mél"] != "" :
				feature["properties"]["Courriel"]=row["Mél"]
			if row["Site Web"] != "" :
				web=row["Site Web"]
				if not web.startswith("http") :
					web="http://"+web
				feature["properties"]["Site Web"]=web
			if row["Adresse"] != "" :
				feature["properties"]["Adresse"]=row["Adresse"]
			if row["Description"] != "" :
				feature["properties"]["Description"]=row["Description"]
			if row["Tél 1"] != "" :
				tel=row["Tél 1"]
				if row["Tél 2"] != "" :
					tel=tel+" / "+row["Tél 2"]
				feature["properties"]["Tél"]=tel
			if row["Page FB"] != "" :
				feature["properties"]["FaceBook"]=row["Page FB"]
			feature["properties"]["Commune"]=row["Commune"]
			layers[activitysector]['features'].append(feature)

for layername,features in layers.iteritems() :
	fd=open("%s.json"%layername,"w")
	json.dump(features,fd,sort_keys=True,indent=4)
	fd.close()

