cd docs
rm -rf ./build
sphinx-apidoc -f -d 4 -e -o source ../porcello
sphinx-build -M html source build
sphinx-build -b rinoh source build/rinoh
cp -f build/rinoh/porcello.pdf porcello.pdf
cd ..
