// pipeslash compiler to C
// Copyright (c) 2017, SYZYGY-DEV333
// All rights reserved.
// Licensed under SPL 1.0 [bit.ly/splicense]
package main

import (
	"fmt"
	"io/ioutil"
	"os"
	"strings"
	"regexp"
)

var content_bytearray, err = ioutil.ReadFile(os.Args[1])
var content = string(content_bytearray[:])

func cleanup(src string) string {
	reg := regexp.MustCompile("[^|/]+")
	return reg.ReplaceAllString(content, "")
}

func translate(src string) string {
	dic := strings.NewReplacer("/|/", "++ptr;\n",
		"/||/", "--ptr;\n",
		"/|||/", "++*ptr;\n",
		"/||||/", "--*ptr;\n",
		"/|||||/", "putchar(*ptr);\n",
		"/||||||/", "*ptr=getchar();\n",
		"/|||||||/", "while (*ptr) {\n",
		"/||||||||/", "}\n")
	return dic.Replace(src)
}

// allow dynamic tape sizing in the future
var beginning = (
`#include <stdio.h>
int main(){
char array[30000] = {0};
char *ptr=array;`)

func main() {
	ccode := translate(cleanup(content))
	fmt.Printf(beginning)
	fmt.Printf("\n")
	fmt.Printf(ccode)
	fmt.Printf("}\n")
}
