package helpers

import (
	"errors"
	"flag"
	"fmt"
	"log"
	"strconv"
	"strings"

	"github.com/Arturo0911/Simulation/distribution"
)

var (
	dist        = flag.String("distribution", "binomial", "Kind of distribution to choose")
	elements    = flag.Int("n", 0, "aleatory sample")
	unknown     = flag.Int("x", 0, "aleatory sample")
	probability = flag.Float64("p", 0.0, "probability success")
	keyword     = flag.String("k", "eq",
		"At least (at), at the most (am) or exactly the same(eq); these values should be separeted with a comma to be parsed")
)

// Binomial
func binomialProcess(flag_ string, n int, p float64) (float64, error) {

	key := strings.Split(flag_, ",")
	var finalResult float64

	if len(key) <= 1 {
		return 0, errors.New("you should to pass second parameter as the number to get the distribution")
	}

	switch key[0] {
	case "eq":
		number, err := strconv.Atoi(key[1])
		if err != nil {
			log.Fatal(err)
		}
		//in the case that the required process is exactky equals
		newDist := distribution.NewDistribution(n, number, p)

		return newDist.DistributionBinomial(), nil
	case "at": // means  value >= x

		number, err := strconv.Atoi(key[1])
		if err != nil {
			log.Fatal(err)
		}
		for i := number; i <= n; i++ {
			newDist := distribution.NewDistribution(n, i, p)
			finalResult += newDist.DistributionBinomial()
		}
		return finalResult, nil

	case "am": // means  value <= x

		number, err := strconv.Atoi(key[1])
		if err != nil {
			log.Fatal(err)
		}
		for i := number; i >= 0; i-- {
			newDist := distribution.NewDistribution(n, i, p)
			finalResult += newDist.DistributionBinomial()
		}
		return finalResult, nil
	}

	return finalResult, nil

}

// Geometric
func geometricProcess() {

}

func poissonProces() {}

func CLI() {
	Banner()
	fmt.Println("USE THE FOLLOWING COMMANDS TO GET THE RESULT")
	flag.Parse()
	fmt.Printf("\n[*] distribution %v, elements %v, unknow variable %v and probability %v\n\n",
		*dist, *elements, *unknown, *probability)

	switch *dist {
	case "binomial":
		result, err := binomialProcess(*keyword, *elements, *probability)
		if err != nil {
			log.Fatal(err)
		}
		fmt.Println(result)
	case "geometric":
		geometricProcess()
	case "poisson":
		poissonProces()
	}

}
