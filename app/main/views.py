from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_source,get_articles
from ..models import Source,Articles

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data i.e news source
    '''
    general = get_source('general')
    science = get_source('science')
    business = get_source('business')
    technology = get_source('technology')
    health = get_source('health')
    entertainment = get_source('entertainment')
    sports = get_source('sports')

    return render_template('index.html',general = general, science = science, business = business,technology = technology, health = health, entertainment = entertainment, sports = sports)


@main.route('/sources/<id>')
def articles(id):
	'''
	view articles page
	'''
	articles = get_articles(id)

	return render_template('articles.html',articles = articles)
