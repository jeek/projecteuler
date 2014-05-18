#!/bin/bash

./problem004 > problem004.out

echo 004: 906609 | diff problem004.out -
