import csv
from datetime import datetime

def generate_post(title, level, youtubeid, filename, name):
    of = open(filename,"w")
    of.write("---"+ "\n")
    of.write('title: ' + title.replace(":", ".") + "\n")
    of.write('categories:'+ "\n")
    of.write('  - video'+ "\n")
    of.write('tags:'+ "\n")
    of.write('  - USACO ' + level+ "\n")
    of.write('  - VIDEO ' + "\n")
    #of.write('permalink: ' + name.lower() +"\n")
    of.write('---'+ "\n")
    of.write('  '+ "\n")
    of.write('## ' + title + "  \n")
    of.write('  '+ "\n")
    of.write('{{% include video id="{id}" provider="youtube" %}}' .format(id = youtubeid)+ "\n")
    of.write('  '+ "\n")
    of.write('  '+ "\n")
    of.write('{% highlight C++ linenos %}'+ "\n")
    of.write('  '+ "\n")
    of.write('{% endhighlight %}  '+ "\n")
    of.write(''+ "\n")
    of.close()

def generate_table(namelist, filename):
    of = open(filename, "w")
    of.write("""---
title: "Video Tutorials for USACO Questions"  
layout: tag  
permalink: /usacovideo/  
author_profile: true  
---
![](/assets/images/USACObessieheader.PNG)

## USACO: A Story About Farmer John and Bessie the Cow  

Farmer John is the well acclaimed owner of many cows. But one of them always gets into mischief! Help Farmer John deal with Bessie the cow, using programs to assist them on their journey on the [USACO](http://usaco.org/) site.


""")
    Gold = []
    Bronze = []
    Silver = []
    for n in namelist:
        if n[2] == 'Gold':
            Gold.append(n)
        if n[2] == "Silver":
            Silver.append(n)
        if n[2] == "Bronze":
            Bronze.append(n)
    levels = ['Gold', 'Silver', 'Bronze']
    levels.reverse()
    for x in levels:
        of.write("""  \n## """ + x + """ Questions
    
| Name   |  Year   | P# | Contest |  
|--------|---------|----|---------|  
""")
        for n in eval(eval('x')):
            for i in range(len(n[0].split()) - 1):
                if n[0].split()[i][0] == "P":
                    break
            if i == 4:
                contest = n[0].split()[3]
            else:
                contest = " ".join(n[0].split()[3:5])
            # url = n[1].lower().replace("december", "dec").replace("january", 'jan').replace("february", 'feb').split("_")
            # url[1], url[2] = url[2], url[1]
            # url = url[:i + 1]
            # url = "_".join(url)
            # "video/usacovideo-usaco-2018-gold-us-open-p3/"
            of.write('| [' + " ".join(n[0].split()[i + 1:]) + '](/video/usacovideo-' + n[1].lower().replace('_','-') + ') | ' + n[3] + ' | ' +
                     n[0].split()[i][:2] + ' | ' + contest + ' |   \n')
    of.close()

namelist = []
with open('youtube.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        title = row[0]
        id    = row[1]
        name = title.replace('.', ':').replace('-',' ')
        name  = name.split(':')[0].replace('.','').replace(' ', "-").lower()
        date  = datetime.today().strftime('%Y-%m-%d')
        filename = 'output/'+ date + '-usacovideo-' + name + ".md"
        level = title.split()[2]
        year = title.split()[1]
        namelist.append([title, name,  level, year])
        print(title, id, title.split()[2], filename)
        generate_post(title, title.split()[2], id, filename, '/'+name.replace('_','-'))

generate_table(namelist, "usacovideo.md")
