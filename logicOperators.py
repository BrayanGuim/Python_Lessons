#Boolean type;
#"and" example
idade = 25
altura = 1.75

resultado = (idade>=18) and (altura>=1.70)
msg = 'Poderá participar do evento?' + str(resultado)

print(msg)
#"or" example; programa de disparo de alarme
porta ='f'
janela='f'

alarme = (porta=='a') or (janela=='a')
msg2 = 'Alarme disparado? ' + str(alarme)

print(msg2)

#"not" operator
tem_dinheiro = False
tem_dinheiro=not tem_dinheiro

msg3 = 'Tem dinheiro? '+str(tem_dinheiro)
print(msg3)