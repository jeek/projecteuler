#!/bin/bash

./problem010 > problem010.out

echo 010: 142913828922 | diff problem010.out -
