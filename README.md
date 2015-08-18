# TerminalBibleVerse
Grabs a Bible verse through http://www.esvapi.org/.

Changing the path to the repo and adding the following lines to a .zshrc file will load a Bible verse on termial load. 

```
 function _display_bible_verse() {
   verse=$(python ~/Projects/TerminalBibleVerse/get_bible_verse.py)
   echo "$verse"
 }
 echo "$(_display_bible_verse)"
```
