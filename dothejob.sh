# Uncomment this stuff if you need it
# ./autogen.sh --host=i686-w64-mingw32
# Uncomment this thing under ONLY IF you have a configure script
# ./configure

make clean
cd pkg/win32
make clean
cd ../..
make -j4
cd pkg/win32
make -j4
cd staging-doom

# BTW this code is designed to be runned in a MSYS2 MINGW64 environment
