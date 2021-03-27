#!/bin/bash

if [[ ! -d ${1} || ! -f ${2} ]]; then

    exit 1

fi

if [[ $# -eq 0 ]]; then    

    echo "Nie podano argumentow wejsciowych"
    exit 2

fi

FIRST_ARG=${1}
SECOND_ARG=${2}

for FILE in ${FIRST_ARG}/*; do

    if [[ ! -e ${FILE} ]]; then
        
        printf "${FILE} $(date --iso-8601) \n" >> ${SECOND_ARG}
        rm ${FILE}

    fi

done
