from django.shortcuts import render
import requests
import re
from urllib.parse import urlparse, urljoin

# Create your views here.

def web_request(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass

def main(request):
    target_url = request.GET['url']
    response = web_request(target_url)
    result = response.content.decode('utf-8')
    href_links = re.findall('(?:href=")(.*?)"', result)
    return render(request, "result.html", {'output':href_links})