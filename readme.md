# Python CLI template

This is an opinionated template for making a Python command line program.

## Usage

```bash
git clone git@gitlab.cbp.dhs.gov:niid/dac-ter-ardis/python-cli-template.git yourprojectname
cd yourprojectname
rmdir /s .git
del readme.md
ren template_readme.md readme.md
del template_readme.md
ren main.py yourproject.py
copy .env.template .env
git init
```

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
