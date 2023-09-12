# SSSniperWolf-BBBingo-autoplay
 A script to play SSSniperWolf BBBingo by jacksfilms automatically. Esentially opens a shitton of cards you want to, to increase your chances and then you can check if the input you give to it results in a bingo for any of those cards.

<h1> <span style="color:#F47174">
 Easiest
</span>: Command line usage: </h1>

First of all make sure you have pip and python 3.10+ or higher installed on your machine, if you don't have it installed, you can download it from [here](https://www.python.org/downloads/). 
Then, make sure you have git installed on your machine, if you don't have it installed, you can download it from [here](https://git-scm.com/downloads).



<h3>1. Open up  a Terminal / cmd (better PowerShell) window</h3>

Installation:
copy and paste this block into your terminal  
```bash
git clone https://github.com/viktorashi/bingobaker.com-autoplayer && cd bingobaker.com-autoplayer && pip install -r requirements.txt
```
<h3>2. Get usage directions</h3>



```bash
python  autobingo.py -h
```
```string
usage: autobingo [-h] [-u URL] [-cnt COUNT] [-i INPUT_PATH] [-o OUTPUT_PATH] [-c CARDS_PATH] [-gm {normal,blackout,peen,3in6,loser}] [-r]
                 [-strt START] [-fs FREE_SPACE]
                 [{editconfig,generate,check}]

Auto Bingo playing command line tool. Currently only being used for bingobaker.com

positional arguments:
  {editconfig,generate,check}
                        The mode to run the program in. [default: editconfig]

options:
  -h, --help            show this help message and exit
  -u URL, --url URL     The link to the bingo card generator
  -cnt COUNT, --count COUNT
                        Number of bingo cards to generate from the generator link
  -i INPUT_PATH, --input INPUT_PATH
                        The file containing the keywords to search for on the bingo cards [default: input.txt]
  -o OUTPUT_PATH, --output OUTPUT_PATH
                        File to write the bingo'ed cards to [default: output.json]
  -c CARDS_PATH, --cards CARDS_PATH
                        The path you want the cards to be saved in
  -gm {normal,blackout,peen,3in6,loser}, --gamemode {normal,blackout,peen,3in6,loser}
                        The gamemode to play in. [default: normal]
  -r, --reverse         Reverse the bingo card order when reading from [cards.txt] [default False]
  -strt START, --start START
                        The index of the card to start doing anything from
  -fs FREE_SPACE, --free-space FREE_SPACE
                        Name of the freespace to search for in the card [default: 'no credit']

ion care how u use my code lol
```
for the operation and options

## Regarding  all the options : if nothing is specified, the last used value from the bingoconfig.json file will be used, if never specified before, the default values will be used

### <font size=5> Positional arguments</font> reffer to the first thing you type after ```python autobingo.py```, meaning the function you want to execute, generating, checking the bingos, marking the spots (which includes checking the bingo's if any spots containing the keywords have been found), and clearing the cards in case jack got a bigo already :'( 
    
- generate : generates {--count} bingo cards from the specified {--url}, writes their links to {--cards [default cards.txt]} (middle free space is always checked)
- check :checks bingos for each card, will be less used since it automatically checks the bingo eitherway for each card as it searches
- editconfig : is the default behaviour if nothing specified, it does nothing but update the ***bingoconfig.json***

### <font size=5> --input <sub> [default: input.txt , shorthand -i]</sub> </font>  is the file in which you have the keywords you want to search for on the bingo cards, each keyword on a new line. They DON'T have to be specified exactly as in the cards, lowercase values will be compared and they can just contain  those strings 
#### **`inpux.txt`**
``` 
freebooting a freebooted 
fake laugh
bro
```
### <font size=5> --output <sub>[default: output.json, shorthand -o]</sub></font> : file that outputs the bingos 
#### **`output.json`**
``` 
https://bingobaker.com/#64e7dce5f63bda5a
https://bingobaker.com/#64e7dce69d2d0c80
```

