#!/bin/bash
# luajit ./lenet5.lua
yes | th ./slicing.lua
th ./example-linear-regression.lua
