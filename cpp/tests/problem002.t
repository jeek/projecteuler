#!/bin/bash

./problem002 > problem002.out

echo 002: 4613732 | diff problem002.out -
