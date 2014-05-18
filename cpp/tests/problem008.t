#!/bin/bash

./problem008 > problem008.out

echo 008: 40824 | diff problem008.out -
