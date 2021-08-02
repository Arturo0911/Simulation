package main

import (
	"fmt"
	"time"

	"github.com/mbndr/figlet4go"
)

func showMenu() {

	// ...

	time.Sleep(1 * time.Millisecond)
	ascii := figlet4go.NewAsciiRender()

	// Adding the colors to RenderOptions
	options := figlet4go.NewRenderOptions()

	term, _ := figlet4go.NewTrueColorFromHexString("885DBA")
	options.FontColor = []figlet4go.Color{
		// Colors can be given by default ansi color codes...
		figlet4go.ColorGreen,
		figlet4go.ColorYellow,
		figlet4go.ColorCyan,
		// ...or by an hex string...
		term,
		// ...or by an TrueColor object with rgb values
		//figlet4go.TrueColor{136, 93, 186},
	}

	renderStr, _ := ascii.RenderOpts("Algoritmo Congruencial", options)
	renderStrBody, _ := ascii.RenderOpts("Multiplicativo", options)
	fmt.Print(renderStr)
	fmt.Println(renderStrBody)
	time.Sleep(1 * time.Microsecond)
	fmt.Println("[*] Made it by: ARTURO FRANCESCO NEGREIROS SAMANEZ")
	fmt.Println("[*] Course: 7mo SB")
	fmt.Println("[*] Contact: arturo.negreiros.samanez@uagraria.edu.ec")
	fmt.Println("[*] Ingresa 'no' en cualquier momento y saldras del programa")
	fmt.Println("[*] Valores a ingresar:")
}

func uniformNumber(seed, a, m, n int) {

	rangeNumbers := make([]float64, n)
	//fmt.Println(seed)
	for i := 0; i < n; i++ {
		product := (seed * a) % m
		//fmt.Println(product)
		z := float64(product) / float64(m)
		rangeNumbers[i] = z
		seed = product
	}
	fmt.Print("___________________________________________\n\n")
	fmt.Println("Terminos         ||         valor generado")
	fmt.Print("___________________________________________\n\n")
	for _, num := range rangeNumbers {
		fmt.Println(num)
	}
	fmt.Println("___________________________________________")
}

func main() {
	showMenu()
	for {
		var (
			seed        int
			number      int
			module      int
			rangeNumber int
			response    string
		)
		fmt.Print("Ingrese la semilla: ")
		fmt.Scan(&seed)
		fmt.Print("\ningrese a: ")
		fmt.Scan(&number)

		fmt.Print("\nIngrese m: ")
		fmt.Scan(&module)

		fmt.Print("\nIngrese el rango a calcular: ")
		fmt.Scan(&rangeNumber)

		uniformNumber(seed, number, module, rangeNumber)

		fmt.Println("[*] ¿ Desea continuar ? yes/no")
		fmt.Scan(&response)
		if response != "yes" {
			break
		} else {
			continue
		}
	}

}
