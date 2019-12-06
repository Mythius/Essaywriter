from selenium import webdriver


file = 'here.txt';

f = open(file,'r')
t = f.read()

text = t.split('\n')[0]

deep = t.split('\n')[1]

with open(file,'w') as f:
	f.write('')

driver = webdriver.Chrome(r"C:/Users/south/Applications/chromedriver.exe")

subject = text

driver.get('https://en.wikipedia.org/wiki/'+text)


def organize(r):
	s = r.split('\n')

	if not deep == 'true':
		f = list(filter(lambda x: not  "." in x,s))
	else: 
		f = list(s)

	f = f[1:]


	data = []


	for i in f:
		prev = i[i.find('\t'):].strip()
		if(prev == 'See also' or prev == 'References' or prev == 'Footnotes' or prev == 'External links'):
			return data
		try:
			driver.get('https://www.google.com/search?q='+subject+'+'+prev)
			t1 = driver.execute_script("return document.querySelector('.st').innerText")
			t2 = driver.execute_script("return document.querySelectorAll('.st')[1].innerText")
			data.append(prev + ':\n' + t1 + '\n' + t2 + '\n\n')
		except:
			print('Failed to research: '+i)

	return data

try:
	result = driver.execute_script('return document.querySelector(".toc").innerText')
	result = organize(result)
except: 
	result = 'Try Rewording Topic....'


with open(file,"a") as f:
	for l in result:
		try:
			f.write(l)
		except:
			f.write('<Write Error>\n')



with open('done.txt',"w") as f:
	f.write('true')

driver.quit()

#input('Click ENTER to Exit')