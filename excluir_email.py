import imaplib
import email

imap_servidor = 'imap.gmail.com'
imap_porta = 993
login = 'rafaelzerort@gmail.com'

with open('senha_rafaelzero.txt') as f:
    senha = f.readlines()

senha_do_email = senha[0].strip()

try:
    mail = imaplib.IMAP4_SSL(imap_servidor, imap_porta)
    mail.login(login, senha_do_email)
    print('Conexão realizada com êxito')

    mail.select('inbox')
    print('Entrou no inbox')

    status, messages, = mail.search(None, 'ALL')
    print(f'{status}, Iniciando exclusão!')

    for message_id in messages[0].split():
        # Extrair a mensagem
        status, msg_dados = mail.fetch(message_id, '(RFC822)')

        email_lido = msg_dados[0][1]
        msg = email.message_from_bytes(email_lido)
        remetente = msg['From']

        # Apagar tudo
        mail.store(message_id, '+FLAGS', '\\Deleted')
        print(f'Mensagem de {remetente} excluída.')

    mail.expunge()
    mail.close()
    mail.logout()

except Exception as e:
    print(f'Erro as conectar ao servidor IMAP: {e}')
 