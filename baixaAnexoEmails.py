########################## IMPORTAÇÃO DAS BIBLIOTECAS UTILIZADAS##########################
# IMAPLIB É A BIBLIOTECA QUE PERMITE A CONEXÃO E A LEITURA DOS EMAILS NA CAIXA
import imaplib
# EMAIL É A BIBLIOTECA QUE PERMITE TRANSFORMAR O CODIGO utf-8 EM STRING, PODENDO SER GRAVADA EM UM ARQUIVO
import email





########################## CREDENCIAIS ##########################
# SRV = SERVIDOR IMAPR
SRV = "imap.servidor.com"
# USER = EMAIL PARA LOGAR
USER = "email@aqui.com"
# PASS = SENHA DO EMAIL
PASS = "senhaAqui"





########################## LOGON COM AS CREDENCIAIS NO SERVIDOR ##########################
# IMAPLIB.IMAP4_SSL(SRV) É O PADRÃO DE SEGURANÇA PARA LOGAR NO SERVIDOR (SRV) BUSCA A VARIAVEL NA CREDENCIAL
mail = imaplib.IMAP4_SSL(SRV)
# MAIL.LOGIN BUSCA AS CREDENCIAIS DE EMAIL E SENHA E INSERE NO SERVIDOR
mail.login(USER, PASS)





########################## SETA OS PARAMETROS DE BUSCA NO EMAIL ##########################
# MAIL.LIST AVISA AO CODIGO PARA LISTAR OS EMAILS CONFORME OS FILTROS ABAIXO
(mail.list())
# MAIL.SELECT APLICA OS FILTROS ONDE BUSCAR OS EMAILS (READONLY=FALSE MARCA OS EMAILS COMO LIDOS) (READONLY=TRUE NÃO MARCA OS EMAILS COMO LIDOS)                      
(mail.select(mailbox="MARCADOR OU DIRETORIO AQUI",readonly=False))
# RESPOSTAS, IDDOSEMAILS SEPARA OS EMAILS POR ID E LISTA AS RESPOSTAS ENVIADAS
respostas,IdDosEmails = mail.search(None,"All")





########################## SALVAR OS ANEXOS ##########################
# ESCREVE O EMAIL EM RFC822 (LINGUAGEM DE EMAIL) DE FORMA QUE O PROGRAMA CONSEGUE LER TODA MENSAGEM E ANEXOS
for i in IdDosEmails[0].split():
    resultado,dados = mail.fetch(i, "(RFC822)")
    textoDoEmail = dados[0][1]
# TRADUZ PARA UTF-8 (LINGUAGEM BINARIA) DE FORMA A PODER SER ESCRITO NO COMPUTADOR
    textoDoEmail = textoDoEmail.decode("utf-8")
# VARIAVEL QUE TRANSFORMA EM STRING    
    textoDoEmail = email.message_from_string(textoDoEmail)
# FOR PART IN TEXTODOEMAIL.WALK NAVEGA POR TODOS OS EMAILS PROCURANDO O PARAMETRO "MULTIPART" QUE É EQUIVALENTE A ANEXO.
    for part in textoDoEmail.walk():
# SE ELE ENCONTRAR UM ANEXO, ELE SAI DA CONDIÇÃO E SEGUE O ALGORITMO 
        if part.get_content_maintype() == "multipart":
            continue
# SE ELE NÃO ENCONTRAR UM ANEXO, ELE SEGUE PARA O PROXIMO EMAIL
        if part.get("Content-Disposition") is None:
            continue
# PUXA O NOME DO ARQUIVO ANEXADO
        filename = part.get_filename()
        print(filename)
# CRIA UM NOVO ARQUIVO COPIANDO O NOME DO ANEXO
        arquivo = open(filename, "wb")
# ESCREVE NO ARQUIVO AS INFORMAÇÕES COLETADAS E DECODIFICA PARA LINGUAGEM "HUMANA"
        arquivo.write(part.get_payload(decode=True))
# FECHA O ARQUIVO PARA QUE ELE POSSA SER UTILIZADO
        arquivo.close
        




################################ OBSERVAÇÕES ################################
# - OS ANEXOS SERÃO ESCRITOS NA PASTA ONDE O EXECUTAVEL ESTIVER SALVO
# - NÃO RODAR O PROGRAMA SEM FILTROS
# - NÃO RODAR O PROGRAMA EM UMA PASTA OU MARCADOR COM MUITOS EMAILS
# - NA LINHA 36, O PARAMETRÔ READONLY DEVE SER MANTIDO COMO FALSE,
# - SE ESTIVER TRUE ELE IRA BAIXAR TODOS OS EMAILS DA PASTA/MARCADOR MESMO JÁ TENDO SIDO BAIXADO.
  ################################ OBSERVAÇÕES ################################      
        
            
        
    
    