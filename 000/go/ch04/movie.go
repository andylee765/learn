// json 
package main 

import (
	"fmt"
	"encoding/json"
	"log"
	)
type Movie struct {
	Title string
	Year int `json:"released"`
	Color bool `json:"color,omitempty"`
	Actors []string
}
var movies = []Movie{
	{Title: "Casablanca", Year: 1942, Color: false,
		Actors: []string{"Humphrey Bogart", "Ingrid Bergman"}},
	{Title: "Cool Hand Luke", Year: 1967, Color: true,
		Actors: []string{"Palul Newman"}},
	{Title: "Bullitt", Year: 1968, Color: true,
		Actors: []string{"Steve McQueen", "Jacqueline Bisset"}},
}
func test_json(){
	fmt.Printf("%v\n", movies)
	data, err := json.Marshal(movies)
	if err != nil {
		log.Fatalf("JSON marshaling failed: %s", err)
	}
	fmt.Println("After marshaling:")
	fmt.Printf("%s\n", data)
	data, err = json.MarshalIndent(movies, "", "  ")
	if err != nil {
		log.Fatalf("JSON marshaling failed: %s", err)
	}
	fmt.Println("After Marshal Indent:")
	fmt.Printf("%s\n", data)
}
func main() {
	test_json()
	fmt.Println("json.")
}