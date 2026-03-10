#!/bin/bash

pkg update -y
pkg upgrade -y

pkg install python -y
pkg install git -y

pip install colorama