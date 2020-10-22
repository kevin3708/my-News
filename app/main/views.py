from flask import render_template,request,redirect,url_for
from .import main
from ..requests import get_news,get_source,search_news
@main.route('/')
def index():
    sports_news = get_news('sports')
    economy_news = get_news('economy')
    inter_news = get_news('international')
    title = 'Home -Welcome to the best News Website Online'

    search_news = request.args.get('news_query')
    if search_news:
        return redirect(url_for('search',news_name=search_news))
    else:
        return render_template('index.html',title = title, sports = sports_news, economy = economy_news, international = inter_news  )

@main.route('/news/<id>')
def news(id):
    news = get_source(id)
    title = f'{news.name}'
    return render_template('news.html',title = title, news = news)
@main.route('/search/<news_name>')
def search(news_name):
    
    news_name_list = news_name.split(" ")
    news_name_format = "+".join(news_name_list)
    searched_news = search_news(news_name_format)
    title = f'search results for {news_name}'
    return render_template('search.html',news = searched_news)


