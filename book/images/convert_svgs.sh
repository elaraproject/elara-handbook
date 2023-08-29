#!/bin/sh
for file in *.svg; do inkscape "$file" --export-filename="raster/${file%svg}png"; done
