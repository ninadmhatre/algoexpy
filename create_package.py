__author__ = 'Ninad'


# rename existing package directory
# copy files...
# -- src/*.py
#  -- example/
#  -- docs/
#  -- tests/
#  -- setup.py

import os
import sys
import shutil
import time
from addonpy.addonpyHelpers import AddonHelper

# if sys.argv[1] is None:
#     version_user = raw_input("Please enter version #: ").rstrip()
# else:
#     version_user = sys.argv[1].rstrip()


x_time = time.localtime()
_SUFFIX = "{0}{1}{2}{3}{4}{5}".format(x_time.tm_year,
                                      x_time.tm_mon,
                                      x_time.tm_mday,
                                      x_time.tm_hour,
                                      x_time.tm_min,
                                      x_time.tm_sec)

PACKAGE_DIR = 'package-{0}'.format(_SUFFIX)

CURR_DIR = os.path.abspath('.')
PKG_DIR = os.path.join(CURR_DIR, PACKAGE_DIR, 'pylrn')
SORT_DIR = os.path.join(CURR_DIR, 'Sort')
DS_DIR = os.path.join(CURR_DIR, 'DataStructures')
QUIZ_DIR = os.path.join(CURR_DIR, 'Quiz')

if os.path.isdir(PKG_DIR):
    base_dir = os.path.dirname(PKG_DIR)
    backup_name = base_dir + '.old'
    if os.path.isdir(backup_name):
        shutil.rmtree(backup_name)
    os.rename(base_dir, backup_name)

os.makedirs(PKG_DIR)
print("Created fresh package directory...")

src_list = AddonHelper.walk_dir(CURR_DIR, 'py')

for file in src_list:
    shutil.copy2(file, PKG_DIR)

current_time = time.gmtime()
# v_info = "{0}|[{1}-{2}-{3} {4}:{5}:{6} UTC]".format(version_user,
#                                                     current_time.tm_year,
#                                                     current_time.tm_mon,
#                                                     current_time.tm_mday,
#                                                     current_time.tm_hour,
#                                                     current_time.tm_min,
#                                                     current_time.tm_sec)

shutil.copytree(SORT_DIR, os.path.join(PKG_DIR, 'Sort'))
print("Copied 'Sort' dir...")

shutil.copytree(DS_DIR, os.path.join(PKG_DIR, 'DataStructures'))
print("Copied 'DataStructures' dir...")

shutil.copytree(QUIZ_DIR, os.path.join(PKG_DIR, 'Quiz'))
print("Copied 'Quiz' dir...")

shutil.copy2('setup.py', os.path.dirname(PKG_DIR))
print("Copied setup file")

os.chdir(PKG_DIR)

os.remove(os.path.join(PKG_DIR, 'setup.py'))
os.remove(os.path.join(PKG_DIR, 'create_package.py'))

# pyc_list = AddonHelper.walk_dir(PKG_DIR, ext=['pyc'], recursive=True)
# for i in pyc_list:
# print("\t removing " + str(i))
# os.remove(i)

print("Create package...")
os.system("python setup.py sdist")

print("Install package...")
os.system("python setup.py install")






