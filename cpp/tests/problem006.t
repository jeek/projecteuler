#!/bin/bash

./problem006 > problem006.out

echo 006: 25164150 | diff problem006.out -
