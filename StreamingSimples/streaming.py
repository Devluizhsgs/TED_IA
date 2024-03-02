class SistemaStreaming:
    def __init__(self):
        self.catalogo_filmes = ["Messias o Instrutor de leigos", "Exterminador do futuro 10: O Messias", "Os poderes de um professor"]
        self.catalogo_series = ["Ensinamentos avançados para alunos desinformados", "A Origem Do Exterminador", "Ensino de classes"]

    def exibir_catalogo(self):
        print("\nCatálogo de Filmes:")
        for filme in self.catalogo_filmes:
            print(filme)
        print("\nCatálogo de Séries:")
        for serie in self.catalogo_series:
            print(serie)

    def iniciar_streaming(self):
        print("\nBem-vindo ao Sistema Simplificado de Streaming de Vídeo Para Apresentação Simples!")
        while True:
            print("\nOpções:")
            print("1. Visualizar catálogo de filmes e séries")
            print("2. Sair do sistema")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.exibir_catalogo() 
            elif opcao == "2":
                print("Obrigado por usar nosso sistema de streaming. Até logo!")
                break
            else:
                print("Opção inválida. Por favor, escolha uma opção válida.")


# Função principal para iniciar o sistema
def main():
    sistema = SistemaStreaming()
    sistema.iniciar_streaming()


if __name__ == "__main__":
    main()
