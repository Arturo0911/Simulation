package cmd

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func usage() {
	fmt.Println("\nGuia de uso")
	fmt.Println("1.- Si tienes los valores de las probabilidades y cuanto corresponde cada uno entonces ingresalos,\n    caso contrario presiona ENTER y se te otorgará valores predeterminados para probar el algoritmo")
	fmt.Println("\n2.- En caso de que quieras salir del programa, presiona la tecla X en mayúscula o minúscula.")
}

/*func defaultValues(defaultValues string) ([]int64, []float64) {

	if (strings.ToLower(defaultValues)) == "d" || (strings.ToLower(defaultValues) == "default") {
		return []int64{-5, 1, 2, 3}, []float64{0.125, 0.50, 0.25, 0.125}
	} else {
		return nil, nil
	}
}*/

func CheckValues() error {
	return nil
}

func CLI() {
	InitBanner()
	usage()
	scanner := bufio.NewScanner(os.Stdin)

	var xValues []int64
	var pValues []float64
	counter := 0
	for {
		scanner.Scan()
		fmt.Println("Indica los valores de X: ")
		line := scanner.Text()
		fmt.Println("\nIndica los valores probabilísticos de P: ")
		line = scanner.Text()

		if len(strings.Split(line, "")) != len(strings.Split(line_, "")) {
			continue
		}
		fmt.Println(line)
		fmt.Println(line_)
		for i := 0; i < len(strings.Split(line, "")); i++ {

			valueInt, _ := strconv.Atoi(strings.Split(line, "")[i])
			valueFloat, _ := strconv.ParseFloat(strings.Split(line_, "")[i], 64)
			xValues = append(xValues, int64(valueInt))
			pValues = append(pValues, valueFloat)
		}

	}

	fmt.Println("valores de x: ", xValues)
	fmt.Println("valores de p: ", pValues)

}
