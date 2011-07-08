#! /usr/bin/python
import string;
import re;
import urllib;
f = open("companies.txt");
fw = open("intermediate.txt", 'w');
for line in f :
    p = re.compile(r'{"name":');
    list = p.split(line.rstrip('"\n'));
    if len(list) > 1:
        url = "http://api.crunchbase.com/v/1/company/" + list[1].rstrip('",').lstrip(' "')+".js" ;
        print url;
        print "Company:" + list[1].rstrip('",').lstrip(' "');
        fw.write("Company:" + list[1].rstrip('",').lstrip(' "')+"    ");
        page = urllib.urlopen(url);
        buf = page.read();
        if re.search("error",buf) :
            fw.write("\n");
            continue;
        ext = re.compile('("homepage_url"):(.*)|("category_code"):(.*)|("number_of_employees"):(.*)');
        print ext.search(buf).group(1) + ":" + ext.search(buf).group(2);
f.close();
