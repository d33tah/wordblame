# wordblame

Performs a word-by-word "blame" command, as known from version control
systems.

Usually "blame" is implemented on a per-line basis - this program is an
attempt at creating a tool that would enable the user to find out which change
introduced a particular word.

For usage information, run this program with --help command-line argument.

Sample usage:

```
./wordblame --list-cmd './wikipedia-list-changes Rosselia_bracteata' \
    --get-cmd './wikipedia-show-change' \
    --url-cmd="sed 's@&action=edit@\&diff=prev@g'" --verbose > report.html
```

Author: Jacek Wielemborek, licensed under WTFPL.

Example report: https://d33tah.github.io/wordblame/nmap.html
