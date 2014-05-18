#!/bin/bash

./problem020 10 > problem020test.out

echo 020: 27 | diff problem020test.out -
