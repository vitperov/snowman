HOST=robo@192.168.1.116

#echo $1 > say.txt
#scp say.txt $HOST:~
#ssh -t $HOST "echo $1 > ~/say.txt"
ssh -t $HOST "echo $1 > ~/say.txt && text2wave -eval '(voice_msu_ru_nsh_clunits)' say.txt -o ~/say.wav"
scp $HOST:~/say.wav .
lame say.wav say.mp3
mpg321 say.mp3


