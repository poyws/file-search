import os
from datetime import datetime
import platform
from collections import defaultdict

d = "/" if platform.system() == "Linux" else os.getenv("SystemDrive", "C:") + "\\"

print("[+] Escolha o critério de pesquisa:")
print("[1] Pesquisar por extensão de arquivo")
print("[2] Pesquisar por nome de arquivo")
print("[3] Pesquisar por tamanho de arquivo em bytes")

criterio = input("[+] Digite o número da opção desejada (1, 2 ou 3): ").strip()

if criterio == '1':
    ext = input("[+] Digite a extensão do arquivo (ex: .txt): ")
    nome_arquivo = None
    tamanho_min = tamanho_max = None
elif criterio == '2':
    nome_arquivo = input("[+] Digite o nome do arquivo (ex: documento.txt): ")
    ext = None
    tamanho_min = tamanho_max = None
elif criterio == '3':
    tamanho_min = int(input("[+] Digite o tamanho mínimo em bytes: "))
    tamanho_max = int(input("[+] Digite o tamanho máximo em bytes: "))
    ext = nome_arquivo = None
else:
    print("[-] Opção inválida. O programa será encerrado.")
    exit()

salvar = input("[+] Deseja salvar o relatório em um arquivo de texto? (s/n): ").lower() == 's'

tamanho_total = 0
contagem = 0
maior_arquivo = ("", 0)
menor_arquivo = ("", float('inf'))
tempo_modificacao_total = 0
relatorio = []
arquivos_por_diretorio = defaultdict(int)

print("[+] Iniciando a busca nos diretórios...")
for r, _, f in os.walk(d):
    for arq in f:
        if (ext and arq.endswith(ext)) or (nome_arquivo and nome_arquivo in arq):
            caminho = os.path.join(r, arq)
            try:
                tamanho = os.path.getsize(caminho)
                if tamanho_min is not None and tamanho < tamanho_min:
                    continue
                if tamanho_max is not None and tamanho > tamanho_max:
                    continue

                mod_time = os.path.getmtime(caminho)
                mod = datetime.fromtimestamp(mod_time).strftime('%Y-%m-%d %H:%M:%S')

                tamanho_total += tamanho
                contagem += 1
                tempo_modificacao_total += mod_time
                arquivos_por_diretorio[r] += 1

                if tamanho > maior_arquivo[1]:
                    maior_arquivo = (caminho, tamanho)
                if tamanho < menor_arquivo[1]:
                    menor_arquivo = (caminho, tamanho)

                linha = f"Arquivo: {caminho} | Tamanho: {tamanho} bytes | Última modificação: {mod}"
                relatorio.append(linha)
                print(f"[+] Encontrado: {linha}")
            except (PermissionError, FileNotFoundError):
                continue

if contagem > 0:
    tamanho_medio = tamanho_total // contagem
    tempo_modificacao_medio = tempo_modificacao_total / contagem

    if arquivos_por_diretorio:
        diretorio_mais_arquivos = max(arquivos_por_diretorio.items(), key=lambda x: x[1], default=("Nenhum diretório", 0))[0]
    else:
        diretorio_mais_arquivos = "Nenhum diretório com arquivos encontrados"

    print("[+] Resultados encontrados:")
    print(f"\n[+] Total de arquivos: {contagem}")
    print(f"[+] Tamanho total: {tamanho_total} bytes")
    print(f"[+] Tamanho médio: {tamanho_medio} bytes")
    print(f"[+] Maior arquivo: {maior_arquivo[0]} ({maior_arquivo[1]} bytes)")
    print(f"[+] Menor arquivo: {menor_arquivo[0]} ({menor_arquivo[1]} bytes)")
    print(f"[+] Diretório com mais arquivos: {diretorio_mais_arquivos}")
    print(f"[+] Tempo total de modificação: {tempo_modificacao_total:.2f} segundos")
    print(f"[+] Tempo médio de modificação: {tempo_modificacao_medio:.2f} segundos")
else:
    print("[-] Nenhum arquivo encontrado com os critérios especificados.")
    tamanho_medio = tempo_modificacao_medio = diretorio_mais_arquivos = None

if salvar and contagem > 0:
    with open("relatorio.txt", "w") as f:
        f.write("\n".join(relatorio))
        f.write(f"\n\nTotal de arquivos: {contagem}")
        f.write(f"\nTamanho total: {tamanho_total} bytes")
        if contagem > 0:
            f.write(f"\nTamanho médio: {tamanho_medio} bytes")
        f.write(f"\nMaior arquivo: {maior_arquivo[0]} ({maior_arquivo[1]} bytes)")
        f.write(f"\nMenor arquivo: {menor_arquivo[0]} ({menor_arquivo[1]} bytes)")
        f.write(f"\nDiretório com mais arquivos: {diretorio_mais_arquivos}")
        f.write(f"\nTempo total de modificação: {tempo_modificacao_total:.2f} segundos")
        f.write(f"\nTempo médio de modificação: {tempo_modificacao_medio:.2f} segundos")
    print("[+] Relatório salvo em 'relatorio.txt'.")
