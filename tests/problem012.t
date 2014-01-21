#!/bin/bash

./problem012 > problem012.out

echo 012: 76576500 | diff problem012.out -
