import requests


class Guardian:
    def __init__(self, guardian_key, url):
        self.guardian_key = guardian_key
        self.url = url+guardian_key

    def get_articles(self):
        response = requests.get(self.url)
        news = response.json()
        returned_articles = []

        if response:
            results = news['response']['results']
            for x in range(0, 5):
                returned_articles.append(results[x]['webTitle'])
                print(results[x]['webTitle'])
            return returned_articles
        else:
            returned_articles.append('An error has occurred.')
            return returned_articles
