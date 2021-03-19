#!/bin/bash

SOURCE_DIR=${1:-"lab_uno"};
RM_LIST=${2:-"lab_uno/2remove"};
TARGET_DIR=${3:-"bakap"};

if [[ ! -d ${TARGET_DIR} ]]; then

    mkdir ${TARGET_DIR};

fi

for VALUE in $(cat "${RM_LIST}"); do

    if [[ -e ${SOURCE_DIR}/${VALUE} ]]; then

        if [[ ! -d ${SOURCE_DIR}/${VALUE} ]]; then

            rm ${SOURCE_DIR}/${VALUE};

        fi

        if [[ -d ${SOURCE_DIR}/${VALUE} ]]; then

            rm -r ${SOURCE_DIR}/${VALUE};

        fi
    
    fi

done

for FILE in ${SOURCE_DIR}/*; do

    if [[ ! -d ${FILE} ]]; then

        mv ${FILE} ${TARGET_DIR}/;

    fi

done

for DIRECTORY in ${SOURCE_DIR}/*; do

    if [[ -d ${DIRECTORY} ]]; then

        cp -r ${DIRECTORY}/ ${TARGET_DIR}/;

    fi

done

if [[ $(find ${SOURCE_DIR} -type f | wc -l ) -eq 0 ]]; then
    echo "tu byl Kononowicz"
fi

if [[ $(find ${SOURCE_DIR} -type f | wc -l ) -gt 0 ]]; then

    echo "jeszcze cos zostalo"

    if [[ $(find ${SOURCE_DIR} -type f | wc -l ) -ge 2 ]]; then

        echo "zostaly co najmniej 2 pliki"

        if [[ $(find ${SOURCE_DIR} -type f | wc -l) -gt 4 ]]; then
            
            echo "zostalo wiecej niz 4 pliki"
        
        fi

        if [[ $(find ${SOURCE_DIR} -type f | wc -l) -le 4 ]]; then
            
            echo "zostalo nie wiecej niz 4 ale co najmniej 2 pliki"
        
        fi 

    fi

fi

for FILE in ${TARGET_DIR}/*; do

    chmod a-w ${FILE};

done

DATA=$(date +%F);

zip -r bakap_${DATA}.zip ${TARGET_DIR}; 