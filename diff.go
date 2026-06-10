package blueprint

import (
	"fmt"
	"strings"

	"github.com/google/go-cmp/cmp"
)

// GenerateDiff generates a diff between two blueprint versions.
func GenerateDiff(versionA, versionB *Blueprint) string {
	diff := cmp.Diff(versionA.Content, versionB.Content)
	return strings.ReplaceAll(diff, "\n", "\n    ")
}
