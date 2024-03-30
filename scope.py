#where a variable is visible and accessible on the code
#there are two types: global (variable created outside a function and accessible everywhere on my code) and local scope (the local is generally a variable that is only inside a function and not acessible elsewhere)

global_var = 'Curso Completo de Python'

#to access a global variable from outside a function inside a function, write global vari_name
#with this, you can reassign the value of the global variable everywhere from inside a function.
def write_text():
    global global_var
    global_var = 'Banco de Dados com SQL'
    local_var = 'Fábio dos Reis'
    print(f'Global variable: {global_var}')
    print(f'Local variable: {local_var}')

if __name__ == '__main__':
    print(f'Eexecute the function write_text:')
    write_text()

    print('Trying to access the variables directly')
    print(f'Global variable: {global_var}')
#print(f'Local variable: {local_var}')       this variable is not accessible, therefore returning an error.
#if two variables is created with the same name, one inside a function and another outside a function, what happens is that, the same variable inside the function becomes a local variable; while the outside variable remains as being global. It is like creating a new variable, even though the names are the same.