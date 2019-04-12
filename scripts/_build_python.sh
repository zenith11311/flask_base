#!/bin/bash

exit_on_error() {

    local ERRNO=$1
    local COMMAND=$2

    if [ ${ERRNO} -eq 0 ]; then
        return 0
    fi

    echo "[ ERROR ] error ${ERRNO} occurred while processing ${COMMAND}."
    rm -rf ${DEV_TOOLS}/${PYTHON_VER}*
    exit 1
}

execute_command() {
    local WORK_PATH=$1
    local COMMAND=$2
    cd ${WORK_PATH} && eval ${COMMAND}
    exit_on_error $? "while executing ${COMMAND}"
}

build_python() {
    local DOWNLOAD_PATH=${DEV_TOOLS}/${PYTHON_VER}
    local INSTALL_PATH=${DEV_TOOLS}/${PYTHON_SMALL_VER}
    cd ${DOWNLOAD_PATH} && ./configure --prefix=${INSTALL_PATH} --enable-shared
    exit_on_error $? "${DOWNLOAD_PATH} configuration"
    cd ${DOWNLOAD_PATH} && make install
    exit_on_error $? "${DOWNLOAD_PATH} make install"

    ln -s ${INSTALL_PATH}/bin/python3 ${INSTALL_PATH}/bin/python
}

####################
# _build_python.sh #
####################

DEV_TOOLS=${DEV_HOME}/tools

if [ -z "${DEV_TOOLS}" ];then
    echo "Must run following command beforehand" 
    echo "$ source init.env"
fi

echo "Building PYTHON 3.7"
PYTHON_VER="Python-3.7.2"
PYTHON_VER_NO="3.7.2"
PYTHON_SMALL_VER="python3.7"

if [ ! -d ${DEV_TOOLS}/bin ]; then
    mkdir ${DEV_TOOLS}/bin
fi

if [ ! -d ${DEV_TOOLS}/lib ]; then
    mkdir ${DEV_TOOLS}/lib
fi

if [ ! -d ${DEV_TOOLS}/${PYTHON_SMALL_VER} ]; then
    execute_command ${DEV_TOOLS} "wget https://www.python.org/ftp/python/${PYTHON_VER_NO}/${PYTHON_VER}.tar.xz"
    execute_command ${DEV_TOOLS} "tar xJvf ${PYTHON_VER}.tar.xz"

    build_python 
fi

execute_command ${DEV_TOOLS} "rm -rf ${PYTHON_VER}*"

if [ -L ${DEV_TOOLS} ]; then
    rm ${DEV_TOOLS}/bin/python
fi

execute_command ${DEV_TOOLS} "ln -s ${DEV_TOOLS}/${PYTHON_SMALL_VER} ${DEV_TOOLS}/bin/python"

execute_command ${DEV_TOOLS}/bin/python/bin "ln -s ${DEV_TOOLS}/bin/python/bin/python3 ${DEV_TOOLS}/bin/python/bin/python"

echo "Done building python..."
