from decouple import config
from flask import Flask, render_template

import guardian
import message
import weather

guardian_key = config('GUARDIAN_KEY')
news_url = config('NEWS_URL')
sport_url = config('SPORT_URL')
g_news = guardian.Guardian(guardian_key, news_url)
g_sport = guardian.Guardian(guardian_key, sport_url)

weather_query = config('WEATHER_QUERY')
weather_key = config('WEATHER_KEY')
weather_url = config('WEATHER_URL')
weather = weather.Weather(weather_url, weather_query, weather_key)

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/mirror')
def mirror():
    news = g_news.get_articles()
    sport = g_sport.get_articles()

    forecast = weather.get_weather()

    quote = message.print_message()
    return render_template('mirror.html', quote=quote, news=news, sport=sport, forecast=forecast)


if __name__ == "__main__":
    app.run(debug=True)
