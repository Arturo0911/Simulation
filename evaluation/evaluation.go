package evaluation

import (
	"fmt"
	"math"
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

type BinomialDitribution struct {
	N int
	P float64
	X int
}

type Distribution interface {
	Combinatory() float64
	DistributionBinomial() string
}

func NewDistribution(n, x int, p float64) *BinomialDitribution {

	return &BinomialDitribution{
		N: n,
		X: x,
		P: p,
	}
}

func Factorial(value int) int {

	if value == 0 {
		return 1
	}

	for i := value - 1; i >= 1; i-- {
		value *= i
	}
	return value

}

func (bin *BinomialDitribution) Combinatory(n, x int) float64 {

	return float64(Factorial(bin.N) / (Factorial(bin.N-bin.X) * Factorial(bin.X)))

}

func (bin *BinomialDitribution) DistributionBinomial() string {

	return fmt.Sprintf("%0.4f", (bin.Combinatory(bin.N, bin.X))*(math.Pow(bin.P,
		float64(bin.X)))*(math.Pow(float64(1-bin.P), float64(bin.N-bin.X))))
}
