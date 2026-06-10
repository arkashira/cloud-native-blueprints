
# Verification
1. Run `python main.py invalid-file.yaml` - Should show specific error message without crashing
2. Run `python main.py valid-blueprint.yaml` - Should process without errors
3. Check for `import sys` in main module using: `grep 'import sys' main.py`
4. Verify no generic exception handling remains: `grep -r 'except Exception' .`