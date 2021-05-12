package distribution

import (
	"fmt"
	"log"
	"math"
	"strconv"
)

//		888888b.  d8b                             d8b        888
//		888  "88b Y8P                             Y8P        888
//		888  .88P                                            888
//		8888888K. 88888888b.  .d88b. 88888b.d88b. 888 8888b. 888
//		888  "Y88b888888 "88bd88""88b888 "888 "88b888    "88b888
//		888    888888888  888888  888888  888  888888.d888888888
//		888   d88P888888  888Y88..88P888  888  888888888  888888
//		8888888P" 888888  888 "Y88P" 888  888  888888"Y888888888

//		8888888b. d8b        888          d8b888             888   d8b
//		888  "Y88bY8P        888          Y8P888             888   Y8P
//		888    888           888             888             888
//		888    888888.d8888b 888888888d88888888888b. 888  888888888888 .d88b. 88888b.
//		888    88888888K     888   888P"  888888 "88b888  888888   888d88""88b888 "88b
//		888    888888"Y8888b.888   888    888888  888888  888888   888888  888888  888
//		888  .d88P888     X88Y88b. 888    888888 d88PY88b 888Y88b. 888Y88..88P888  888
//		8888888P" 888 88888P' "Y888888    88888888P"  "Y88888 "Y888888 "Y88P" 888  888

type DistributionParameters struct {
	N int     // Quantity of elements to be processed
	P float64 // probability success about that event
	X int     // Variable to discover
}

type GeometricParameters struct {
	P float64
	X int
}

type PoissonParameters struct {
	U int
	X int
}

type Distribution interface {
	Combinatory() float64
	DistributionBinomial() float64
	DistributionGeometric() float64
	DistributionPoisson() float64
	BinomialNegative() float64
}

func NewDistribution(n, x int, p float64) *DistributionParameters {

	return &DistributionParameters{
		N: n,
		X: x,
		P: p,
	}
}

func NewGeoDistribution(p float64, x int) *GeometricParameters {
	return &GeometricParameters{
		P: p,
		X: x,
	}
}

func NewPoissonDistribution(u, x int) *PoissonParameters {
	return &PoissonParameters{
		U: u,
		X: x,
	}
}

func Factorial(value int) int {

	if value == 0 || value == 1 {
		return 1
	}

	for i := value - 1; i >= 1; i-- {
		value *= i
	}
	return value

}

func (bin *DistributionParameters) Combinatory(n, x int) float64 {

	return float64(Factorial(bin.N) / (Factorial(bin.N-bin.X) * Factorial(bin.X)))

}

func (bin *DistributionParameters) DistributionBinomial() float64 {

	final, err := strconv.ParseFloat(fmt.Sprintf("%0.4f", (bin.Combinatory(bin.N, bin.X))*(math.Pow(bin.P,
		float64(bin.X)))*(math.Pow(float64(1-bin.P), float64(bin.N-bin.X)))), 64)

	if err != nil {
		log.Fatal(err)
		return 0
	}
	return final
}

func (geo *GeometricParameters) DistributionGeometric() float64 {
	// Time to test to get the frist success
	return (geo.P * math.Pow((1-geo.P), float64(geo.X-1)))
}

func (poisson *PoissonParameters) DistributionPoisson() float64 {
	return (math.Exp(float64(-poisson.U)) * math.Pow(float64(poisson.U), float64(poisson.X))) / float64(Factorial(poisson.X))
}
