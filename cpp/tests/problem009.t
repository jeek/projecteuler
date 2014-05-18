#!/bin/bash

./problem009 > problem009.out

echo 009: 31875000 | diff problem009.out -
