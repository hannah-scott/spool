# spool

Plaintext tools for [Tape](https://aeriform.itch.io/tape). Unspool your tape into a plaintext file, do some edits, then spool it back up!

## Usage

0. Close Tape
   - Tape doesn't seem to check for updates before making changes to tables: keeping it open can overwrite your changes
1. In both `unspool.py` and `spool.py`, change `tapeDB` to point to your Tape database
   - In Linux this is under `~/.config/Tape` by default
   - You can also symlink `file.sqlite` to point to the DB, no real impact either way
2. Run `unspool.py` to create a YAML file containing your DB information
3. Make some changes, save the file
4. Run `spool.py` to roll everything back up into Tape
5. Reopen Tape and see your changes!

When making changes and adding new collections you can use whatever ID system you want, e.g. 1-2-3, a-b-c. Tape picks random ones, but there isn't a set format as long as IDs are unique.

## Copything

I exert no copyright over this code, and you should feel free to do whatever you want with it. If you are unsure about whether you can use this code for something: you can!

[Tape](https://aeriform.itch.io/tape) is the intellectual property of [Aeriform](https://www.aeriform.io/). They made an extremely cool tool, and if you're able you should support them financially.
