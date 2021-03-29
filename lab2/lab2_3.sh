#!/bin/bash -eu

if [[ $# -eq 0 ]]; then    

    echo "Nie podano argumentow wejsciowych"
    exit 1

fi

if [[ ! -d ${1} ]]; then

    exit 2

fi

FIRST_ARG=${1}

for FILE in ${FIRST_ARG}/*;  do

    onlyFile="${FILE##*/}"
    extension="${onlyFile##*.}"

    if [[ -f ${FILE} &&  ${onlyFile} == *.* && ${extension} == "bak" ]]; then
        
        chmod u-w ${FILE}
        chmod o-w ${FILE}

    fi

    if [[ -d ${FILE} && ${onlyFile} == *.* && ${extension} == "bak" ]]; then

        chmod u-x ${FILE}
        chmod g-x ${FILE}
        chmod o+x ${FILE}
        
    fi

    if [[ -d ${FILE} && ${onlyFile} == *.* && ${extension} == "tmp" ]]; then

        chmod a+w ${FILE}         

    fi

    if [[ -f ${FILE} &&  ${onlyFile} == *.* && ${extension} == "txt" ]]; then
        
        chmod a-rwx ${FILE}

        chmod u+r ${FILE}
        chmod g+w ${FILE}
        chmod o+x ${FILE}

    fi

    if [[ -f ${FILE} &&  ${onlyFile} == *.* && ${extension} == "exe" ]]; then        
       
        chmod a+xs ${FILE}              
        
    fi

done