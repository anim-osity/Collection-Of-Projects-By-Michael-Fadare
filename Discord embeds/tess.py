import requests
import github
from github import Github
from github import InputGitTreeElement
from git import Repo

token = 'github token'
g = Github(token)
repo = g.get_user().get_repo('Test')
contents = repo.get_contents("Links.txt")

RawData = requests.get('gets the contents of the discord repo document')
Raw = RawData.text

if 

#if the link is not in the File already add it to the file 
UpdatedRaw = Raw + " " + LinkToEdit


repo.update_file(contents.path, "H", UpdatedRaw, contents.sha, branch="master")
