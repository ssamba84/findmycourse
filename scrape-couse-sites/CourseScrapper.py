import requests
import xml.etree.ElementTree as ET
class CourseScrape:
	def __init__(self, site_name, site_map_url):
		self.site_name = site_name
		self.site_map_url = site_map_url
	def getCoursesUrl(self):
		site_map_resp = requests.get(site_map_url)
		site_map_resp.raise_for_status()
		site_map_contents = site_map_resp.content
		
