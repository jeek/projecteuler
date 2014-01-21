#!/bin/bash

./problem004 2 > problem004test.out

echo 004: 9009 | diff problem004test.out -
