
mainFileSnippet = """
package main

import (
	"fmt"
	"log"
	"net/http"
)

func main(){
    mux := http.NewServeMux()
    mux.HandleFunc("/hello", func(w http.ResponseWriter, r *http.Request) {
        fmt.Fprint(w, "Hello world")
    })
    log.Fatal(http.ListenAndServe(":8080", mux))
}


"""
passwordHashSnippet = """
package middleware
import (
	"golang.org/x/crypto/bcrypt"
)

func HashPassword(password string) (string, error) {
	hashedPassword, err := bcrypt.GenerateFromPassword([]byte(password), bcrypt.DefaultCost)
	if err != nil {
		return "", err
	}
	return string(hashedPassword), nil
}

func CompareHash(password, hash string) bool {
	err := bcrypt.CompareHashAndPassword([]byte(hash), []byte(password))
	return err == nil
}

"""

jwtSnippet = """
package middleware
import (
	"time"

	"github.com/dgrijalva/jwt-go"
)

var secretKey = []byte("my_secret_key")

type Claims struct {
	jwt.StandardClaims
	UserID uint `json:"user_id"`
}

func GenerateToken(id uint) (string, error) {
	expirationTime := time.Now().Add(time.Minute * 60)
	claims := &Claims{
		UserID: id,
		StandardClaims: jwt.StandardClaims{
			ExpiresAt: expirationTime.Unix(),
		},
	}
	token := jwt.NewWithClaims(jwt.SigningMethodHS256, claims)
	return token.SignedString(secretKey)
}

func ValidateToken(tokenStr string) (*Claims, error) {
	claims := &Claims{}
	token, err := jwt.ParseWithClaims(tokenStr, claims, func(token *jwt.Token) (interface{}, error) {
		return secretKey, nil
	})
	if err != nil {
		return nil, err
	}
	if !token.Valid {
		return nil, jwt.NewValidationError("invalid token", jwt.ValidationErrorSignatureInvalid)
	}
	return claims, nil
}

"""

