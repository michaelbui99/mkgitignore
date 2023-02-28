Write-Output "Setting up mkgitignore..."

$scriptsPath = "$HOME/Scripts"
$workingDir = Get-Location

if (-not (Test-Path $scriptsPath)) {
    Write-Output "Creating new Scripts folder..."
    Set-Location $HOME && mkdir Scripts
}

Set-Location $scriptsPath

if (Test-Path "$scriptsPath/mkgitignore") {
    Write-Output "Removing existing mkgitignore..."
    Remove-Item mkgitignore -R -Force
}

git clone https://github.com/michaelbui99/mkgitignore.git

Set-Location mkgitignore
python -m venv venv
.\venv\Scripts\activate
Write-Output "Installing dependencies..."
pip install -r requirements.txt

Write-Output "Adding new function to $PROFILE ..."
$scriptFunction = @"
function mkgitignore(`$template) {
    $HOME\Scripts\mkgitignore\venv\Scripts\Activate.ps1
    python $HOME\Scripts\mkgitignore\mkgitignore\main.py `$template
}
"@

Write-Output `n >> $PROFILE
Write-Output $scriptFunction >> $PROFILE

Set-Location $workingDir
. $PROFILE
Write-Output "mkgitignore is now ready to use. Usage: mkgitignore <TEMPLATE>"
Write-Output "Consider running '. $PROFILE' before usage to ensure function is set up in current shell"