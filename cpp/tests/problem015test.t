#!/bin/bash

./problem015 2 > problem015.out

echo 015: 6 | diff problem015.out -
