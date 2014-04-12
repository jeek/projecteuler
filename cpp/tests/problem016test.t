#!/bin/bash

./problem016 15 > problem016.out

echo 016: 26 | diff problem016.out -
