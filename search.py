#! /usr/bin/python
import sys;
import string;
import re;
import urllib;
from indextank.client import ApiClient;
indexapi = ApiClient('http://:7Xwa4xmDZZsyFG@d6nwu.api.indextank.com');
index = indexapi.get_index('Techcrunch');
query = sys.argv[1];
results = index.search(query,fetch_fields=['text','homepage_url','category_code','number_of_employees'], 
                                  snippet_fields=['phone']);
print results;
for doc in results['results']:
    print "Company:" + doc['text']; 
    print "Website:" + doc['homepage_url'].strip("\n"); 
    print "Category:" + doc['category_code']; 
    print "Number of Employees:" + doc['number_of_employees']; 
    print "---"
