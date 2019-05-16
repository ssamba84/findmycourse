from ScrapeSiteMap import SiteMapScrapper
'''
def getUrlContent(site_url):
	req_resp = requests.get(site_url)
	req_resp.raise_for_status()
	return req_resp.content
	

def getSiteMapUrl(site_url):
	site_map_url_map = ""
	try:
		site_robots_file_raw = getUrlContent(site_url+"/robots.txt")
		site_robots_file = site_robots_file_raw.replace("\n",",")
		site_robots_array = site_robots_file.split(",")
		site_map_url_map = filter(lambda x: "Sitemap" in x, site_robots_array)[0]
	except Exception as e:
		print(e)
	site_map_url_map = site_map_url_map.split(":",1)
	return site_map_url_map[1].strip() if len(site_map_url_map) == 2 else None
'''
 
def main():
	sms = SiteMapScrapper()
	eduSiteFile = open("eduSites.txt")
	lines = eduSiteFile.readlines()
	#sites = ["https://coursera.org","https://www.udacity.com","https://www.udemy.com"]
	sites = [line.rstrip("\n") for line in lines]
	siteMapLst =  [sms.getSiteMapUrl(x) for x in sites ]
	print siteMapLst
if __name__ == "__main__":
	main()
