package main

import (
	"fmt"
	"strconv"

	"github.com/Arturo0911/Simulation/evaluation"
	"github.com/Arturo0911/Simulation/helpers"
)

func CLI() {
	fmt.Println("USE THE FOLLOWING COMMANDS TO GET THE RESULT")
}

func main() {
	helpers.CLIBanner()

	coinDistribution1 := evaluation.NewDistribution(4, 3, 0.5)
	coinDistribution2 := evaluation.NewDistribution(4, 4, 0.5)
	fmt.Println(coinDistribution1.DistributionBinomial())
	fmt.Println(coinDistribution2.DistributionBinomial())

	c1, err := strconv.ParseFloat(coinDistribution1.DistributionBinomial(), 64)
	if err != nil {
		fmt.Println(err.Error())
	}

	c2, err := strconv.ParseFloat(coinDistribution2.DistributionBinomial(), 64)
	if err != nil {
		fmt.Println(err.Error())
	}

	fmt.Println(c1 + c2)

}
