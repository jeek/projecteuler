#!/bin/bash

./problem006 10 > problem006test.out

echo 006: 2640 | diff problem006test.out -
