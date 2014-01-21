#!/bin/bash

./problem010 10 > problem010test.out

echo 010: 17 | diff problem010test.out -
