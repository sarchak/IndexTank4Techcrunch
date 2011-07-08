#! /usr/bin/python
import sys;
import string;
import re;
import urllib;
from indextank.client import ApiClient;
indexapi = ApiClient('http://:7Xwa4xmDZZsyFG@d6nwu.api.indextank.com');
index = indexapi.get_index('techcrunch');
query = "text:"+sys.argv[1]+" OR company:"+sys.argv[1];
#results = index.search(query);
results = index.search(query,fetch_fields=['text','company','homepage_url','category_code','number_of_employees'], 
                                  snippet_fields=['category_code']);
#results = index.search(query);
#print results;
#results = index.search('%s category_code:%s' % (query,category_code))
for doc in results['results']:
    print "Company:" + doc['company']; 
    print "Website:" + doc['homepage_url'].strip("\n"); 
    print "Category:" + doc['category_code']; 
    print "Number of Employees:" + doc['number_of_employees']; 
    print "---"
