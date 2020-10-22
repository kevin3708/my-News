import urllib.request,json
from .models import News

apiKey = None

base_url = None

def configure_request(app):
    global apiKey,base_url
    apiKey = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']

def get_news(category):
    '''
    Function that gets the json responce to our url request
    '''
    get_news_url = base_url.format(category,apiKey)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            news_results = process_news(news_results_list)


    return news_results

def process_news(news_list):
    news_results = []
    for news_item in news_list:
        id = news_item.get('id')
        name = news_item.get('name')
        title = news_item.get('title')
        description = news_item.get('description')
        url = news_item.get('url')
        image = news_item.get('urlToImage')
        publishedAt = news_item.get('publishedAt')


        if image:
            news_object = News(id,name,title,description,url,image,publishedAt)
            news_results.append(news_object)

    return news_results

def get_source(id):
    get_source_url = base_url.format(id,apiKey)

    with urllib.request.urlopen(get_source_url) as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)

        source_object = None

        if get_source_response:
            id = get_source_response.get('id')
            name = get_source_response.get('name')
            description = get_source_response.get('description')
            url = get_source_response.get('url')
            category = get_source_response.get('category')
            image = get_source_response.get('urlToImage')
            publishedAt = get_source_response.get('publishedAt')

            source_object = News(id, name, description, url, category, image, publishedAt)

        return source_object

def search_news(news_name):
    search_news_url = 'https://newsapi.org/v2/search/everything?q={}&apiKey={}'.format(category,apiKey)
    with urllib.request.urlopen(search_news_url) as url:
        search_news_data = url.read()
        search_news_response = json.loads(search_news_data)

        search_news_results = None

        if search_news_response['articles']:
            search_news_list = search_news_response['articles']
            search_news_results = process_news(search_news_list)


    return search_news_results