### <font size=5> --cards <sub>[default: cards.txt, shorthand -c]</font> </sub>: path you want the generated cards to be saved in 
#### **`cards.txt`**
``` 
..............
https://bingobaker.com/#64e7dce5f63bda5a
https://bingobaker.com/#64e7dce69d2d0c80
https://bingobaker.com/#64e7dce8ea9ba59b
https://bingobaker.com/#64e7ef15848b63aa
https://bingobaker.com/#64e7ef16a2ac9aa0
https://bingobaker.com/#64e7f64cb4cf4a44
https://bingobaker.com/#64e7f64e07911364
https://bingobaker.com/#64e7f650b9c63320
https://bingobaker.com/#64e7f65121c3c750
https://bingobaker.com/#64e7f6535e698b25
.................
```

### <font size=5> --url <sub>[default:"" nothing, only paramter that needs specified, shorthand -u]</sub></font>: the link to the bingobaker.com generator 

### <font size=5> --count <sub>[default: 100, shorthand -cnt]</sub></font> : number of cards to be generated by the {generate} function 


### <font size=5> --gamemode <sub>[default : normal , shorthand -gm] </sub> </font>: The bingo shape for the code to check
options:
 - norrmal : full row, collumn or diagonal
 - blackout : all spots
 - peen : form of a peepee ╭ᑎ╮ middle collumn bottom row
 - 3in6 : 3x3 square inside 6x6 grid
 - loser : shape of an L on her forehead (first collumn, last row)


### <font size=5> --reverse <sub>[Bool, default: False, shorthand -r] </sub> </font>: Wether  to do all operations on cards in reverse or normal order, usage: 
```bash
python autobingo.py mark -r
```
or 
```bash
python autobingo.py mark --reverse
```


### <font size=5> --start <sub>[int, default: 0, shorthard -strt] </sub> </font>:  The index of the card to start doing anything from

### <font size=5> --free-space <sub>[string, default: "no credit", shorthand -fs] </sub> </font>: The name of the freespace spot to check for if the card has an even size (meaning there is no clear midde spot)


<h3><span style="color:#F47174"> 3. It will all be saved  </span></h3>


### Every parameter value you provide to the command will be saved in a file called ***bingoconfig.json*** right next to the program. Plus it will automatically check set the size to the card's size, if the free space is in the middle or not and update that in the config file <h3><span style="color:red"> DO NOT CHANGE THE CONFIG FILE DIRECTLY</span></h3>



<img src="image.png" alt="drawing" width="70">   <font size=40> Warning: </font> 

idk how well i've tested this but i believe it starts messing up if you do. But delete it all-togather if you have and it doesn't work anymore, it will just generate another one.

<h1>Usage example</h1>

#### Don't be scared by the extensive docs, it's actually really easy to use
First you would usually want to generate the cards, so 
##### **`zsh`**
```bash
python autobingo.py generate --url https://bingobaker.com/#64c998520e68afc5 -cnt 100
```
should do the job, then you would create an **input.txt** right next to this and run

##### **`zsh`**
```bash
python autobingo.py check
```
ez, peek into the console once in a while and see if it outputed anything about a congratilations, then go to output.json to check it.
#### This generates 75 bingo cards with the generator link you have provided to it, the bingo's of which will be saved to the ***wins.txt*** file.

##### **`zsh`**
```bash
python autobingo.py generate --url https://bingobaker.com/#64c998520e68afc5 --output wins.txt --count 75 
```
Given all this data has been saved to ***bingoconfig.json*** this 


<h2>For the coders</h2>
There's also a class you can use in your projects by doing

```python
from main import autobingo
```

at the top of your adjecent python file


<h1>Credits</h1>
@Itamar1337 - thanks for making it actually usable and and not have this script impose the same effect a TNT minecraft nuke bomb has on your pc


bye bruh
