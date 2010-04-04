import unittest
import coverage
from unittest import TestResult
import os
import importlib

def find_test_paths(startDir="tests"):
    result = []
    directories = [startDir]
    while len(directories)>0:
        directory = directories.pop()
        for name in os.listdir(directory):
            fullpath = os.path.join(directory,name)
            if os.path.isfile(fullpath) and name.startswith("test"):
                result.append(fullpath)
            elif os.path.isdir(fullpath):
                directories.append(fullpath)
    return result

test_paths = find_test_paths()

cov = coverage.coverage()
cov.start()

loaded = set()
suite = unittest.TestSuite()
for module in test_paths:
    mod = importlib.import_module(''.join(module.split(".")[:-1]).replace("\\", "."))
    exec("import {}".format(mod.__name__))
    for c in dir(mod):
        if c.startswith("Test"):
            fullname = mod.__name__ + "." + c
            testclass = eval(fullname)
            if testclass not in loaded:
                loaded.add(testclass)
            suite.addTest(unittest.TestLoader().loadTestsFromTestCase(testclass))
    # test_searching

result = TestResult()
suite.run(result)
print(result)
cov.stop()
cov.report()
cov.html_report(directory="cov_html")
