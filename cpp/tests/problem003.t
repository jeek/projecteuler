#!/bin/bash

./problem003 > problem003.out

echo 003: 6857 | diff problem003.out -
