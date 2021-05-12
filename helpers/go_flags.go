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

var euler = math.Exp(float64(1))
var (
	dist        = flag.String("dist", "binomial", "Kind of distribution to choose")
	value       = flag.Int("u", 0, "value desired")
	elements    = flag.Int("n", 0, "aleatory sample")
	unknown     = flag.Int("x", 0, "aleatory sample")
	probability = flag.Float64("p", 0.0, "probability success")
	keyword     = flag.String("k", "eq",
		"At least (at), at the most (am) or exactly the same(eq); these values should be separeted with a comma to be parsed")
)

func usage() {
	fmt.Println("The right words ar bin =>(binomial) \n or")
	fmt.Println("To choose binomial distribution use -dist=bin -n=<number of elements> -x=<number to get success> -p probability -k=at,<number> or -k=am,<number> or -k=eq,<number>")
	fmt.Println("The right word ar geo =>(geometric)\n or")
	fmt.Println("The right words ar pos =>(poisson)\n or")
	fmt.Println("The right words ar neg =>(binomial negative)\n or")
}

// Binomial
func binomialProcess(flag_ string, n int, p float64) (float64, error) {

	key := strings.Split(flag_, ",")
	var finalResult float64

	if len(key) <= 1 {
		return finalResult,
			errors.New("you should to pass second parameter as the number to get the distribution")
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
func geometricProcess(p float64, x int) (float64, error) {
	geoDis := distribution.NewGeoDistribution(p, x)
	return geoDis.DistributionGeometric(), nil
}

func poissonProces() {}

func CLI() {
	fmt.Println(euler)
	Banner()
	fmt.Println("USE THE FOLLOWING COMMANDS TO GET THE RESULT")
	fmt.Print("\n[*]Starting CLI")
	flag.Parse()
	fmt.Printf("\n[*] distribution %v, elements %v, unknow variable %v and probability %v\n\n",
		*dist, *elements, *unknown, *probability)

	switch *dist {
	case "bin":
		result, err := binomialProcess(*keyword, *elements, *probability)
		if err != nil {
			log.Fatal(err)
		}
		fmt.Println("Distribution binomial is => ", result)
	case "geo":
		value, err := geometricProcess(*probability, *unknown)
		if err != nil {
			log.Fatal(err)
		}
		fmt.Println("Distribution geometric is => ", value)
	case "pos":

		switch *value {

		default:
			fmt.Println("You should to choose the -u flag with a value different to zero")

		}

		poissonProces()

	default:
		usage()
	}

}
