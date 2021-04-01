# Project's documentation

The porcello provide simple skeleton for a pythons discord bot.

Refer to the [discrod.py library documentation](https://discordpy.readthedocs.io/en/latest/api.html) for the API used.

## documents

- porcello Usage (this project): 
[porcello.pdf](https://dtcsrv848.dl.net/tools/python_libs/porcello/-/raw/master/docs/porcello.pdf?inline=false) [USER GUIDE]

- database schema: 
[database_schema_v12.pdf](https://dtcsrv848.dl.net/tools/python_libs/porcello/-/raw/master/docs/database_schema_v12.pdf?inline=false)

- project's source code available from:
[porcello git repository](https://dtcsrv848.dl.net/tools/python_libs/porcello)

---

## project files

Files from this repository:
- porcello/porcello.py: Project's file
- requirements.txt: needed packages to build the application 
- script_pycharm: Script files to automate build/clean processes (PyCharm version)
- script_linux: Script files to automate build/clean processes (linux version)
- docs/: HTML/PDF documentation directory
- tests/: Unit test scripts
- LICENSE: license file
- README.md: this file

---

## scripts

Inside `script_pycharm` directory there is a script's
collection to automate common processes


### install requirements

Install requirements from Terminal of PyCharm with:

> script_pycharm\install_requirements.bat


### build documentation

Build html/pdf documentations from Terminal of PyCharm with: 

> script_pycharm\make_docs.bat


### execute unit tests

Execute unit test from Terminal of PyCharm with: 

> script_pycharm\make_tests.bat


### clean directories

Clean directories from Terminal of PyCharm with:

> script_pycharm\make_clean.bat

---

## IMPORTANT DEVELOPER NOTE

In other to release a new version for an upgrade or a bug-fix please follow below steps do not miss something:

1. Get last version of *develop* branch from git repository
2. Update _revision_ number saved on following files:
    * > docs/source/conf.py
    * > porcello/porcello.py
3. Create new entry on `CHANGELOG.md` file for new release with change info
4. Make you changes on source code to integrate the new library
5. Add/update test files on `tests` directory
7. Repeat "*porcello*" program since you not have fix all issues
12. Update this project documentation (check all links)
13. Build documentation with "*make docs*" script
14. Check new version of `porcello.pdf` document
15. Clean directories with "*make clean*" script
16. Commit changes to *develop* and push to origin
17. Merge (fast-forward) the *develop* branch into *master* branch
18. Tag the *master* branch with the released version number
19. Check GIT repository from browser interface
20. Notify new version to users
