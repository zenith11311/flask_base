#!/bin/bash

exit_on_error() {

    local ERRNO=$1
    local COMMAND=$2

    if [ ${ERRNO} -eq 0 ]; then
        return 0
    fi

    echo "[ ERROR ] error ${ERRNO} occurred while processing ${COMMAND}."
    rm -rf ${DEV_TOOLS}/virtualenv*
    exit 1
}

execute_command() {
    local WORK_PATH=$1
    local COMMAND=$2
    echo "work_path : ${WORK_PATH}"
    echo "command   : ${COMMAND}"
    cd ${WORK_PATH} && eval ${COMMAND}
    exit_on_error $? "while executing ${COMMAND}"
}

####################
# _build_venv.sh #
####################

VENV_VER=16.4.1
DEV_TOOLS=${DEV_HOME}/tools

if [ -z "${DEV_TOOLS}" ];then
    echo "Must run following command beforehand" 
    echo "$ source init.env"
    exit 1
fi

echo "Building virtualenv" 

if [ ! -d ${DEV_TOOLS}/bin ]; then
    mkdir ${DEV_TOOLS}/bin
fi

if [ ! -d ${DEV_TOOLS}/lib ]; then
    mkdir ${DEV_TOOLS}/lib
fi

if [ ! -d ${DEV_TOOLS}/virtualenv-${VENV_VER} ]; then
    echo "Download virtualenv"
    echo "dev_tools_dir : ${DEV_TOOLS}"
    execute_command ${DEV_TOOLS} "wget -O virtualenv-${VENV_VER}.tar.gz https://files.pythonhosted.org/packages/ca/fd/3c50bd5938f47414fca6cba87ae5b2c4f300bbcb6100ccf96c78057f7314/virtualenv-${VENV_VER}.tar.gz"
    echo "Unzip virtualenv tarball"
    execute_command ${DEV_TOOLS} "tar xvf virtualenv-${VENV_VER}.tar.gz" 
    echo "Clean up the install trace of virtualenv"
    execute_command ${DEV_TOOLS} "rm virtualenv-${VENV_VER}.tar.gz" 
fi

echo "#!/bin/bash " > ${DEV_TOOLS}/bin/virtualenv
echo "python3 ${DEV_TOOLS}/virtualenv-${VENV_VER}/virtualenv.py --system-site-packages \$1" >> ${DEV_TOOLS}/bin/virtualenv
chmod 777 ${DEV_TOOLS}/bin/virtualenv

echo "Done building virtualenv..."

