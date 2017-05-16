# pipeslash
Pipeslash is an esoteric programming language using | and / as the only characters.
It is Turing complete, although I do not advise doing any serious programming in it.
Unless, of course, you feel like trolling your teacher (I disclaim all responsibility of the consequences).
Or if you want to **seriously** confuse an antivirus (again, I take no responsibility.)

## Pipeslash grammar

| Command | What it does |
--------- | --------------
| `/|/` | move pointer to the right |
| `/||/` | move pointer to the left |
| `/|||/` | increment the memory cell under the pointer |
| `/||||/` | decrement the memory cell under the pointer |
| `/|||||/` | output the character signified by the cell at the pointer |
| `/||||||/` | input a character and store it in the cell at the pointer |
| `/|||||||/` | jump past the matching `/||||||||/` if the cell under the pointer is 0 |
| `/||||||||/` | jump back to the matching `/|||||||/` if the cell under the pointer is nonzero |
				
All characters other than / and | are (should be) treated as comments.

## pshi.py
This is the (rather lame) interpreter. It is basically psh2bf attached to a simple brainf*** interpreter.

Usage: `pshi.py [inputfile]`

I plan on writing a better one in the future, but for now this is it.

## psh2bf.py
Translates pipeslash to brainf***

Usage: `psh2bf.py [inputfile] [> outputfile]`

## bf2psh.py
Does the opposite of the above program

Usage: `bf2psh.py [inputfile] [> outputfile]`

## TO DO
- REPL?
- Compiler?
- Auto-formatting in the translators

Have fun with this completely pointless language!

### Bonus License info
All this is licensed under the [Simple Permissive License](https://gist.github.com/SYZYGY-DEV333/98c3b48c0d5a755a0f503b12be8807ac), version 1.0. I like this licence, 
you should check it out!

Also, I might be slightly biased, since I made it.

Whatever, basically just do what you want with my stuff, dont blame me if it goes horribly wrong, 
and give me some credit here and there. That's all :)
