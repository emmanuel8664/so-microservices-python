
from subprocess import Popen, PIPE


def get_all_users():
  grep_process = Popen(["grep","/bin/bash","/etc/passwd"], stdout=PIPE, stderr=PIPE)
  user_list = Popen(["awk",'-F',':','{print $1}'], stdin=grep_process.stdout, stdout=PIPE, stderr=PIPE).communicate()[0].split('\n')
  return filter(None,user_list)

def add_user(username,password):
  add_process = Popen(["sudo","adduser","--password",password,username], stdout=PIPE, stderr=PIPE)
  add_process.wait()
  return True if username in get_all_users() else False

def remove_user(username):
  vip = ["operativos","jenkins","postgres","root","ruby","python"]
  if username in vip:
    return True
  else:
    remove_process = Popen(["sudo","userdel","-r",username], stdout=PIPE, stderr=PIPE)
    remove_process.wait()
    return False if username in get_all_users() else True

def recently_logged():
        lastlog = Popen(["lastlog","-b","0","-t","1"] , stdout=PIPE, stderr=PIPE)
        usernames = Popen(["awk", "{print $1}"], stdin=lastlog.stdout, stdout=PIPE, stderr=PIPE).communicate()[0].split('\n')     
	return usernames

def user_info(in_user):        
	user = "" + in_user
	user_info = Popen(["id", user ], stdout=PIPE, stderr=PIPE)
	user_info.wait()
	result = user_info.communicate()[0]
        return result

def user_commands(user):
	line = "/home/"+user+"/.bash_history"
	commands = Popen([ "tail", line], stdout=PIPE, stderr=PIPE).communicate()[0].split('\n')
	return commands
