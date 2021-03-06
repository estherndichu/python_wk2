import urllib.request,json
from .models import Source,Articles
from datetime import datetime


api_key = None

base_url = None

articles_url = None

def configure_request(app):
	global api_key,base_url,articles_url
	api_key = app.config['API_KEY']
	base_url = app.config['SOURCE_BASE_URL']
	articles_url = app.config['ARTICLE_BASE_URL']


def get_source(category):
	'''
	Function that returns json reponse to url request
	'''
	get_source_url = base_url.format(category,api_key)

	with urllib.request.urlopen(get_source_url) as url:
		get_source_data = url.read()
		get_source_response = json.loads(get_source_data)

		source_results = None

		if get_source_response['sources']:
			source_results_list = get_source_response['sources']
			source_results = process_source(source_results_list)

	return source_results

def process_source(source_list):
	'''
	Function that processes the news sources results and returns source list
	'''

	source_results = []

	for source_item in source_list:
		id = source_item.get('id') 
		name = source_item.get('name')
		description = source_item.get('description')
		url = source_item.get('url')
		category = source_item.get('category')
		language = source_item.get('language')
		country = source_item.get('country')


		source_object = Source(id,name,description,url,category,country,language)
		source_results.append(source_object)


	return source_results    

def get_articles(id):
  '''
	Function that processes the articles and returns a list of articles
	'''
		
  get_articles_url = articles_url.format(id,api_key)

  with urllib.request.urlopen(get_articles_url) as url:
			articles_results = json.loads(url.read())

			articles_object = None
			if articles_results['articles']:
				articles_object = process_articles(articles_results['articles'])

			return articles_object

def process_articles(articles_list):
  
	articles_object = []
	
	for article_item in articles_list:
		id = article_item.get('id')
		author = article_item.get('author')
		title = article_item.get('title')
		description = article_item.get('description')
		url = article_item.get('url')
		image = article_item.get('urlToImage')
		date = article_item.get('publishedAt')
		
		if image:
			articles_result = Articles(id,author,title,description,url,image,date)
			articles_object.append(articles_result)		