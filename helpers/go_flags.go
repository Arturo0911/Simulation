package helpers

import (
	"errors"
	"flag"
	"fmt"
	"log"
	"math"
	"strconv"
	"strings"

	"github.com/Arturo0911/Simulation/distribution"
)

var (
	dist        = flag.String("dist", "binomial", "Kind of distribution to choose")
	value       = flag.Float64("u", 0, "value desired")
	elements    = flag.Int("n", 0, "aleatory sample")
	unknown     = flag.Float64("x", 0, "aleatory sample")
	probability = flag.Float64("p", 0.0, "probability success")
	keyword     = flag.String("k", "eq",
		"At least (at), at the most (am) or exactly the same(eq); these values should be separeted with a comma to be parsed")
)

// Binomial
func binomialProcess(flag_ string, n int, p float64) (float64, error) {

	key := strings.Split(flag_, ",")
	var finalResult float64

	if len(key) <= 1 {
		return finalResult,
			errors.New("you should to pass second parameter as the number to get the distribution")
	}

	switch key[0] {
	case "eq": // means value == x
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
func geometricProcess(p float64, x int) (float64, error) {
	geoDis := distribution.NewGeoDistribution(p, x)
	return geoDis.DistributionGeometric(), nil
}

func poissonProces(u int) (float64, error) {

	if !math.IsNaN(*unknown) {
		possDis := distribution.NewPoissonDistribution(u, int(*unknown))
		return possDis.DistributionPoisson(), nil
	} else {
		return 0, errors.New("'x' value cannot be empty or NaN")
	}

}

func CLI() {
	Banner()
	fmt.Print("\n[*] If you not include the respective tag and the value, then default value will be zero.\n")
	fmt.Print("[*] Starting CLI\n")
	flag.Parse()
	fmt.Printf("[*] distribution %v, elements %v, unknow variable %v and probability %v\n\n",
		*dist, *elements, *unknown, *probability)

	switch *dist {
	case "bin":
		result, err := binomialProcess(*keyword, *elements, *probability)
		if err != nil {
			log.Fatal(err)
		}
		fmt.Println("Distribution binomial is => ", result)
	case "geo":
		value, err := geometricProcess(*probability, int(*unknown))
		if err != nil {
			log.Fatal(err)
		}
		fmt.Println("Distribution geometric is => ", value)
	case "pos":

		if math.IsNaN(*value) {
			fmt.Println("Value cannot be empty")
		} else {
			poissonVal, err := poissonProces(int(*value))
			if err != nil {
				log.Fatal(err)
			}

			fmt.Printf("value is %0.5f or %0.2f percent \n", poissonVal, (poissonVal * 100))
		}

	default:
		fmt.Println("<=>")
	}

}
