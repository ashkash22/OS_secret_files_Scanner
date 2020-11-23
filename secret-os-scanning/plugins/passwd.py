from helpers.get_home import get_home
from helpers.base_plugin import BasePlugin
import subprocess
import re


class Passwd(BasePlugin):

    def run(self):
        cmd_passwd = ['cat', '/etc/passwd']
        self.output = subprocess.check_output(cmd_passwd)
        return self.output

    def check_output(self):
        regexs = 'root:[x*]:0:0:'
        data3 = re.findall(regexs.encode(), self.output)
        if len(data3) > 0:
            self.result["vulnerable"] = True
            self.result["patterns_found"] = data3
            self.result["check"] = "passwd_check"

