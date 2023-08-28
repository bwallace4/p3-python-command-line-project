# Directme


As a big fan of movies and Hollywood in general, I thought how could i design my project to include this. Sometimes I forget who directed some of my favorite films. 
DIRECTME is a command line interface that allows the user to query data from my database in Sqlalchemy, a film library database. Giving the user options on updating and reading information about the film industry. Whether its the director, the reviews or the movie itself. The three tables creates a one-to-many relationship and are joined together by foreign keys. 

## Table of Contents

- [Overview](#overview)
- [Getting Started](#getting-started)
  - [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Overview
My project lets you insert your own information or lookup information you didn't know about a certain film. Commands are made simple by simply typing them in the terminal. The purpose of my project is to educate. 


## Getting Started
You always want to fork and clone your repo. install libraries sqlalchemy and alembic, clicker 
also a database sqlite 
python3 and pip 


### Installation

1. Clone the repository: `git clone https://github.com/bwallace4/p3-python-command-line-project.git`
2. Navigate to the project directory: `cd p3-python-command-line-project`
3. Install dependencies: `pipenv install`
4. Run the project: `python cli.py` 

## Usage
HOW we communicate with the terminal run 
 ./cli.py........
My lib.py - is where I keep most of my data.......
seed.py - is where i seed my data using the faker library.......
debug.py-  is where I test bugs in my application......
models.py - is where I keep my data tables......

FIRST STEP is creating the database by running models.py
SECOND STEP is running seed.py to add some random data to the database
THIRD STEP is opening the database using sqlite explorer
LAST STEP is running cli.py and using the terminal to run commands
python cli.py create_user

Troubleshooting my app may require you to delete the library.db then remake it by running the models,py script


## License

This project is licensed under the [MIT License](LICENSE).

