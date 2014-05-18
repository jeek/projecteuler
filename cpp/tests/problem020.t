#!/bin/bash

./problem020 > problem020.out

echo 020: 648 | diff problem020.out -
