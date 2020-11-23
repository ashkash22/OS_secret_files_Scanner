from helpers.get_home import get_home
from helpers.base_plugin import BasePlugin
import subprocess
import re


class AWSCreds(BasePlugin):

    def run(self):
        cmd = ['cat', f'{get_home()}/.aws/credentials']
        self.output = subprocess.check_output(cmd)
        return self.output

    def check_output(self):
        regex = '(?<![A-Za-z0-9/+=])[A-Za-z0-9/+=]{40}(?![A-Za-z0-9/+=])'
        data = re.findall(regex.encode(), self.output)
        if len(data) > 0:
            self.result["vulnerable"] = True
            self.result["patterns_found"] = data
            self.result["check"] = "aws_check"
