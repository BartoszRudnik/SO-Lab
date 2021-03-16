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

        mv ${DIRECTORY}/ ${TARGET_DIR}/;

    fi

done

for FILE in ${TARGET_DIR}/*; do

    chmod a-w ${FILE};

done

DATA=$(date +%F);

zip -r bakap_${DATA}.zip ${TARGET_DIR}; 