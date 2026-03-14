# Organizador de Contas e Gerador de 2FA
Organizador de Contas e Gerador de 2FA
Este script em Python foi desenvolvido para automatizar e organizar o processo de criação de contas que exigem autenticação de dois fatores (2FA). Ele agiliza o fluxo de trabalho ao formatar os dados automaticamente, gerar o código OTP e copiá-lo diretamente para a área de transferência.

Funcionalidades:
Organização Automática: Salva e-mail, senha e chave 2FA em um arquivo .txt padronizado.


Timestamp: Registra automaticamente a data e o horário em que a conta foi criada.


Geração de OTP: Gera o código de 6 dígitos em tempo real a partir da chave 2FA.


Auto-Copy: Copia o código OTP gerado automaticamente para a área de transferência (Clipboard), eliminando a necessidade de selecionar e copiar manualmente.


Limpeza de Chave: Remove espaços e padroniza a chave 2FA em letras maiúsculas automaticamente.

Como usar:
Pré-requisitos
Python 3 instalado.

(Linux/Manjaro) xclip instalado para suporte à área de transferência:

Bash
sudo pacman -S xclip
Instalação
Clone o repositório:

Bash
git clone https://github.com/thesomeypo/Script-de-organiza-o-e-2FA.git
Crie e ative um ambiente virtual:

Bash
python -m venv venv
source venv/bin/activate
Instale as dependências:

Bash
pip install -r requirements.txt
Execução
Rode o script e siga as instruções no terminal:

Bash
python script.py
Estrutura do Arquivo de Saída
O script gera (ou atualiza) um arquivo chamado contas.txt com a seguinte estrutura:
email,senha:CHAVE2FA criado em DD/MM/AAAA HH:MM:SS