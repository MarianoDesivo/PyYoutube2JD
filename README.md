# PyYoutube2JD
Python program that gets all the links in a youtube channel, and downloads them as audio. It uses [MyJDownloader API](https://github.com/mmarquezs/My.Jdownloader-API-Python-Library) for python

Currently you have to download the .py file and edit some variables with your data (myjd user, password, downloads directory,etc), see code comments for more details.

It will download all of the videos (you don't already have in the Downloads tab) in audio format. You can convert them to mp3 (or other formats) with JD build-in scripts (see link: https://board.jdownloader.org/showthread.php?t=70525)

Made on windows 10 with Python 3.8.1

# PyYoutube2JD



PyYoutube2JD allows [JDownloader](https://jdownloader.org/) users to get all video download links from a Youtube account (or playlist).

It gets every video link and moves them to your Downloads queue as audio files.

## Prerequisites

Before you begin, ensure you have met the following requirements:

* You have installed the latest version of[JDownloader](https://jdownloader.org/).
* [MyJDownloader API](https://github.com/mmarquezs/My.Jdownloader-API-Python-Library) for python.
```
  pip install myjdapi
```
* [PyAutoGUI](https://pypi.org/project/PyAutoGUI/)
 ```
  pip install pyautogui
 ```
* Python 3 or higher.

## Installing PyYoutube2JD

To install PyYoutube2JD, follow these steps:

* Open Jdownloader.
* Go to MyJDownloader > Setup & Login
* Make sure you have got an account (if not create a new one following the instructions at MyJDownloader.org)
* Complete the text boxes with your email, password, and device name (you will need this data later).
* Download PyYoutube2JD.py and open with your edit IDLE to configure and execute it.

## Using PyYoutube2JD.py

To use PyYoutube2JD.py, follow these steps:

* Complete with your data, used on previous steps:
```python
#connect to JDownloader

jd=myjdapi.Myjdapi()
jd.set_app_key("EXAMPLE")


pw='' #Password
mail= '' #User
device = '' #Write your device name, for example: 'JDownloader@MARIANO'

```
* On *folder*, rewrite the directory you want to use
```python
##This function will get all the video links from a youtube account
def Obtenerlinks(url,youtuber):
       
   
    folder = r'C:\Users\MARIANO\\Downloads\Jdownloader\\'+ youtuber + '\\' + fecha #Name the folder you want to store files, I used Date as I said previously
    
    lincs.add_links([{
                          "autostart": False,
                          "links": url, #Youtube account link (see examples below)
                          "packageName": youtuber, #Name you want to call it, it will be used for the folder name
                          "extractPassword": None,
                          "priority": "DEFAULT",
                          "downloadPassword": None,
                          "destinationFolder": folder, 
                          "overwritePackagizerRules": True
                      }])

```


Add run commands and examples you think users will find useful. Provide an options reference for bonus points!

## Contributing to <project_name>
<!--- If your README is long or you have some specific process or steps you want contributors to follow, consider creating a separate CONTRIBUTING.md file--->
To contribute to <project_name>, follow these steps:

1. Fork this repository.
2. Create a branch: `git checkout -b <branch_name>`.
3. Make your changes and commit them: `git commit -m '<commit_message>'`
4. Push to the original branch: `git push origin <project_name>/<location>`
5. Create the pull request.

Alternatively see the GitHub documentation on [creating a pull request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).

## Contributors

Thanks to the following people who have contributed to this project:

* [@scottydocs](https://github.com/scottydocs) 📖
* [@cainwatson](https://github.com/cainwatson) 🐛
* [@calchuchesta](https://github.com/calchuchesta) 🐛

You might want to consider using something like the [All Contributors](https://github.com/all-contributors/all-contributors) specification and its [emoji key](https://allcontributors.org/docs/en/emoji-key).

## Contact

If you want to contact me you can reach me at <your_email@address.com>.

## License
<!--- If you're not sure which open license to use see https://choosealicense.com/--->

This project uses the following license: [<license_name>](<link>).
