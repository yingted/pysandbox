from __future__ import absolute_import
import sys

class SetRecursionLimit(object):
    def __init__(self):
        self.old_limit = sys.getrecursionlimit()

    def enable(self, sandbox):
        self.old_limit = sys.getrecursionlimit()
        sys.setrecursionlimit(sandbox.config.recusion_limit)

    def disable(self, sandbox):
        sys.setrecursionlimit(self.old_limit)
