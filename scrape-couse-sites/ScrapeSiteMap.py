import requests
class SiteMapScrapper:
	def getUrlContent(self, site_url):
		req_resp = requests.get(site_url)
		req_resp.raise_for_status()
		return req_resp.content
	

	def getSiteMapUrl(self, site_url):
		site_map_url_map = None
		try:
			site_robots_file_raw = self.getUrlContent(site_url+"/robots.txt")
			site_robots_file = site_robots_file_raw.replace("\n",",").replace("\r","")
			site_robots_array = site_robots_file.split(",")
			site_map_url_pairs = filter(lambda x: "Sitemap" in x, site_robots_array)
			site_map_url_map = [x.split(":",1)[1] for x in site_map_url_pairs]
		except Exception as e:
			print(e)
		return site_map_url_map
