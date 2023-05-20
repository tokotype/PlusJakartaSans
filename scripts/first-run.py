#!/usr/bin/env python3

# This script is run the first time any action is performed after the repository
# is cloned. If you are reading this because the automatic initialization failed,
# skip down to the section headed "INITIALIZATION STEPS".

from sh import git
import datetime
import re
import sys
from urllib.parse import quote
import subprocess

BASE_OWNER = "googlefonts"
BASE_REPONAME = "googlefonts-project-template"
DUMMY_URL = "https://yourname.github.io/your-font-repository-name"


def repo_url(owner, name):
    return f"https://github.com/{owner}/{name}"


def web_url(owner, name):
    return f"https://{owner}.github.io/{name}"


def raw_url(owner, name):
    return f"https://raw.githubusercontent.com/{owner}/{name}"


def touch():
    open(".init.stamp", "w").close()


def lose(msg, e=None):
    print(msg)
    print("You will need to do the initialization steps manually.")
    print("Read scripts/first-run.py for more instructions how to do this.")
    if e:
        print(
            "\nHere's an additional error message which may help diagnose the problem."
        )
        raise e
    sys.exit(1)


try:
    my_repo_url = git.remote("get-url", "origin")
except Exception as e:
    lose("Could not use git to find my own repository URL", e)

m = re.match(r"(?:https://github.com/|git@github.com:)(.*)/(.*)/?", str(my_repo_url))
if not m:
    lose(
        f"My git repository URL ({my_repo_url}) didn't look what I expected - are you hosting this on github?"
    )

owner, reponame = m[1], m[2]

if owner == BASE_OWNER and reponame == BASE_REPONAME:
    print("I am being run on the upstream repository (probably due to CI)")
    print("All I'm going to do is create the touch file and quit.")
    touch()
    sys.exit()

# INITIALIZATION STEPS

# First, the README file contains URLs to pages in the `gh-pages` branch of the
# repo. When initially cloned, these URLs will point to the
# googlefonts/Unified-Font-Repository itself. But downstream users want links
# and badges about their own font, not ours! So any URLs need to be adjusted to
# refer to the end user's repository.

# We will also pin the dependencies so future builds are reproducible.

readme = open("README.md").read()

print(
    "Fixing URLs:", web_url(BASE_OWNER, BASE_REPONAME), "->", web_url(owner, reponame)
)

readme = readme.replace(web_url(BASE_OWNER, BASE_REPONAME), web_url(owner, reponame))
# In the badges, the URLs to raw.githubusercontent.com are URL-encoded as they
# are passed to shields.io.
print(
    "Fixing URLs:",
    quote(raw_url(BASE_OWNER, BASE_REPONAME), safe=""),
    "->",
    quote(raw_url(owner, reponame), safe=""),
)
readme = readme.replace(
    quote(raw_url(BASE_OWNER, BASE_REPONAME), safe=""),
    quote(raw_url(owner, reponame), safe=""),
)

print(
    "Fixing URLs:",
    DUMMY_URL,
    "->",
    web_url(owner, reponame),
)
readme = readme.replace(
    f"`{DUMMY_URL}`",
    web_url(owner, reponame),
)

with open("README.md", "w") as fh:
    fh.write(readme)

# Fix the OFL

ofl = open("OFL.txt").read()
ofl = ofl.replace(web_url(BASE_OWNER, BASE_REPONAME), web_url(owner, reponame))
ofl = ofl.replace("My Font", reponame.title())
ofl = ofl.replace("20**", str(datetime.date.today().year))
with open("OFL.txt", "w") as fh:
    fh.write(ofl)

# Pin the dependencies
print("Pinning dependencies")
dependencies = subprocess.check_output(["pip", "freeze"])
with open("requirements.txt", "wb") as dependency_file:
    dependency_file.write(dependencies)

# Finally, we add a "touch file" called ".init.stamp" to the repository which
# prevents this first-run process from being run again.
touch()
