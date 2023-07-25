# Python CLI template

This is an opinionated template for making a Python command line program.

## Usage

```bash
git clone https://github.com/reubengann/python-cli-template.git yourprojectname
cd yourprojectname
rmdir /s .git
del readme.md
ren template_readme.md readme.md
ren main.py yourproject.py
copy .env.template .env
git init
```

(then, if using vs code, modify launch.json to have the correct filename)

## Features

- Main function with argument parsing, verbs, and logging
- Environment/.env settings
- Dependency management via pip-tools
- Pytest already set up
- Environment variable template
- A decent gitignore
- Coverage settings
- A readme template
- A good VS Code config
