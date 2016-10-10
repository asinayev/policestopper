import urllib2

links={
	'location':'https://assets.dnainfo.com/generated/photo/2013/12/nyc-crime-map-1386541340.jpg/extralarge.jpg',
	#'time':'https://static.pexels.com/photos/9352/glass-time-watch-business-small.jpg',
	#'age':'http://vignette4.wikia.nocookie.net/supernanny/images/d/d8/Agespecific_.jpg/revision/latest?cb=20160415014842',
	#'precinct':'http://animalnewyork.com/wp-content/uploads/2012/04/animalny_precinct.jpg',
	#'transit':'https://static.pexels.com/photos/6563/people-new-york-train-crowd.jpeg',
	#'weight':'https://static.pexels.com/photos/42069/belly-body-calories-diet-42069.jpeg',
	#'indoors':'https://static.pexels.com/photos/451/red-school-blur-factory.jpg',
	#'period':'https://static.pexels.com/photos/9036/pexels-photo.jpg',
	#'uniform':'http://s1.ibtimes.com/sites/www.ibtimes.com/files/styles/lg/public/2014/12/03/nypd-police-body-camera.jpg'
}

for l in links:
	req = urllib2.Request(links[l], headers={'User-Agent' : "Magic Browser"})
	con = urllib2.urlopen( req )
	with open(l+".jpg",'wb') as f:
		f.write(con.read())
		f.close()