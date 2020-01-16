
# coding: utf-8

# In[29]:


#Calculoradora basica funções()

#soma
def funcSoma(var1, var2):
    somar = var1 + var2 
    return somar

#subtração
def funcSub(var1, var2):
    sub = var1 - var2
    return sub

#multiplicação
def funcMult(var1, var2):
    mult = var1*var2 
    return mult

#Divisão
def funcDiv(var1, var2):
    div = var1/var2
    return div

# Funcao de conversao int e float
def funcConvertor(registradorOperacao):  
    if type(registradorOperacao) == int:
        registradorOperacao = int(registradorOperacao)
        #Conversao para inteiro
        return (registradorOperacao)
    else:
        registradorOperacao = float(registradorOperacao)
        return (registradorOperacao)


# In[73]:


#Entrada de operações
print("##################################################### Calculadora #############################################################")
print("Lista de Operações: \n 1 - Soma \n 2 - Subtração \n 3 - Multiplicação \n 4 - Divisão")
print('\nDigite "Novo" para novo calculo \nDigite "Fim" para encerar a calculadora')
print("###############################################################################################################################")


# In[17]:


#Entrada dos dados
registradorOperacao = input("\nDigite uma das quatro operações:  ")


# In[18]:


# chamada ao convertor para int e float
registradorOperacao = funcConvertor(registradorOperacao)


# In[19]:


############################# Validação de entrada da calculadora ###############################


# In[20]:


# Verificação de possibilidade (entrada de dados)
if ((registradorOperacao <= 4) and (registradorOperacao >= 1)):
    verificador = True
    #Se verdadeiro não fazer nada
else:
    verificador = False
    #Se falso entrar na condição para reescrever


# In[25]:


while (verificador == False):
    if ((registradorOperacao <= 4) and (registradorOperacao >= 1)):
        print("Comando valido! Por favor continue!")
        verificador = True
        break
    else:
        print("Comando invalido! Tente novamente.")
        registradorOperacao = (input("\nDigite uma das quatro operações:  "))
        registradorOperacao = funcConvertor(registradorOperacao)
        verificador = False


# In[57]:


#chamada a soma
if (registradorOperacao == 1):
    valor = 0
    soma1Input = (input("\nDigite o Primeiro valor:  "))
    soma1Convertido = funcConvertor(soma1Input)
    soma2Input = (input("\nDigite o Segundo valor:   "))
    soma2Convertido = funcConvertor(soma2Input)
    valor = funcSoma(soma1Convertido,soma2Convertido)
    print(valor)
#chamada subtração
elif (registradorOperacao == 2):
    valor = 0
    sub1Input = (input("\nDigite o Primeiro valor:  "))
    sub1Convertido = funcConvertor(sub1Input)
    sub2Input = (input("\nDigite o Segundo valor:   "))
    sub2Convertido = funcConvertor(sub2Input)
    valor = funcSub(sub1Convertido,sub2Convertido)
    print(valor)
#multiplicação    
elif (registradorOperacao == 3):
    valor = 0
    mult1Input = (input("\nDigite o Primeiro valor:  "))
    mult1Convertido = funcConvertor(mult1Input)
    mult2Input = (input("\nDigite o Segundo valor:   "))
    mult2Convertido = funcConvertor(mult2Input)
    valor = funcMult(mult1Convertido,mult2Convertido)
    print(valor)
#Divisão    
elif (registradorOperacao == 4):
    valor = 0
    div1Input = (input("\nDigite o Primeiro valor:  "))
    div1Convertido = funcConvertor(div1Input)
    div2Input = (input("\nDigite o Segundo valor:   "))
    div2Convertido = funcConvertor(div2Input)
    valor = funcDiv(div1Convertido,div2Convertido)
    print(valor)

