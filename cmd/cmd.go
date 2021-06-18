package cmd

import (
	"fmt"
	"strconv"
	"strings"
)

func usage() {
	fmt.Println("\nGuia de uso")
	fmt.Println("1.- Si tienes los valores de las probabilidades y cuanto corresponde cada uno entonces ingresalos,\n    caso contrario presiona ENTER y se te otorgará valores predeterminados para probar el algoritmo")
	fmt.Println("\n2.- En caso de que quieras salir del programa, presiona la tecla X en mayúscula o minúscula.")
}

func defaultValues(defaultValues string) ([]int64, []float64) {

	if (strings.ToLower(defaultValues)) == "d" || (strings.ToLower(defaultValues) == "default") {
		return []int64{-5, 1, 2, 3}, []float64{0.125, 0.50, 0.25, 0.125}
	} else {
		return nil, nil
	}
}

func CLI() error {
	InitBanner()
	usage()
	var number int
	fmt.Println("Ingresa la cantidad de valores de x y p: ")
	fmt.Scan(&number)
	var firstStep string
	var xValues []int64
	var pValues []float64

	fmt.Println("elige d/determinado por valores determinados \n o  p/customized por personalizados")
	fmt.Scan(&firstStep)
	x, p := defaultValues(firstStep)

	if x == nil && p == nil {
		fmt.Println("Ingresa los valores propios: ")
		fmt.Print("Los valores para Z(x): ")
		var xWherever string
		var pWherever string
		fmt.Scan(&xWherever)
		fmt.Scan(&pWherever)

		xWherever_ := strings.Split(xWherever, " ")
		strings.Split(pWherever, " ")
		for x := 0; x < len(xWherever_); x++ {
			valueInt, _ := strconv.Atoi(xWherever_[x])
			valueFloat, _ := strconv.ParseFloat(strings.Split(xWherever, " ")[x], 64)
			xValues[x] = int64(valueInt)
			pValues[x] = valueFloat
		}
		fmt.Println(xValues)
		fmt.Println(pValues)
	}

	return nil
}
