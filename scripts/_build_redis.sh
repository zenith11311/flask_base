#!/bin/bash

exit_on_error() {

    local ERRNO=$1
    local COMMAND=$2

    if [ ${ERRNO} -eq 0 ]; then
        return 0
    fi

    echo "[ ERROR ] error ${ERRNO} occurred while processing ${COMMAND}."
    rm -rf ${DEV_TOOLS}/redis*
    exit 1
}

execute_command() {
    local WORK_PATH=$1
    local COMMAND=$2
    cd ${WORK_PATH} && eval ${COMMAND}
    exit_on_error $? "while executing ${COMMAND}"
}

####################
# _build_redis.sh #
####################

DEV_TOOLS=${DEV_HOME}/tools

if [ -z "${DEV_HOME}" ];then
    echo "Must run following command beforehand" 
    echo "$ source init.env"
fi

if [ ! -d ${DEV_TOOLS}/bin ]; then
    mkdir ${DEV_TOOLS}/bin
fi

if [ ! -d ${DEV_TOOLS}/lib ]; then
    mkdir ${DEV_TOOLS}/lib
fi

if [ ! -d ${DEV_TOOLS}/redis-server ]; then
    execute_command ${DEV_TOOLS} "wget http://download.redis.io/redis-stable.tar.gz"
    execute_command ${DEV_TOOLS} "tar xzf redis-stable.tar.gz"
    execute_command ${DEV_TOOLS}/redis-stable "make"
    execute_command ${DEV_TOOLS}/redis-stable "make install PREFIX=${DEV_TOOLS}/redis-server"
    execute_command ${DEV_TOOLS} "rm -rf ${DEV_TOOLS}/redis-stable*"
    execute_command ${DEV_TOOLS} "ln -s ${DEV_TOOLS}/redis-server/bin ${DEV_TOOLS}/bin/redis"
fi

echo "Done building redis..."

