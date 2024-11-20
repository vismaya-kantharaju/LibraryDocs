
# Hosting Python Docstrings Using MkDocs

- To generate and host Python docstring documentation using MkDocs, you can use mkdocstrings, a plugin that automatically generates documentation from docstrings.

## Step-by-step Guide to Host Python Docstrings Using MkDocs
### Prerequisites:
- Ensure Python is installed.
  
-  Install mkdocs using:
  
``` bash
pip install mkdocs
```

- Install mkdocstrings for generating docstrings-based documentation:
  
``` bash

pip install mkdocstrings
```

### 1. Create Project Structure
Create a new directory for your project documentation. Within this directory, you should have the following structure:


```bash 
LibraryDocs/
    ├── docs/
    │   ├── index.md
    │   └── library_module.md
    ├── library.py
    └── mkdocs.yml
```

- docs/ directory contains markdown files for your documentation.
- mkdocs.yml is the configuration file for MkDocs.

### 2. Create MkDocs Configuration File (mkdocs.yml)
Create a file called mkdocs.yml with the following content:

``` bash

site_name: Library Management System Docs
nav:
  - Home: index.md
  - Library Module:
      - Overview: library_module.md
plugins:
  - search
  - mkdocstrings:
      handlers:
        python:
          options:
            show_source: false
theme:
  name: material  # Optionally use the Material theme (install with `pip install mkdocs-material`)

```

### 3. Create Markdown Files

index.md (Homepage of your documentation)

**Create a file index.md inside the docs/ directory with the following content:**

``` bash

# Library Management System

Welcome to the Library Management System documentation!

This project is a simulation of a basic library management system, allowing you to add, lend, and view books using Python classes and functions.
library_module.md (Module documentation with docstrings)

```
**Create a file library_module.md inside the docs/ directory. Use the following content:**

```bash

# Library Module

::: library

```

- This line **::: library** automatically generates documentation for all classes, functions, and docstrings within the library module when you build the site using MkDocs with mkdocstrings.

### 4. Create and Organize Python Code

**Inside the root directory** (LibraryDocs), create a file library.py and **copy your Python code** into it.

### 5. Generate Documentation Using MkDocs

Run the following command to serve your documentation locally and check the generated site:

```bash 
mkdocs serve

```
- This command starts a local server. Open http://127.0.0.1:8000/ in your browser to view the documentation.

### 6. Building and Hosting the Site

To generate static files for hosting:

```bash

mkdocs build

```
- This creates a site/ directory containing static files you can deploy using platforms like GitHub Pages, Netlify, etc.

- Optional: Using mkdocstrings in Python Modules

Notes:
Ensure your Python module is in the right location for mkdocstrings to parse.
Ensure your module (library.py) follows proper docstring conventions, as shown earlier since mkdocstrings extracts documentation directly from them.
The mkdocstrings plugin dynamically pulls and formats your docstrings, offering a seamless way to document your code.
This setup helps generate and host your documentation easily using MkDocs, with auto-generated content from Python docstrings using mkdocstrings.


# Deploying MkDocs Using GitHub Actions

You can automate the deployment of your MkDocs documentation to GitHub Pages using GitHub Actions. Here's how to do it:

# Step-by-Step Guide:

- Ensure your repository has a valid mkdocs.yml configuration file and the docs directory.
- Create a .github/workflows/mkdocs-deploy.yml file in your repository with the following content:
- Commit and push these changes. Whenever you push changes to the specified branch (in this case, main), this action will automatically build and deploy the MkDocs site to GitHub Pages.
- the mkdocs-deploy.yml looks like this : 

```bash

name: Deploy MkDocs to GitHub Pages

on:
  push:
    branches:
      - main  # Replace 'main' with the branch you want to trigger deployment from
  pull_request:
    branches:
      - main

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout the repository
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: 3.x  # Replace with your Python version, e.g., '3.10'

      - name: Install dependencies
        run: |
          pip install mkdocs mkdocs-material mkdocstrings[python]

      - name: Build and deploy
        run: |
          mkdocs gh-deploy --force

```

**name: Deploy MkDocs to GitHub Pages**

- Specifies the name of the workflow. It will be displayed in the GitHub Actions dashboard.
- Trigger Conditions:

```  
  on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main
```
- on.push.branches: Triggers the workflow whenever a commit is pushed to the main branch.
- on.pull_request.branches: Triggers the workflow whenever a pull request is opened, synchronized, or reopened against the main branch.
  
```
jobs:
  deploy:
    runs-on: ubuntu-latest
```
- jobs.deploy: Defines a job named deploy. Jobs are independent units of work in the workflow.
- runs-on: ubuntu-latest: Specifies the environment for the job. Here, it uses the latest version of Ubuntu.
  
**Step 1: Checkout the Repository**
 ```
 name: Checkout the repository
  uses: actions/checkout@v3
```
  
- This step checks out the repository code so that subsequent steps can access its contents. It uses the actions/checkout action.

**Step 2: Set up Python**

```
  name: Set up Python
  uses: actions/setup-python@v4
  with:
    python-version: 3.x
```
    
- Sets up Python in the workflow environment.
- python-version: Specifies the Python version to use (e.g., 3.10).

**Step 3: Install Dependencies**

```
  name: Install dependencies
  run: |
    pip install mkdocs mkdocs-material mkdocstrings[python]
  ```
    
- Installs MkDocs and its plugins required for building and deploying the documentation:
- mkdocs: The core MkDocs tool for generating static documentation.
- mkdocs-material: A Material Design theme for MkDocs.
- mkdocstrings[python]: A plugin to generate documentation directly from Python docstrings.

**Step 4: Build and Deploy**

```
name: Build and deploy
  run: |
    mkdocs gh-deploy --force
  ```
    
- Builds the MkDocs documentation and deploys it to GitHub Pages using the mkdocs gh-deploy command.
- --force: Ensures that the deployment overwrites any existing content in the GitHub Pages branch (gh-pages).







