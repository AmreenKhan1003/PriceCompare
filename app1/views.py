from django.shortcuts import render
from selenium import webdriver as wb
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, 'web.html')

def expression(request):
    a = request.GET['text1']
    wbd = wb.Chrome("C:/Users/R computer/Downloads/chromedriver.exe")
    _BASE_URL = "https://www.amazon.in/"
    _BASE_URL2 = "https://www.flipkart.com/"
    #Amazon
    search_url = _BASE_URL + ("s?k=%s" % (a))
    print(search_url)
    wbd.get(search_url)
    price = wbd.find_elements_by_class_name('a-price-whole')
    p1='Amazon Price: ₹' + price[0].text
    l1='Amazon Link: ' + search_url
    #Flipkart
    search_url2 = _BASE_URL2 + ("search?q=%s" % (a))
    wbd.get(search_url2)
    price2 = wbd.find_elements_by_class_name('_1vC4OE')
    p2=' & Flipkart price: ' + price2[0].text
    l2='FLipkart Link: ' + search_url2
    return render(request, 'web.html', {'aprice':p1, 'alink':l1, 'fprice':p2, 'flink':l2})

def abouts(request):
    return render(request, 'about.html')
