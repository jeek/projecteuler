#!/bin/bash

./problem011 > problem011.out

echo 011: 70600674 | diff problem011.out -
