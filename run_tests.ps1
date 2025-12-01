# run_tests.ps1

param (
    [string]$TestFile = "tests/test_interface.py"  # arquivo de teste na raiz
)

Write-Host "Diretório atual: $(Get-Location)"
Write-Host "PYTHONPATH atual: $env:PYTHONPATH"

# Caminho para a raiz do projeto
$ROOT = Split-Path -Parent $MyInvocation.MyCommand.Path
$DEV_PATH = Join-Path $ROOT "dev"

# Ativar venv se existir
$VENV_PATH = Join-Path $ROOT "venv\Scripts\Activate.ps1"
if (Test-Path $VENV_PATH) {
    Write-Host "Ativando venv..."
    & $VENV_PATH
} else {
    Write-Host "Aviso: venv não encontrada, continuando sem ambiente virtual."
}

# Verifica se pytest está instalado
$pytestInstalled = python -m pip show pytest
if (-not $pytestInstalled) {
    Write-Host "Instalando pytest..."
    python -m pip install pytest
} else {
    Write-Host "pytest já instalado."
}

# Configura PYTHONPATH para incluir 'dev', onde 'app' está
$env:PYTHONPATH = $DEV_PATH
Write-Host "PYTHONPATH configurado para $DEV_PATH"

# Define KV_ROOT para testes
$KV_ROOT = Join-Path $DEV_PATH "app\interface\kvLang"
$env:KV_ROOT = $KV_ROOT

# Lista arquivos .kv
Write-Host "Arquivos em kvLang:"
Get-ChildItem -Path $KV_ROOT -Filter *.kv | ForEach-Object { $_.FullName }

# Verifica se arquivo de teste existe
$TEST_PATH = Join-Path $ROOT $TestFile
if (Test-Path $TEST_PATH) {
    Write-Host "Rodando pytest em $TestFile ..."
    python -m pytest $TEST_PATH -v
} else {
    Write-Host "Arquivo de teste $TestFile não encontrado."
}
