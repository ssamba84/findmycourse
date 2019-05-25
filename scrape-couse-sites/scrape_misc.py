from ScrapeSiteMap import SiteMapScrapper
def printsiteMaps(siteMapMap):
	for site, sitemap in siteMapMap.items():
		print(site + " : " + ",".join(sitemap)) 
def main():
	sms = SiteMapScrapper()
	eduSiteFile = open("eduSites.txt")
	lines = eduSiteFile.readlines()
	sites = [line.rstrip("\n") for line in lines]
	siteMapMap =  dict([(x, sms.getSiteMapUrl(x)) for x in sites ])
	printsiteMaps(siteMapMap)
if __name__ == "__main__":
	main()
