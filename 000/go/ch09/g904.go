//test
package main 

import (
	"fmt"
	)

func test() {
	var x, y int
	go func() {
		x = 1
		fmt.Print("y:", y, " ")
	}()
	go func() {
		y = 1
		fmt.Print("x:", x, " ")
	}()
}
func main() {
	test()
}