"""
SIMULADOR DE CREACIÓN DE UNA CUENTA POR:
MANUEL ALEJANDRO SANCHEZ SANCHEZ

DISFRUTA!
"""

import time 

def usuario(username):
    user = False #INICIALIZAMOS UN VALOR BOOLEANO PARA RETORNAR TRUE SI EL USUARIO ES VALIDO
    if len(username) >= 6: #VERIFICAMOS QUE NUESTRO USUARIO SEA MAYOR O IGUAL A 6 CARACTERES
        if len(username) <= 12: #VERIFICAMOS QUE NUESTRO USUARIO SEA MENOR O IGUAL A 12 CARACTERES
            if username.isalnum() == True: #VERIFICAMOS QUE NUESTRO USUARIO SOLO TENGA LETRAS Y NUMEROS
                time.sleep(1)    
                print("Usuario valido...")
                user = True #SI SE CUMPLE SE CAMBIA A VERDADERO NUESTRO VALOR DE RETORNO
                time.sleep(2)
            else:
                time.sleep(1)    
                print("El nombre de usuario puede contener solo letras y números...")  
                time.sleep(2) 
                exit()
        else:
            time.sleep(1)    
            print("El nombre de usuario no puede contener más de 12 caracteres...")
            time.sleep(2)
            exit()     
    else:
        time.sleep(1)    
        print("El nombre de usuario debe contener al menos 6 caracteres...")
        time.sleep(3)
        exit() 

    return user #DEVUELVE VALOR QUE NOS INDICARA SI ES VALIDO EL USUARIO    

def contraseña(password):
    contra = False #INICIALIZAMOS UN VALOR BOOLEANO QUE ES EL QUE SERA RETORNADO SI ES VALIDA NUESTRA CONTRASEÑA
    if len(password) <= 8: #VERIFICAMOS QUE LA CONTRASEÑA SEA MENOR A 8 CARACTERES
        if password.isspace() == True:
            time.sleep(1)     
            print("La contraseña no es segura, solo contiene espacios...")
            time.sleep(2)
            exit()
        else:
            if password.isupper() == True: #SI LA CONTRASEÑA SOLO CONTIENE MAYUS
                time.sleep(1)    
                print("La contraseña no es segura...")
                time.sleep(2)
                exit()
            else:
                if password.islower(): #SI LA CONTRASEÑA SOLO CONTIENE MINUSCULAS
                    time.sleep(1)    
                    print("La contraseña no es segura...")
                    time.sleep(2)
                    exit()
                else:   
                    if password.isdigit() == True:  #SI LA CONTRASEÑA SOLO TIENE DIGITOS
                        time.sleep(1)    
                        print("La contraseña no es segura...")
                        time.sleep(2)
                        exit()
                    else:     
                        if password.isalpha() == True: #SI LA CONTRASEÑA SOLO TIENE LETRAS
                            time.sleep(1)    
                            print("La contraseña no es segura...")
                            time.sleep(2)
                            exit()
                        else:
                            if password.isalnum() == True: #SI LA CONTRASEÑA ES ALFANUMERICA PERO SIN CARACTER ESPECIAL
                                time.sleep(1)    
                                print("La contraseña no es segura, necesitas poner al menos un caracter especial...")
                                time.sleep(3)
                                exit()
                            else: # AQUI VERIFICAMOS QUE LA CONTRASEÑA CONTENGA AL MENOS UN CARACTER ESPECIAL
                                verificador = False
                                for i in password:
                                    if i == " ":
                                        time.sleep(1)    
                                        print("La contraseña no es segura...")
                                        time.sleep(3)
                                        exit()
                                    else:
                                        verificador = True 

                                if verificador == True:       
                                    time.sleep(1)    
                                    print("Contraseña segura...")
                                    time.sleep(2)
                                    contra = True   
    else:
        print("La contraseña debe tener maximo 8 caracteres")
        time.sleep(3)
        exit()

    return contra #DEVUELVE UN VALOR TRUE SI LA CONTRASEÑA ES VALIDA


bienvenida = "Bienvenido al simulador de registro de cuenta"
print(bienvenida.center(50, " "))
time.sleep(1)

print("")
print("Espero que te encuentres bien, este es un simulador donde")
print("se hara un registro de una cuenta creado por:")
print("Manuel A. Sanchez Sanchez, espero te guste.")
time.sleep(5)

registro = ""
print(registro.center(100, " "))

print("Para empezar se necesita saber que el usuario consta de mínimo 6")
print("caracteres y máximo 12 caracteres, también que debe ser alfanumerica.")
time.sleep(6)
userName = input("\nIngrese el usuario, porfavor: ")
userFunc = usuario(userName)

print("\nPara la contraseña debe contener al menos letras minúsculas, mayúsculas,")
print("números y al menos 1 carácter no alfanumérico al igual que solamente")
print("consta de 8 caracteres.")
time.sleep(7)
passUser = input("\nIngrese la contraseña, porfavor: ")
passFunc = contraseña(passUser)


print("\nLa cuenta se ha creado con exito con los siguientes datos: ")
time.sleep(1)
print("\nUsuario: ", userName)
time.sleep(1)
print("\nContraseña: ", passUser)
time.sleep(2)

despedida = "\nMuchas gracias por usar este simulador, espero verte en mis otros proyectos. Saludos!"
print(despedida)
time.sleep(3)
    
