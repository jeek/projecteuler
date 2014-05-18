#!/bin/bash

./problem012 5 > problem012test.out

echo 012: 28 | diff problem012test.out -
