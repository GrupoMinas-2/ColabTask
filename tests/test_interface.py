import pytest
import os
from unittest.mock import MagicMock, patch
from kivy.uix.boxlayout import BoxLayout
from pathlib import Path
from kivy.lang import Builder


# MOCK GLOBAL PARA Builder.load_file (Isso impede que qualquer load_file tente abrir arquivos .kv reais)
patcher = patch.object(Builder, "load_file", return_value=None)
patcher.start()


# CONFIGURAÇÃO DO KV_ROOT PARA TESTES (opcional)
KV_ROOT = Path(os.environ.get("KV_ROOT", ""))

# IMPORTA MÓDULOS DA APLICAÇÃO
from dev.app.interface.widgets.nucleo_iten import Nucleo
from dev.app.interface.screens.home_screen import HomePage

# DEBUG: imprime diretório e arquivos 
print("Diretório atual:", os.getcwd())
kv_dir = Path(os.getcwd()) / "dev" / "app" / "interface" / "kvLang"
if kv_dir.exists():
    print("Arquivos em kvLang:", [f.name for f in kv_dir.iterdir() if f.suffix == ".kv"])
else:
    print("Diretório kvLang não encontrado")

# 
# TESTE 1 - Criação de Nucleo sem acessar o banco
# 
def test_nucleo_valores_padrao():
    with patch("dev.app.interface.widgets.nucleo_iten.Nucleo.use_case", create=True) as mock_use_case:
        # Cria mocks para o serviço e repositório
        mock_service = MagicMock()
        mock_repository = MagicMock()
        mock_service.repository = mock_repository
        mock_use_case.service = mock_service

        # Instancia Nucleo (não acessa o DB real)
        n = Nucleo.__new__(Nucleo)
        n.use_case = mock_use_case
        n.titulo = "nome núcleo"
        n.descricao = "descrição"

        # Simula chamada do use_case
        n.use_case.service.repository.insert_nucleo(n)
        mock_repository.insert_nucleo.assert_called_once_with(n)

# TESTE 2 - Mock da HomePage e container
def test_homepage_mock_widgets():
    home = HomePage()

    # Mock do container de widgets
    class FakeContainer(BoxLayout):
        def __init__(self):
            super().__init__()
            self.adicionados = []

        def add_widget(self, widget):
            self.adicionados.append(widget)

    # Mock dos ids
    home.ids = {"containerNucleos": FakeContainer()}

    # Adiciona um núcleo mock
    class FakeNucleo:
        pass

    home.ids["containerNucleos"].add_widget(FakeNucleo())
    assert len(home.ids["containerNucleos"].adicionados) == 1
