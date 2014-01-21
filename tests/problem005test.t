#!/bin/bash

./problem005 10 > problem005test.out

echo 005: 2520 | diff problem005test.out -
