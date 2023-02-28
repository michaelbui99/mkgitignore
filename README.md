# mkgitignore

Small utiliy tool for creating a .gitignore file based on Github's gitignore templates

# Example

![](/doc/mkgitignore_demo.gif)

# Usage

The .gitignore file will be created at the current working directory.<br>
Template name must match the exact name in the github/gitignore repository without the .gitingore extension

```bash
$ python mkgitignore/main.py Unity
```

# Setup

Download the setup.ps1 (windows) or setup.sh (linux)

Run the script

```bash
$ ./setup.ps1
```

or

```bash
$ chmod +x ./setup.sh && ./setup.sh
```
