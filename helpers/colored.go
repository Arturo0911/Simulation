package helpers

import (
	"fmt"
	"time"

	"github.com/mbndr/figlet4go"
)

func Banner() {
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

	renderStr, _ := ascii.RenderOpts("BINOMIAL", options)
	renderStrBody, _ := ascii.RenderOpts("DISTRIBUTIONS", options)
	fmt.Print(renderStr)
	fmt.Println(renderStrBody)
	time.Sleep(1 * time.Microsecond)
}
