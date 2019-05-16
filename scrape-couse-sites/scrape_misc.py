from ScrapeSiteMap import SiteMapScrapper
 
def main():
	sms = SiteMapScrapper()
	eduSiteFile = open("eduSites.txt")
	lines = eduSiteFile.readlines()
	sites = [line.rstrip("\n") for line in lines]
	siteMapLst =  [sms.getSiteMapUrl(x) for x in sites ]
	print siteMapLst
if __name__ == "__main__":
	main()
