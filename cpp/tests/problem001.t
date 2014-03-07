#!/bin/bash

./problem001 > problem001.out

echo 001: 233168 | diff problem001.out -
