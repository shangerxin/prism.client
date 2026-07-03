param(
    [string]$PythonExe = "python",
    [switch]$Upload,
    [switch]$TestPyPI
)

$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

Write-Host "[1/6] Installing build tools (build, twine)..."
& $PythonExe -m pip install --upgrade build twine

Write-Host "[2/6] Cleaning old artifacts..."
if (Test-Path "dist") {
    Remove-Item -Recurse -Force "dist"
}
if (Test-Path "build") {
    Remove-Item -Recurse -Force "build"
}
Get-ChildItem -Directory -Filter "*.egg-info" | Remove-Item -Recurse -Force

Write-Host "[3/6] Building source and wheel distributions..."
& $PythonExe -m build

Write-Host "[4/6] Validating distributions with twine check..."
& $PythonExe -m twine check dist/*

Write-Host "[5/6] Inspecting wheel metadata (Name/Version)..."
$wheel = Get-ChildItem -Path "dist" -Filter "*.whl" | Sort-Object LastWriteTime | Select-Object -Last 1
if (-not $wheel) {
    throw "No wheel file found in dist/."
}

Add-Type -AssemblyName System.IO.Compression.FileSystem
$zip = [System.IO.Compression.ZipFile]::OpenRead($wheel.FullName)
try {
    $metadataEntry = $zip.Entries | Where-Object { $_.FullName -like "*.dist-info/METADATA" } | Select-Object -First 1
    if (-not $metadataEntry) {
        throw "METADATA entry was not found in $($wheel.Name)."
    }

    $reader = New-Object System.IO.StreamReader($metadataEntry.Open())
    try {
        $metadataText = $reader.ReadToEnd()
    }
    finally {
        $reader.Close()
    }
}
finally {
    $zip.Dispose()
}

$nameLine = ($metadataText -split "`n" | Where-Object { $_ -match "^Name:\s*" } | Select-Object -First 1).Trim()
$versionLine = ($metadataText -split "`n" | Where-Object { $_ -match "^Version:\s*" } | Select-Object -First 1).Trim()
Write-Host "  $nameLine"
Write-Host "  $versionLine"

if ($Upload) {
    Write-Host "[6/6] Uploading distributions..."
    if ($TestPyPI) {
        & $PythonExe -m twine upload --repository testpypi dist/*
    }
    else {
        & $PythonExe -m twine upload dist/*
    }
}
else {
    Write-Host "[6/6] Upload skipped."
    if ($TestPyPI) {
        Write-Host "Run to upload to TestPyPI: $PythonExe -m twine upload --repository testpypi dist/*"
    }
    else {
        Write-Host "Run to upload to PyPI: $PythonExe -m twine upload dist/*"
    }
}
