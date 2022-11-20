#!/usr/bin/env bash

set -e

function help_text {
  printf """
Push the project's docker images.
Usage:
  -i    The docker image to push
  -a    Push all images
  
Example:
  ./push.sh \\
    -i dataloader
"""
}

function push_image (){
    docker push aminehajali/se-$1
}

function push_all {
    push_image front
    push_image datareader
    push_image dataloader
    push_image scrapper
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
        push_all
        exit 0
    fi

    if [ $1 == "-i" ] ; then
        if [ $# -eq "1" ] ; then
            echo "-i expects image to push"
            exit 1
        fi
        shift 1

        while (("$#")); do
            case "$1" in
            front|fr)
                push_image front
                shift 1
                ;;
            dataloader|dl)
                push_image dataloader
                shift 1
                ;;
            datareader|dr)
                push_image datareader
                shift 1
                ;;
            scrapper|sc)
                push_image scrapper
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
