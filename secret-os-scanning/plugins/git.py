from helpers.get_home import get_home
from helpers.base_plugin import BasePlugin
import subprocess
import re


class Gitcred(BasePlugin):

    def run(self):
        cmd_wp_pass = ['cat', f'{get_home()}/.git/credentials']
        self.output = subprocess.check_output(cmd_wp_pass)
        return self.output

    def check_output(self):
        regexs = 'sshpass|password|pwd|passwd|pass'
        #SECRET[\\-|_|A-Z0-9]*(\'|\")?(:|=)(\'|\")?[\\-|_|A-Z0-9]{10}
        #'(ftp|ftps|http|https)://[A-Za-z0-9-_:\.~]+(@)'
        data2 = re.findall(regexs.encode(), self.output)
        if len(data2) > 0:
            self.result["vulnerable"] = True
            self.result["patterns_found"] = data2
            self.result["check"] = "git_pass_check"