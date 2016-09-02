# pipeslash
Pipeslash is an esoteric programming language using | and / as the only characters.
It is Turing complete, although I do not advise doing any serious programming in it.

## Pipeslash grammar

| Command | What it does |
--------- | --------------
| `/|/` | move pointer to the right
| `/||/` | move pointer to the left
| `/|||/` | increment the memory cell under the pointer
| `/||||/` | decrement the memory cell under the pointer
| `/|||||/` | output the character signified by the cell at the pointer
| `/||||||/` | input a character and store it in the cell at the pointer
| `/|||||||/` | jump past the matching `/||||||||/` if the cell under the pointer is 0
| `/||||||||/`| Jump back to the matching `/|||||||/` if the cell under the pointer is nonzero
				
All characters other than / and | are (should be) ignored.

Have fun!
