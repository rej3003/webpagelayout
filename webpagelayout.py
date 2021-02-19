import os
import time 

HtmIndex = '''
<!DOCTYPE html>
<html>
<head>
test
	<meta charset="UTF-8">
	<title>home page </title>
	<link rel="stylesheet" type="text/css" href="css/style.css">
	<script src="js/script.js"></script>

</head>
<body>

<h1>Home page</h1>
</body>
</html>
'''


jsindex = '''
window.addEventListener('load', () => {
	console.log('The page has loaded')
});
'''




styleindex = '''
*{
    padding: 0;
    margin: 0;
}
h1 {
  color: green;
}
'''




import os
os.mkdir('root')
os.chdir('root')
for each in ('html', 'css', 'js'):
    os.mkdir(each)


f = open("index.html", "a")#firts page 
f.write(HtmIndex)
f.close()




os.chdir('html') #html in folder
f = open("page_2.html", "a")
f.write('html code ')
f.close()



os.chdir('../css') #css in folder
f = open("style.css", "a")
f.write(styleindex)
f.close()





os.chdir('../js') #js in folder
f = open("script.js", "a")
f.write(jsindex)
f.close()
