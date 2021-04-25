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

def generate_table(contest, year):
        for i in range(len(n[0].split()) - 1):
            if n[0].split()[i][0] == "P":
                break

            contest = " ".join(n[0].split()[3:5])
        # url = n[1].lower().replace("december", "dec").replace("january", 'jan').replace("february", 'feb').split("_")
        # url[1], url[2] = url[2], url[1]
        # url = url[:i + 1]
        # url = "_".join(url)
        # "video/usacovideo-usaco-2018-gold-us-open-p3/"
        print('| [' + " ".join(n[0].split()[i + 1:]) + '](/video/usacovideo-' + n[1].lower().replace('_','-') + ') | ' + n[3] + ' | ' +
                 n[0].split()[i][:2] + ' | ' + contest + ' |   \n')

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
