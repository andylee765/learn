// Chapter 7.06
package main 

import (
	"fmt"
	"sort"
	)

type StringSlice  []string
func (p StringSlice) Len() int				{ return len(p) }
func (p StringSlice) Less(i, j int) bool 	{ return p[i] < p[j]}
func (p StringSlice) Swap(i, j int)			{ p[i], p[j] = p[j], p[i]}
func test_sort() {
	s := []string{"g", "a", "d", "b", "c"}
	fmt.Println(s)
	sort.Sort(StringSlice(s))
	fmt.Println(s)
}

func main() {
	test_sort()

}
