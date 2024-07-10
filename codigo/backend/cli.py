import requests

art = '''

 █████  ███████  ██████  ██ ███████ 
██   ██ ██      ██       ██ ██      
███████ █████   ██   ███ ██ ███████ 
██   ██ ██      ██    ██ ██      ██ 
██   ██ ███████  ██████  ██ ███████ 
                                    
                                    
 ██████ ██      ██                  
██      ██      ██                  
██      ██      ██                  
██      ██      ██                  
 ██████ ███████ ██                  
                                    
'''

endpoints = {
    "Healthy Check": "http://127.0.0.1:8000",
    "Upload CSV": "http://127.0.0.1:8000/upload-csv",
    "Rodar Ant Colony Optimization": "http://127.0.0.1:8000/run-aco",
    "Pegar Tarefa Ant Colony Optimization": "http://127.0.0.1:8000/results",
}


def main():
    """
    Main function to display the menu and handle user input.
    It continuously prompts the user to choose an endpoint or exit the program.
    """
    while True:
        # Print the ASCII art
        print(art)

        print("\nBem vindo!")  # Welcome message

        # Prompt user to choose an endpoint
        print("\nEscolha um endpoint para rodar:")

        # List the available endpoints
        options = list(endpoints.keys())
        for i, option in enumerate(options, 1):
            print(f"{i}: {option}")
        print("0: Sair")  # Option to exit the program

        # Get user choice
        choice = input(
            "Digite o número do endpoint que você deseja visitar ou 'S' para sair: ")

        # Exit the program if the user chooses 'S'
        if choice.lower() == 's':
            print("Saindo...")
            break

        # Validate the user's choice and perform the corresponding action
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            selected_option = options[int(choice) - 1]
            url = endpoints[selected_option]

            # Handle the 'Upload CSV' endpoint
            if selected_option == "Upload CSV":
                handle_upload_csv(url)
            # Handle the 'Rodar Ant Colony Optimization' endpoint
            elif selected_option == "Rodar Ant Colony Optimization":
                handle_run_aco(url)
            # Handle the 'Pegar Tarefa Ant Colony Optimization' endpoint
            elif selected_option == "Pegar Tarefa Ant Colony Optimization":
                handle_get_aco_task(url)
            # Handle the 'Healthy Check' endpoint
            else:
                response = requests.get(url)
                print_response(response)
        else:
            # Handle invalid choices
            print("Escolha inválida. Por favor, tente novamente.")


def handle_upload_csv(url):
    """
    Handles the 'Upload CSV' endpoint by prompting the user for the file path and uploading the CSV file.

    :param url: URL of the 'Upload CSV' endpoint
    """
    file_path = input("Digite o caminho do arquivo CSV: ")
    try:
        with open(file_path, "rb") as f:
            files = {'file': (file_path, f)}
            response = requests.post(url, files=files)
            print_response(response)
    except FileNotFoundError as e:
        print(f"Arquivo não encontrado: {file_path}")
        print(f"Erro: {str(e)}")


def handle_run_aco(url):
    """
    Handles the 'Rodar Ant Colony Optimization' endpoint by prompting the user for parameters and running the optimization.

    :param url: URL of the 'Rodar Ant Colony Optimization' endpoint
    """
    try:
        num_ants = int(input("Digite o número de formigas: "))
        alpha = float(input("Digite o valor de alpha: "))
        beta = float(input("Digite o valor de beta: "))
        evaporation_rate = float(
            input("Digite o valor da taxa de evaporação: "))
        iterations = int(input("Digite o número de iterações: "))
        params = {
            "num_ants": num_ants,
            "alpha": alpha,
            "beta": beta,
            "evaporation_rate": evaporation_rate,
            "iterations": iterations
        }
        response = requests.post(url, params=params)
        print_response(response)
    except ValueError as e:
        print(f"Entrada inválida: {str(e)}")


def handle_get_aco_task(url):
    """
    Handles the 'Pegar Tarefa Ant Colony Optimization' endpoint by prompting the user for the task ID and fetching the results.

    :param url: URL of the 'Pegar Tarefa Ant Colony Optimization' endpoint
    """
    task_id = input(
        "Digite o ID da tarefa para o endpoint 'Pegar Tarefa Rodar Ant Colony Optimization': ")
    results_url = f"{url}/{task_id}"
    response = requests.get(results_url)
    print_response(response)


def print_response(response):
    """
    Prints the status code and response content of an HTTP response.

    :param response: The HTTP response object
    """
    print(f"\nStatus Code: {response.status_code}")
    print(f"Response Content: {response.content.decode('utf-8')}\n")


# Run the main function
if __name__ == "__main__":
    main()
