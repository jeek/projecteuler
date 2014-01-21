#!/bin/bash

./problem015 > problem015.out

echo 015: 137846528820 | diff problem015.out -
