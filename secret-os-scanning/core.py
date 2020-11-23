from plugins.aws_creds import AWSCreds
from plugins.ssh import SSHKeys
from plugins.wordpress import WPCheck
from plugins.passwd import Passwd
from plugins.git import Gitcred
from plugins.mysql import Mysqlcred
import os
import re
import datetime


results = AWSCreds()
sshresult = SSHKeys()
wpresult = WPCheck()
passwdres = Passwd()
gitres = Gitcred()
mysqlcheck = Mysqlcred()

print(results.result)
print(sshresult.result)
print(wpresult.result)
print(passwdres.result)
print(gitres.result)
print(mysqlcheck.result)

def print_header(text):
    print("---------")
    print(text)
    print("---------")

def find_SSH_host_keys(base_path="/"):
    '''
    Searches for SSH host keys
    '''

    ssh_hk_dir = os.path.join(base_path, "etc", "ssh")
    pattern = "ssh_host_.*"
    found_list = []
    for root, dirs, files in os.walk(ssh_hk_dir):
        for file in files:
            if (re.match(pattern, file) != None):
                path = os.path.join(root, file)
                stat = os.stat(path)
                fileage = datetime.fromtimestamp(stat.st_mtime)
                now = datetime.now()
                delta = now - fileage

                total_seconds = (delta.microseconds + (delta.seconds + delta.days * 24 * 3600) * 10 ** 6) / 10 ** 6

                found_list.append([path, file, total_seconds])

    return found_list


def output_SSH_host_keys(findings):
    '''
    Prints the SSH host keys in the /etc/ssh folder on the screen
    '''

    print_header("SSH Host keys")

    if len(findings) > 0:
        print("The following files contain keys for SSH host authentication:")

        for entry in findings:
            print(entry[0] + " (age of file is " + str(entry[2]) + " seconds)")

        print("")
        print("P: Do not include these files into the published AMI.")
        print("C: Check that these files have been freshly generated.")
        print("")
    else:
        print("")
        print("None.")
        print("")
#tool_path = /Users/prakashashok/Desktop/secret-os-scanning/
#root_path = /var/root
#ssh_path = /.ssh