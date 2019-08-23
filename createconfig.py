import configparser

config = configparser.ConfigParser()
config['DEFAULT'] = {
    'Start': 'Hello, I am MakeYourFolderBetter app!\n\n', 
    'Count_check': 1, 
    'width': 500, 
    'plus_height': 0,
    'ignore': ['__pycache__', '.vscode', 'venv', 'app.py', 'files.json', 'ReadMe.md', 'settings.py', 'test.py']
    }
config['About'] = {'version': 'v0.1.3', 'lic': 'Intersog'}

with open('config.ini', 'w') as configfile:
  config.write(configfile)