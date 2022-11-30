package main

import (
	"fmt"
	"math/rand"
	"net/http"
)

func main() {
	http.HandleFunc("/", handler)
	http.ListenAndServe(":5000", nil)
}

func handler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "%d", rand.Int())
}
