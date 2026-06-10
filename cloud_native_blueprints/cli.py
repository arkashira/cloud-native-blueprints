# test_readme_structure.py
import re
import pathlib

README = pathlib.Path("cloud-native-blueprints/README.md").read_text()

def test_quick_start_section_exists():
    assert "# Quick Start" in README

def test_quick_start_steps_count():
    steps = re.findall(r"^\s*\d+\.\s", README, re.MULTILINE)
    assert len(steps) == 5, f"Expected 5 steps, found {len(steps)}"

def test_each_step_has_command_and_output():
    for i in range(1, 6):
        cmd_pattern = rf"^\s*{i}\.\s+`([^`]+)`"
        out_pattern = rf"^\s*{i}\.\s+`[^`]+`\s+Output:\n```\n([^\n]+)\n```"
        assert re.search(cmd_pattern, README, re.MULTILINE), f"Step {i} missing command"
        assert re.search(out_pattern, README, re.MULTILINE), f"Step {i} missing expected output"

def test_example_blueprints_section():
    assert "## Example Blueprints" in README
    workloads = ["microservices", "postgresql", "redis"]
    for wl in workloads:
        assert f"- {wl}" in README, f"Missing example for {wl}"

def test_troubleshooting_section():
    assert "## Troubleshooting" in README
    issues = ["Authentication", "Missing CRDs", "Network Policy", "Resource Limits"]
    for issue in issues:
        assert issue in README, f"Missing troubleshooting for {issue}"