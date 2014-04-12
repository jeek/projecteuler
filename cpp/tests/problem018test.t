#!/bin/bash

./problem018 3 7 4 2 4 6 8 5 9 3 > problem018test.out

echo 018: 23 | diff problem018test.out -
