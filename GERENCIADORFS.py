import keyboard
import os
import subprocess
import sys

usuario = input(str("Insira o usuário a ser consultado: ")).upper()

del1=("DEL D:\\TESTE\\dist\\TESTAO\\ATUALIZA.TXT")
del2=("DEL D:\\TESTE\\dist\\TESTAO\\COMMIT.TXT")
del3=("DEL D:\\TESTE\\dist\\TESTAO\\CONSULTA.TXT")

txt = ("echo SELECT ID_RECURSO, NOME, LOGIN_ST, EMAIL, ID_FUNCIONARIO, ROWID FROM SPR_RECURSO S WHERE upper(S.nome) like '%")+usuario+("%';>> CONSULTA.TXT")
comando = ("SQLPLUS fac_star_project/facplan@dbfacil1 @D:\\TESTE\\dist\\TESTAO\\CONSULTA.TXT")
    
os.system(txt)
    
if os.system(comando) == 0:
    print(subprocess.getoutput(comando))
else:
    print ("erro")


print("\n\n\n\n\nDeseja alterar o usuário?:\n \n[1] - SIM\n[2] - NÃO")

menuYES = keyboard.read_key() == "1"
menuNO = keyboard.read_key() == "2"

if (menuYES) == True:
    idrecurso=input(str("ID_Recurs alvo: "))
    user=input(str("NOME e LOGIN (devem ser iguais): "))
    email=input(str("E-mail: "))
    
    atualiza=("echo update SPR_RECURSO S SET NOME='"+user+"', EMAIL='"+email+"', LOGIN_ST='"+user+"' WHERE ID_RECURSO="+idrecurso+";>> ATUALIZA.TXT")
    os.system(atualiza)
    commit=("echo commit;>> COMMIT.TXT")
    os.system(commit)
    atualizasql=("SQLPLUS fac_star_project/facplan@dbfacil1 @D:\\TESTE\\dist\\TESTAO\\ATUALIZA.TXT")
    os.system(atualizasql)
    print(subprocess.getoutput(atualizasql))
    commitsql=("SQLPLUS fac_star_project/facplan@dbfacil1 @D:\\TESTE\\dist\\TESTAO\\COMMIT.TXT")
    os.system(commitsql)
    print(subprocess.getoutput(commitsql))
    os.system(comando)
    print(subprocess.getoutput(comando))
    os.system(del1)    
    os.system(del2)    
    os.system(del3)
    
elif (menuNO) == True:    
    os.system(del3)    
    sys.exit()
     
else:
    print("Opção inválida")
    os.system(del3)
    sys.exit()
    
    
    
    
    



        


