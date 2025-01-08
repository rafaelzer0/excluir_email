# Script de Exclusão de E-mails no Gmail via IMAP
Este repositório contém um script Python para conectar-se ao servidor IMAP do Gmail e excluir todos os e-mails na caixa de entrada de uma conta.

## Como Funciona
O script usa a biblioteca imaplib para se conectar ao servidor IMAP do Gmail, autenticar-se com as credenciais do usuário e, em seguida, excluir todas as mensagens da caixa de entrada (INBOX).

## Fluxo do Script
O script faz a autenticação no servidor IMAP do Gmail usando o login e senha fornecidos.
Ele conecta-se à caixa de entrada (inbox).
Busca todas as mensagens existentes.
Para cada mensagem encontrada, marca ela como excluída.
Após excluir todas as mensagens, o script expurga (remove permanentemente) as mensagens da conta de e-mail.
## Requisitos
Python 3.x
Bibliotecas Python:
imaplib
email

Se necessário, instale as dependências com:
pip install imaplib email

## Configuração do Gmail
Para que o script funcione com sua conta do Gmail, você deve:

Ativar o acesso IMAP no seu Gmail (Configurações > Encaminhamento e POP/IMAP).
Permitir apps menos seguros no seu Google Account (caso não esteja usando 2FA) ou gerar uma senha de app (caso use a autenticação de dois fatores).

## Segurança
Senha de e-mail: Este script requer o uso de senha para autenticação. Caso sua conta tenha a autenticação de dois fatores (2FA) ativada, você precisará gerar uma senha de aplicativo no Google.
Backup: Recomenda-se fazer backup dos seus e-mails antes de rodar o script, já que a exclusão é permanente.
