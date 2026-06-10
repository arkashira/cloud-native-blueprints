// Before
package versioning

import (
	"fmt"
	"os"
	"path/filepath"
)

// After
import (
	"github.com/go-git/go-git/v5"
	"github.com/go-git/go-git/v5/plumbing"
	"github.com/go-git/go-git/v5/plumbing/object"
	"time"
)

func InitGitRepo(dir string) error {
	_, err := git.PlainOpen(dir)
	if err != nil && !os.IsNotExist(err) {
		return err
	}

	repo, err := git.Init(dir, false)
	if err != nil {
		return err
	}

	return repo.Close()
}

func CommitHCLFiles(repo *git.Repository, files map[string]string, clusterName string) error {
	worktree, err := repo.Worktree()
	if err != nil {
		return err
	}

	for path, content := range files {
		err = worktree.Write(path, []byte(content), &git.WorktreeOptions{
			Message: fmt.Sprintf("Generated blueprint for %s at %s", clusterName, time.Now().Format(time.RFC3339)),
		})
		if err != nil {
			return err
		}
	}

	_, err = worktree.Commit("Add generated blueprint files")
	if err != nil {
		return err
	}

	return repo.Close()
}