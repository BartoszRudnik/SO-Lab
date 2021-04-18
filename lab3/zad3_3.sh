#!/bin/bash -eu

#We wszystkich plikach w katalogu ‘groovies’ zamień $HEADER$ na /temat/
for FILE in groovies/*; do

    sed -i.bak 's/\$HEADER\$/\/temat\//g' ${FILE}

done

#We wszystkich plikach w katalogu ‘groovies’ po każdej linijce z 'class' dodać '  String marker = '/!@$%/''
for FILE in groovies/*; do

    sed -i '/class/a String marker = "\/!@\$%\/"' ${FILE}

done

#We wszystkich plikach w katalogu ‘groovies’ usuń linijki zawierające frazę 'Help docs:'
for FILE in groovies/*; do

    sed -i "/Help docs:/d" ${FILE}

done