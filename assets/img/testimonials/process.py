import urllib2

reasons = {'good':[
['report by victim', 'https://static.pexels.com/photos/4970/fashion-person-woman-hand-medium.jpg'],
['suspicion of weapons','https://static.pexels.com/photos/34552/pexels-photo-medium.jpg'],
['proximity to scene of offense','https://static.pexels.com/photos/26432/pexels-photo-26432-medium.jpg'],
['carrying suspicious object','https://static.pexels.com/photos/26432/pexels-photo-26432-medium.jpg'] ],
'bad':[
['ongoing investigation','https://static.pexels.com/photos/132752/pexels-photo-132752-medium.jpeg'],
['actions of engaging in a violent crime','https://static.pexels.com/photos/8827/road-man-lights-legs-large.jpg'],
['inappropriate attire for season','https://static.pexels.com/photos/47486/pexels-photo-47486.jpeg'],
['wearing clothes commonly used in a crime','https://static.pexels.com/photos/175730/pexels-photo-175730-medium.jpeg'],
['acting as a lookout','https://static.pexels.com/photos/47446/pexels-photo-47446-medium.jpeg']
]}

for qual in reasons:
	for reason in reasons[qual]:
		req = urllib2.Request(reason[1], headers={'User-Agent' : "Magic Browser"})
		con = urllib2.urlopen( req )
		locname = reason[0].replace (" ", "_")
		with open(locname+".jpg",'wb') as f:
			f.write(con.read())
			f.close()
		print """
				            <div class="portfolio-box %s">
			                	<img src="assets/img/testimonials/%s.jpg" alt="" data-at2x="assets/img/testimonials/%s.jpg">
			                	<div class="portfolio-box-text-container">
			                		<div class="portfolio-box-text">
			                			<p><a href="#">%s</a></p>
			                		</div>
			                	</div>
			                </div>""" % (qual, locname, locname, reason[0])
