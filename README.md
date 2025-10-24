# DOOM Cosine Chaos

DOOM Cosine Chaos is a fork of [Chocolate-DOOM](chocolate-doom.org), and it is not a normal one, but a (ALMOST) non-euclidean one! This DOOM port simply has a thing in it... in `src/tables.c`, the `finesine` and `finetangent` are modified so it is non-euclidean! There is also a python script there called `corrupt_sine.py` which is designed to re-corrupt the `finesine` and `finetangent` tables!
This is a Chocolate-DOOM port by the way (i repeated the same thing btw).

DOOM Cosine Chaos has:

 * To always be 100% Free and Open Source software.
 * Support to some OSes (Linux, Windows, whatever)
 * CORRUPTED SINE TABLES
 * Compatibility with the DOS demo, configuration and savegame files.
 * A accurate recreation of the original DOS game, but with non-euclidean stuff!

You may find many similarities to Chocolate-DOOM tho!

## HOW THE HELL DO I COMPILE?!?!?!?
DONT YELL INTO YOUR COMPUTER SCREEN! I'll tell you how to compile this thing, first, i've made some automation scripts but they are only for Windows with MSYS2 MINGW64, and the automation script is called `dothejob.sh`, and it is designed to be executed inside MSYS2 MINGW64! And there are some comments in that script that you can uncomment if you need to! For linux, just check out [compiling chocolate-DOOM on Linux](https://www.chocolate-doom.org/wiki/index.php/Building_Chocolate_Doom_on_Debian)... (but we are supposed to compile DOOM Cosine Chaos, okay?)
