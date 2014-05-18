#!/bin/bash

./problem007 6 > problem007test.out

echo 007: 13 | diff problem007test.out -
