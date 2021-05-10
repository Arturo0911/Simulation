package helpers

import (
	"flag"
	"fmt"
	"time"

	"github.com/mbndr/figlet4go"
)

var (
	distribution = flag.String("distribution", "binomial", "Kind of distribution to choose")
	elements     = flag.Int("n", 0, "aleatory sample")
	unknown      = flag.Int("x", 0, "aleatory sample")
	probability  = flag.Float64("p", 0.0, "probability success")
)

func banner() {
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

	renderStr, _ := ascii.RenderOpts("BINOMIAL DISTRIBUTIONS", options)
	fmt.Print(renderStr)
	time.Sleep(1 * time.Microsecond)
}

func CLIBanner() {
	banner()
	flag.Parse()
	fmt.Printf("\n[*] distribution %v, elements %v, unknow variable %v and probability %v",
		*distribution, *elements, *unknown, *probability)
}
