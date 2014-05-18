#!/bin/bash

./problem001 10 > problem001test.out

echo 001: 23 | diff problem001test.out -
