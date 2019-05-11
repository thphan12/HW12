{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Imports & Dependencies\n",
    "from splinter import Browser\n",
    "from bs4 import BeautifulSoup\n",
    "executable_path = {'executable_path': '/usr/local/bin/chromedriver'}\n",
    "browser = Browser('chrome', **executable_path, headless=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "def scrape():\n",
    "    final_data = {}\n",
    "    output = marsNews()\n",
    "    final_data[\"mars_news\"] = output[0]\n",
    "    final_data[\"mars_paragraph\"] = output[1]\n",
    "    final_data[\"mars_image\"] = marsImage()\n",
    "    final_data[\"mars_weather\"] = marsWeather()\n",
    "    final_data[\"mars_facts\"] = marsFacts()\n",
    "    final_data[\"mars_hemisphere\"] = marsHem()\n",
    "\n",
    "    return final_data\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "def marsNews():\n",
    "    news_url = \"https://mars.nasa.gov/news/\"\n",
    "    browser.visit(news_url)\n",
    "    html = browser.html\n",
    "    soup = BeautifulSoup(html, \"html.parser\")\n",
    "    article = soup.find(\"div\", class_='list_text')\n",
    "    news_title = article.find(\"div\", class_=\"content_title\").text\n",
    "    news_p = article.find(\"div\", class_ =\"article_teaser_body\").text\n",
    "    output = [news_title, news_p]\n",
    "    return output\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def marsImage():\n",
    "    image_url = \"https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars\"\n",
    "    browser.visit(image_url)\n",
    "    html = browser.html\n",
    "    soup = BeautifulSoup(html, \"html.parser\")\n",
    "    image = soup.find(\"img\", class_=\"thumb\")[\"src\"]\n",
    "    featured_image_url = \"https://www.jpl.nasa.gov\" + image\n",
    "    return featured_image_url"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def marsWeather():\n",
    "    \n",
    "import tweepy\n",
    "\n",
    "from key_vault import (consumer_key, \n",
    "                    consumer_secret, \n",
    "                    access_token, \n",
    "                    access_token_secret)\n",
    "\n",
    "auth = tweepy.OAuthHandler(consumer_key, consumer_secret)\n",
    "auth.set_access_token(access_token, access_token_secret)\n",
    "api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())\n",
    "target_user = \"marswxreport\"\n",
    "full_tweet = api.user_timeline(target_user , count = 1)\n",
    "mars_weather=full_tweet[0]['text']\n",
    "mars_weather"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def marsFacts():\n",
    "    import pandas as pd\n",
    "    facts_url = \"https://space-facts.com/mars/\"\n",
    "    browser.visit(facts_url)\n",
    "    mars_data = pd.read_html(facts_url)\n",
    "    mars_data = pd.DataFrame(mars_data[0])\n",
    "    mars_data.columns = [\"Description\", \"Value\"]\n",
    "    mars_data = mars_data.set_index(\"Description\")\n",
    "    mars_facts = mars_data.to_html(index = True, header =True)\n",
    "    return mars_facts"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
