#!/usr/bin/env bash

set -e

function help_text {
  printf """
Build the project's docker images.
Usage:
  -i    The docker image to build
  -a    Build all images
  
Example:
  ./build.sh \\
    -i dataloader
"""
}

function build_image (){
    if [ -z "$3" ] ; then
        docker build -t aminehajali/se-$1 ./$2
        return 0
    fi
    docker build -f ./$2/Dockerfile.$3 -t aminehajali/se-$1 ./$2
}

function build_dataloader {
    build_image dataloader back dataloader
}

function build_datareader {
    build_image datareader back datareader
}

function build_front {
    build_image front front
}

function build_scrapper {
    build_image scrapper scrapper
}

function build_all {
    build_front
    build_datareader
    build_dataloader
    build_scrapper
}

if [ $# -eq 0 ] ; then
    echo "missing arguments, use -h for help"
    exit 1
fi

if  [ $# -ge "1" ] ; then
    if [ $1 == "-h" ] ; then
        if [ $# -ne "1" ] ; then
            echo "-h doesn't expect any additional arguments"
            exit 1
        fi
        help_text
        exit 0
    fi

    if [ $1 == "-a" ] ; then
        if [ $# -ne "1" ] ; then
            echo "-a doesn't expect any additional arguments"
            exit 1
        fi
        build_all
        exit 0
    fi

    if [ $1 == "-i" ] ; then
        if [ $# -eq "1" ] ; then
            echo "-i expects image to build"
            exit 1
        fi
        shift 1

        while (("$#")); do
            case "$1" in
            front|fr)
                build_front
                shift 1
                ;;
            dataloader|dl)
                build_dataloader
                shift 1
                ;;
            datareader|dr)
                build_datareader
                shift 1
                ;;
            scrapper|sc)
                build_scrapper
                shift 1
                ;;
            *)
                echo "unknown image"
                exit 1
            esac
        done
        exit 0
    fi
    echo "unknown arguments, use -h for help"
    exit 1
fi
