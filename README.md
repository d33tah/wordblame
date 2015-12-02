# wordblame

Performs a word-by-word "blame" command, as known from version control
systems.

Usually "blame" is implemented on a per-line basis - this program is an
attempt at creating a tool that would enable the user to find out which change
introduced a particular word.

For usage information, run this program with --help command-line argument.

Sample usage - you can replace "Nmap" with other article name:

```
./wordblame --get-cmd "./wikipedia-show-change" \
    --list-cmd "./wikipedia-list-changes 'https://en.wikipedia.org/w/index.php?title=Nmap&action=history'" \
    --url-cmd="sed 's@&action=edit@\&diff=prev@g'" --verbose > report.html
```

Author: Jacek Wielemborek, licensed under WTFPL.

Example report: https://d33tah.github.io/wordblame/nmap.html
