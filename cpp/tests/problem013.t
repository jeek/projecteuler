#!/bin/bash

./problem013 > problem013.out

echo 013: 5537376230 | diff problem013.out -
