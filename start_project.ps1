# start_project.ps1

# Caminho relativo para a raiz do projeto
$ProjectRoot = Split-Path -Parent $MyInvocation.MyCommand.Definition
Set-Location $ProjectRoot

Write-Host "Iniciando ColabTask na raiz do projeto: $ProjectRoot"

# Cria venv se não existir
if (-Not (Test-Path ".\venv")) {
    Write-Host "Criando ambiente virtual..."
    python -m venv venv
}

# Ativa o venv
$activate = "$ProjectRoot\venv\Scripts\Activate.ps1"
Write-Host "Ativando ambiente virtual..."
. $activate

# Atualiza pip, setuptools e wheel
Write-Host "Atualizando pip, setuptools e wheel..."
python -m pip install --upgrade pip setuptools wheel

# Instala dependências do projeto
Write-Host "Instalando dependências do Kivy..."
python -m pip install kivy[base] kivy_deps.sdl2 kivy_deps.glew kivy_deps.angle Kivy-Garden

# Executa o app
Write-Host "Rodando a interface..."
python -m dev.main
