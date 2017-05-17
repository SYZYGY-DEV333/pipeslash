// pipeslash interpreter
// Copyright (c) 2017, SYZYGY-DEV333
// All rights reserved.
// Licensed under SPL 1.0 [bit.ly/splicense]
package main

import (
	"fmt"
	"io/ioutil"
	"os"
	"strings"
)

var content_bytearray, err = ioutil.ReadFile(os.Args[1])
var content = string(content_bytearray[:])

func translate(src string) string {
	dic := strings.NewReplacer("/|/", ">",
		"/||/", "<",
		"/|||/", "+",
		"/||||/", "-",
		"/|||||/", ".",
		"/||||||/", ",",
		"/|||||||/", "[",
		"/||||||||/", "]",
		" ", "")
	return dic.Replace(src)
}

func interpret(src string) []uint8 {
	tape := []uint8{0}
	tapeIndex := 0

	srcLength := len(src)

	for srcIndex := 0; srcIndex < srcLength; srcIndex++ {

		switch src[srcIndex] {
		case '>':				// Move Pointer to the Right
			tapeIndex += 1
			if len(tape) <= tapeIndex {
				tape = append(tape, 0)
			}

		case '<':				// Move Pointer to the Left
			if tapeIndex > 0 {
				tapeIndex -= 1
			}

		case '+':				// Increment the memory cell under the pointer
			tape[tapeIndex] += 1

		case '-':				// Deincrement the memory cell under the pointer
			tape[tapeIndex] -= 1

		case '.':				// Output the character signified by the cell at the pointer
			fmt.Print(string(tape[tapeIndex]))

		case ',':				// Input a character and store it in the cell at the pointer
			b := make([]byte, 1)
			os.Stdin.Read(b)
			tape[tapeIndex] = b[0]

		case '[':			// jump past the matching `/||||||||/` if the cell under the pointer is 0
			if tape[tapeIndex] == 0 {
				for depth := 1; depth > 0; {
					srcIndex++
					srcCharacter := src[srcIndex]
					if srcCharacter == '[' {
						depth++
					} else if srcCharacter == ']' {
						depth--
					}
				}
			}

		case ']':			// jump back to the matching /|||||||/ if the cell under the pointer is nonzero
			for depth := 1; depth > 0; {
				srcIndex--
				srcCharacter := src[srcIndex]
				if srcCharacter == '[' {
					depth--
				} else if srcCharacter == ']' {
					depth++
				}
			}
			srcIndex--
		}
	}

	return tape
}

func main() {
	if err != nil {
		fmt.Println("Error reading file")
		fmt.Println(err)
	} else {
		var src = translate(content)
		interpret(src)
	}
}
