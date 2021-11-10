#IMPORTS PARA USAR O CMD
import os
import subprocess
import sys

#MENU



print("***************************************")
print("*                                     *")
print("*  Criador de usuários DBFACIL3 v1.1  *")
print("*                        by: crespin  *")
print("*                                     *")
print("***************************************")
print("\n")
print("***************************************")
print("*                                     *")
print("* [1] - CRIAR USUÁRIO                 *")
print("* [2] - DROPAR USUÁRIO                *")
print("* [3] - EXPORTAR BASE                 *")
print("* [4] - IMPORTAR BASE                 *")
print("* [5] - SAIR                          *")
print("*                                     *")
print("***************************************")

menu_select = input(str("DIGITE A OPÇÃO DESEJADA: "))



#CRIADOR DE USUÁRIOS - INICIO --------------------------------------------------------------------------

if menu_select == str(1):
    usercreate = input(str("Nome do usuário: ")).upper()
    print(usercreate+"@dbfacil3\n")
    password = input(str("Senha: ")).upper()
    tbs = usercreate+"_TBS"

    command0 = ("del D:\\USERS\\dist\\USERADMIN\\import.txt")


    command1 = ("echo CREATE BIGFILE TABLESPACE ")+tbs+(" NOLOGGING DATAFILE '/database/dbfacil3/"+tbs+".dbf' SIZE 5 M autoextend on maxsize unlimited;>> import.txt")
    command2 = ("echo create user ")+usercreate+(" identified by ")+password+(" default tablespace ")+tbs+(";>> import.txt")
    command3 = ("echo GRANT DBA TO ")+usercreate+(";>>import.txt")
    command4 = ("echo GRANT CONNECT TO ")+usercreate+(";>> import.txt")
    command5 = ("echo GRANT RESOURCE TO ")+usercreate+(";>> import.txt")
    command6 = ("echo GRANT SELECT_CATALOG_ROLE TO ")+usercreate+(";>> import.txt")
    command7 = ("echo GRANT ALTER SYSTEM TO ")+usercreate+(";>> import.txt")
    command8 = ("echo GRANT CREATE VIEW TO ")+usercreate+(";>> import.txt")
    command9 = ("echo GRANT SELECT ANY DICTIONARY TO ")+usercreate+(";>> import.txt")
    command10 = ("echo GRANT SELECT ANY TABLE TO ")+usercreate+(";>> import.txt")
    command11 = ("echo GRANT DEBUG CONNECT SESSION TO  ")+usercreate+(";>> import.txt")
    command12 = ("echo GRANT CREATE PROCEDURE TO ")+usercreate+(";>> import.txt")
    command13 = ("echo GRANT CREATE ANY INDEX TO ")+usercreate+(";>> import.txt")
    command14 = ("echo ALTER USER ")+usercreate+(" QUOTA UNLIMITED ON ")+tbs+("; >> import.txt")
    command16 = ("SQLPLUS backup/facplan@dbfacil3 @D:\\USERS\\dist\\USERADMIN\\import.txt")

    
    if os.system(command1) == 0:
        print("Executado com sucesso.")
        print(subprocess.getoutput(command1))
    if os.system(command2) == 0:
        print("Executado com sucesso.")
        print(subprocess.getoutput(command2))
    if os.system(command3) == 0:
        print("Executado com sucesso.")
        print(subprocess.getoutput(command3))
    if os.system(command4) == 0:
        print("Executado com sucesso.")
        print(subprocess.getoutput(command4))
    if os.system(command5) == 0:
        print("Executado com sucesso.")
        print(subprocess.getoutput(command5))
    if os.system(command6) == 0:
        print("Executado com sucesso.")
        print(subprocess.getoutput(command6))
    if os.system(command7) == 0:
        print("Executado com sucesso.")
        print(subprocess.getoutput(command7))
    if os.system(command8) == 0:
        print("Executado com sucesso.")
        print(subprocess.getoutput(command8))
    if os.system(command9) == 0:
        print("Executado com sucesso.")
        print(subprocess.getoutput(command9))
    if os.system(command10) == 0:
        print("Executado com sucesso.")
        print(subprocess.getoutput(command10))
    if os.system(command11) == 0:
        print("Executado com sucesso.")
        print(subprocess.getoutput(command11))
    if os.system(command12) == 0:
        print("Executado com sucesso.")
        print(subprocess.getoutput(command12))   
    if os.system(command13) == 0:
        print("Executado com sucesso.")
        print(subprocess.getoutput(command13))
    if os.system(command14) == 0:
        print("Executado com sucesso.")
        print(subprocess.getoutput(command14))
    if os.system(command16) == 0:
        print("Executado com sucesso.")
        print(subprocess.getoutput(command16))
    if os.system(command0) == 0:
        print("Executado com sucesso")
        print("Finalizando programa... TMJ MEUS NOBRE")
        
