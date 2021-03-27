#!/bin/bash

if [[ ! -d ${1} || ! -d ${2} ]]; then

    exit 1

fi

if [[ $# -eq 0 ]]; then    

    echo "Nie podano argumentow wejsciowych"
    exit 2

fi

FIRST_DIR=${1}
SECOND_DIR=${2}

for FILE in ${FIRST_DIR}/*; do    

    echo -ne ${FILE}

    if [[ -d ${FILE} ]]; then

        echo " -> Katalog"

        ln -s ../${FILE} ./${SECOND_DIR}/${FILE##*/}"_ln"

    fi

    if [[ -f ${FILE} && ! -L ${FILE} ]]; then

        echo " -> Plik regularny"

        onlyFile="${FILE##*/}"

        extension="${onlyFile##*.}"                     
        filename="${onlyFile%.*}"       

        if [[ $onlyFile == *.* ]]; then

            ln -s ../${FILE} ./${SECOND_DIR}/${filename}"_ln."${extension}

        else

            ln -s ../${FILE} ./${SECOND_DIR}/${filename}"_ln"

        fi

    fi

    if [[ -L ${FILE} ]]; then

        echo " -> Dowiazanie symboliczne"

    fi    

done