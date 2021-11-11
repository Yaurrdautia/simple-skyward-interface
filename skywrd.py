import requests
from bs4 import BeautifulSoup

#edit me
#this is for the lake washington school district. see readme to figure out how to change this.
url = "https://www2.saas.wa-k12.net/scripts/cgiip.exe/WService=wlkwashs71/"

#this is the main page where the login is located. see readme for more details.
programlocation_login = "skyporthttp.w"

#this is where the gradebook is located. see readme for more details.
programlocation_gradebook = "sfgradebook001.w"
##

#adding to the baseurl to make a post request
def makeRequest(program, data):
  r = requests.post(url + program, data)
  return r

header = {}
loginData = {}

setup_stat = False
#getting the names of the teachers and their classes
def setup(username,password):
    global loginData
    global setup_stat
    #acting like a browser that wants data.
    header = {"User-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"}
    #The paylod used to initialize the session
    loginData = {
    'requestAction':'eel',
    'method':'extrainfo',
    'codeType':'tryLogin',
    'codeValue':'login',
    'login':username,
    'password':password
    }
    setup_stat =True

#login to the account and grab the session id
def get_login():
    if setup_stat:
        resp = makeRequest(programlocation_login, loginData)
        #return the formatted data.
        return resp.text.lstrip('<li>').rstrip('</li>').split('^')
    else:
        raise Exception("setup() must be called before get_login()")

#acceprts the output of get_login() and returns relavant information such as session id that is reuired to access the data. 
#This function is for debugging and testing purposes. Also can be used to view data. 
def get_session(session):
    if setup_stat:
        registerData = {
        'dwd':session[0],
        'web-data-recid':session[1],
        'wfaacl-recid':session[2],
        'wfaacl':session[3],
        'nameid':session[4],
        'duserid':session[5],
        'User-Type':session[6],
        'Allow-Special':session[8],
        'displaySecond':session[9],
        'hAutoOpenPref':session[10],
        'insecure':session[11],
        'enc':session[13],
        'encses':session[14]
        }
    #return the formatted data.
        return registerData
    else:
        raise Exception("setup() must be called before get_session()")

#uses the session id and encses to access the gradebook. Returns a messy blob of html.
def get_gradbook_html(session):
    if setup_stat:
        encses = session[14]
        sessionid = session[1] + u'\u0015' + session[2]
        r = makeRequest(programlocation_gradebook, data = {'encses':encses,'sessionid':sessionid})
        return r.text
    else:
        raise Exception("setup() must be called before get_gradbook_html()")

#accepts the html from get_gradbook_html() and retuns a list of classes and teachers.
def get_teachers(gradebook):
    if setup_stat:
        soup = BeautifulSoup(gradebook, 'html.parser')
        tables = soup.findAll('table')
        teachers = []
        for i in tables:
            teachers.append(i.text.strip().split('\n'))
        return teachers
    else:
        raise Exception("setup() must be called before listTeachers()")
