#!/bin/bash

./problem017 5 > problem017.out

echo 017: 19 | diff problem017.out -
