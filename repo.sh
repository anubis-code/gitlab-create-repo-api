#!/bin/bash

# Define a list of directories
MAINDIR=$PWD
DIRS=(
    "ansible/aws-base.git"
    "ansible/jenkins-cicd.git"
    "terraform/vpn-aws.git"
)

# Loop through each directory and add new remote and push
for dir in "${DIRS[@]}"
do
    cd $MAINDIR
    cd "$dir"
    git remote add --mirror=fetch newServer git@gitlab.example.com:${dir}
    git push newServer --all
   
done