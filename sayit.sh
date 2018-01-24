echo $1 > ~/bin/say.txt
text2wave -eval '(voice_msu_ru_nsh_clunits)' say.txt -o ~/bin/say.wav
lame say.wav say.mp3
mpg321 say.mp3
