'''
Write a Python Program to Open the url using urllib library
'''
import urllib.request

site = urllib.request.urlopen("https://uit.stanford.edu/service/techtraining/class/fundamentals-big-data-live-online")
code = site.getcode()
print(code)