#CRIADOR DE USUÁRIOS - FIM --------------------------------------------------------------------------    

#DROPADOR DE USUÁRIOS - INICIO ----------------------------------------------------------------------

elif menu_select == str(2):
    
    arqdel = ("del D:\\USERS\\dist\\USERADMIN\\delete.txt")
    
    userdel = input(str("Digite o usuário a ser dropado: ")).upper()
    commanddeluser = ("echo drop user "+userdel+" cascade;>> delete.txt")
    commanddeltbs = ("echo DROP TABLESPACE "+userdel+"_TBS INCLUDING CONTENTS AND DATAFILES;>> delete.txt ")
    commanddelsql = ("SQLPLUS backup/facplan@dbfacil3 @D:\\USERS\\dist\\USERADMIN\\delete.txt")
    
    if os.system(arqdel) == 0:
        print("Executado com sucesso.")
        print(subprocess.getoutput(arqdel))
    if os.system(userdel) == 0:
        print("Executado com sucesso.")
        print(subprocess.getoutput(userdel))
    if os.system(commanddeluser) == 0:
        print("Executado com sucesso.")
        print(subprocess.getoutput(commanddeluser))
    if os.system(commanddelsql) == 0:
        print("Executado com sucesso.")
        print(subprocess.getoutput(commanddelsql))
        print("Finalizando programa... TMJ MEUS NOBRE")
        
#DROPADOR DE USUÁRIOS - FIM ----------------------------------------------------------------------

#EXPORTADOR DE USUÁRIOS - INICIO -----------------------------------------------------------------

elif menu_select == str(3):
    basexp = input(str("Digite o Schema para ser exportada: ")).upper()
    dmpexp = input(str("Digite o Nome do DMP que sera gerado: ")).upper()
    logexp = input(str("Digite o Nome do LOG que sera gerado: ")).upper()

    commandexp = ("expdp backup/facplan@dbfacil3 directory=BACKUP_DIR schemas="+basexp+" dumpfile="+dmpexp+".dmp logfile="+logexp+".log consistent=y statistics=none;")
    if os.system(commandexp) == 0:
        print("Executado com sucesso.")
        print(subprocess.getoutput(commandexp))
        print("Finalizando programa... TMJ MEUS NOBRE")

#IMPORTADOR DE USUÁRIOS - INICIO -----------------------------------------------------------------

elif menu_select == str(4):
    
    baseimp1 = input(str("Digite o Schema base: ")).upper()
    baseimp2 = input(str("Digite o Schema alvo")).upper()
    dmpimp = input(str("Digite o Nome do DMP à ser usado: ")).upper()
    logimp = input(str("Digite o Nome do LOG que sera gerado: ")).upper()
    

    commandimp = ("impdp backup/facplan@dbfacil3 directory=BACKUP_DIR dumpfile="+dmpimp+".DMP logfile="+logimp+".LOG remap_schema="+baseimp1+":"+baseimp2+" remap_tablespace="+baseimp1+"_TBS:"+baseimp2+"_TBS remap_tablespace="+baseimp1+"_IDX:"+baseimp2+"_TBS;")
    if os.system(commandimp) == 0:
        print("Executado com sucesso.")
        print(subprocess.getoutput(commandimp))
        print("Finalizando programa... TMJ MEUS NOBRE")
        
#IMPORTADOR DE USUÁRIOS - FIM -----------------------------------------------------------------        
        
#FINALIZADOR DO PROGRAMA - INICIO -----------------------------------------------------------------

elif menu_select == str(5):
    print("Finalizando programa... TMJ MEUS NOBRE")
    sys.exit()
    
else:
    print("Opção Invalida.")
    
#FINALIZADOR DO PROGRAMA - FIM -----------------------------------------------------------------

    
    



    
    



    
    
    
    
    
    
    
    
    
    