param(
    [string]$PythonExe = "python",
    [switch]$Upload,
    [switch]$TestPyPI
)

$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

Write-Host "[1/5] Installing build tools (build, twine)..."
& $PythonExe -m pip install --upgrade build twine

Write-Host "[2/5] Cleaning old artifacts..."
if (Test-Path "dist") {
    Remove-Item -Recurse -Force "dist"
}
if (Test-Path "build") {
    Remove-Item -Recurse -Force "build"
}
Get-ChildItem -Directory -Filter "*.egg-info" | Remove-Item -Recurse -Force

Write-Host "[3/5] Building source and wheel distributions..."
& $PythonExe -m build

Write-Host "[4/5] Validating distributions with twine check..."
& $PythonExe -m twine check dist/*

if ($Upload) {
    Write-Host "[5/5] Uploading distributions..."
    if ($TestPyPI) {
        & $PythonExe -m twine upload --repository testpypi dist/*
    }
    else {
        & $PythonExe -m twine upload dist/*
    }
}
else {
    Write-Host "[5/5] Upload skipped."
    if ($TestPyPI) {
        Write-Host "Run to upload to TestPyPI: $PythonExe -m twine upload --repository testpypi dist/*"
    }
    else {
        Write-Host "Run to upload to PyPI: $PythonExe -m twine upload dist/*"
    }
}
