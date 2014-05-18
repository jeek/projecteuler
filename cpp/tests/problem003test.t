#!/bin/bash

./problem003 13195 > problem003test.out

echo 003: 29 | diff problem003test.out -
