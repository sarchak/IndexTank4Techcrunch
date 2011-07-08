#! /usr/bin/python
import string;
import re;
import urllib;
from indextank.client import ApiClient;
indexapi = ApiClient('http://:7Xwa4xmDZZsyFG@d6nwu.api.indextank.com');
index = indexapi.get_index('Techcrunch');
f = open("companies.txt");
fw = open("intermediate.txt", 'w');
i = 0;
for line in f :
    p = re.compile(r'{"name":');
    list = p.split(line.rstrip('"\n'));
    if len(list) > 1:
        url = "http://api.crunchbase.com/v/1/company/" + list[1].rstrip('",').lstrip(' "')+".js" ;
        print url;
        print "Company:" + list[1].rstrip('",').lstrip(' "');
        companyid = list[1].rstrip('",').lstrip(' "');
        fw.write("Company:" + list[1].rstrip('",').lstrip(' "')+"    ");
        page = urllib.urlopen(url);
        buf = page.read();
        if re.search("error",buf) :
            fw.write("\n");
            continue;
        ext = re.compile('("homepage_url"):(.*)');
        homepage =ext.search(buf).group(2).strip(' "|",')+"\n";
        fw.write(ext.search(buf).group(1).strip('"') + ":" + ext.search(buf).group(2).strip(' "|",')+"        ");
        jobs = ext.search(buf).group(2).rstrip(',"')+"/jobs";
        ext = re.compile('("category_code"):(.*)');
        fw.write(ext.search(buf).group(1).strip('"') + ":" + ext.search(buf).group(2).strip(' "|",')+"    ");
        category = ext.search(buf).group(2).strip(' "|",');
        ext = re.compile('("number_of_employees"):(.*)');
        fw.write(ext.search(buf).group(1).strip('"') + ":" + ext.search(buf).group(2).strip(' "|",')+"\n");
        num_emp = ext.search(buf).group(2).strip(' "|",');
        index.add_document(i, { 'text': companyid, "homepage_url":homepage, "category_code":category,  "number_of_employees":num_emp});
f.close();
