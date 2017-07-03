from database import BancoDeDados

if __name__ == "__main__":

    banco = BancoDeDados()
    banco.conecta()
    banco.criar_tabelas()

    banco.inserir_cliente('Wellington Viana', '00011122233', "well@well.com.br")
    banco.inserir_cliente('Ana Maria', '11122233344', 'ana@ana.com.br')

    banco.buscar_cliente('00011122233')
    banco.buscar_email('well@well.com.br')

    banco.remover_cliente('00011122233')

    #banco.buscar_cliente('00011122233')

    banco.desconecta()