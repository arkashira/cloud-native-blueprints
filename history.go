import (
	"github.com/axentix/cloud-native-blueprints/pkg/blueprint"
	. "github.com/smartystreet/goconvey/convey"
)

func TestDiff(t *testing.T) {
	Convey("Given two blueprint versions", t, func() {
		version1 := blueprint.Blueprint{Data: `{"key": "value1"}`}
		version2 := blueprint.Blueprint{Data: `{"key": "value2"}`}

		Convey("When calling Diff function", func() {
			diff, err := blueprint.Diff(version1, version2)
			So(err, ShouldBeNil)

			Convey("Then the diff output should match the expected result", func() {
				expectedDiff := `- {"key": "value1"}
+ {"key": "value2"}`
				So(diff, ShouldEqual, expectedDiff)
			})
		})

		Convey("When one of the versions is empty", func() {
			emptyVersion := blueprint.Blueprint{}

			diff, err := blueprint.Diff(emptyVersion, version2)
			So(err, ShouldBeNil)

			Convey("Then the diff output should indicate that the empty version has no changes", func() {
				expectedDiff := `No changes in empty version`
				So(diff, ShouldEqual, expectedDiff)
			})
		})
	})
}