# album-artter

**Album-artter** is a program that puts album art on wav files or (track number, album name, album singer).

![2024 05 08 drawio](https://github.com/rlaxodud6842/album-artter/assets/79405594/03170383-d233-48ae-9c34-ccdf111a77a2)

All you need is:

* You have to put the album folder that you want to change into the songs folder
* Prepare the image with cover.jpg
* Album tag for Album, for example. Keep sequence:
    *1. Album Name
    *2. Album Artist
    *3. Total Track

## How to install

First time only:
+ Install `Python 3` (a version newer or equal to `3.7` is required)
    * Linux: `apt install python3` (or equivalent)
    * Windows: [Official webiste](https://www.python.org/)
    * MacOS: You should have it already installed or `brew install python3`
+ Open your terminal app
+ Create a virtual environment
    * `python3 -m venv venv`
+ Activate the virtual environment
  * Linux/MacOS: `source venv/bin/activate`
  * Windows: `./venv/Scripts/activate`
+ Install requirements
    * `pip list --format=freeze > requirements.txt`
+ You are ready to go!

After the first time:

+ Open your terminal app
+ Activate the virtual environment
  * Linux/MacOS: `source venv/bin/activate`
  * Windows: `./venv/Scripts/activate`
+ You are ready to go!

## Quick guide (from a local album)

+ Create a copy of the `tracks.txt.example`, rename it as `tag.txt`
+ Open `tracks.txt`
+ Add your tracks timestamps info in this format:
   * 1. Album Name
     2. Album Artist
     3. Total Track
+ Run the script
    * Basic usage: `python main.py <path/to/your/music/folder> -a <path/to/your/cover.jpg> -t <path/to/your/tag.txt>`
 


reference https://github.com/crisbal/album-splitter
