# csv2geojson
Générate geoJSON files from CSV table.

####Synopsis
Script to convert a CSV table with a given structure to a set of geoJSON files, ready to be imported into OpenStreetMap(http://umap.openstreetmap.fr/).

####Usage

	csv2geojson.py data.csv
	  
####CSV columns expected in input file :

- Nom
- Secteur d'activité
- Description
- Adresse
- Commune
- Mél
- Site Web
- Page FB
- Tél 1
- Tél 2
- Comptoir d'éch.
- Inclus annuaire (optional)
- Inclus Site (optional)
- Inclus Carte (optional)
- Latitude
- Longitude

####Output

- A geoJSON file per value of the *Secteur d'activité* column with the geoJSON structure of the lines of the CSV file matching this value.
- An additionnal file : *Comptoirs d'échange*  with the geoJSON structure of the lines where the *Comptoir d'échange* is set to *Oui*.


