#!/bin/zsh
# This grabs the text output semirad.py, and then uses youtube-dl
# to download all the videos to the path where you ran the script.

MYDIR="$(dirname "$(realpath "$0")")"
TEXTFILE="${MYDIR}/Output.txt"
echo $TEXTFILE
input="/home/bryce/PycharmProjects/ENSF592/Output.txt"
while IFS= read -r line
do
	 youtube-dl "$line"
  done < "$TEXTFILE"
# youtube-dl https://semi-rad.com/2018/11/friday-inspiration-vol-156/
