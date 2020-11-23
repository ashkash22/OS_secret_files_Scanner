from helpers.get_home import get_home
from helpers.base_plugin import BasePlugin
import subprocess
import re


class SSHKeys(BasePlugin):

    def run(self):
        cmd_ssh = ['cat', f'{get_home()}/.ssh/keys/keys']
        self.output = subprocess.check_output(cmd_ssh)
        return self.output

    def check_output(self):
        regexs = '([-]+BEGIN [^\s]+ PRIVATE KEY[-]+[\s]*[^-]*[-]+END [^\s]+ PRIVATE KEY[-]+)'
        data1 = re.findall(regexs.encode(), self.output)
        if len(data1) > 0:
            self.result["vulnerable"] = True
            self.result["patterns_found"] = data1
            self.result["check"] = "ssh_check"
