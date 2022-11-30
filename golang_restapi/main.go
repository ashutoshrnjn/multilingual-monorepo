package main

import (
	"encoding/json"
	"net/http"
)

type User struct {
	Email    string `json:"email"`
	Password string `json:"password"`
}

func main() {
	http.HandleFunc("/login", func(w http.ResponseWriter, r *http.Request) {
		var user User
		err := json.NewDecoder(r.Body).Decode(&user)
		if err != nil {
			http.Error(w, "Invalid request body", http.StatusBadRequest)
			return
		}

		// Authenticate user
		if user.Email == "test@example.com" && user.Password == "password" {
			w.Write([]byte("User authenticated"))
		} else {
			http.Error(w, "Invalid email or password", http.StatusUnauthorized)
		}
	})

	http.ListenAndServe(":8080", nil)
}
