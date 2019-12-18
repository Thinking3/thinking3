import re
import time

url = raw_input("Please input the article url: ")
weibo_name = raw_input("Please input the weibo name: ")
createFilename = weibo_name + '.py'

with open('Example.py', 'r') as f, open(createFilename, 'w') as des:
    for testline in f.readlines():
        if(re.match('url', testline)):
            testline = 'url = "' + url + '"'
        if(re.match('with open', testline)):
            testline = 'with open(\'/usr/share/nginx/html/data/' + weibo_name + '.csv\', \'a\') as f:'
        des.writelines(testline)
f.close()
des.close()

with open('NewTask_2minutes_per.sh', 'a') as f:
	currentTime = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
	f.writelines("# created at " + currentTime + "\n")
	f.writelines("python " + createFilename + "\n")
f.close()

