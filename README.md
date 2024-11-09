# File Search

## Descrição
O **File Search** é um script simples, mas poderoso, para encontrar arquivos no seu sistema com base em três critérios: **extensão**, **nome** ou **tamanho**. Ele pesquisa todo o sistema (ou o diretório especificado) e gera um relatório com informações detalhadas sobre os arquivos encontrados.

Você pode escolher entre procurar por:
- Extensão de arquivo (exemplo: `.txt`, `.jpg`, etc.)
- Nome do arquivo
- Tamanho do arquivo (especificando um valor mínimo e máximo em bytes)

Além disso, o script também calcula algumas métricas úteis, como:
- Total de arquivos encontrados
- Tamanho total dos arquivos
- Tamanho médio dos arquivos
- O maior e o menor arquivo encontrado
- O diretório com mais arquivos

Ao final, ele gera um relatório e pode salvar tudo em um arquivo de texto para você.

## Funcionalidades
- Escolher entre pesquisar por **extensão**, **nome** ou **tamanho** do arquivo
- Exibir informações detalhadas sobre os arquivos encontrados
- Mostrar as estatísticas gerais (total de arquivos, tamanho médio, maior e menor arquivo, etc.)
- Salvar o relatório em um arquivo de texto

## Como Usar

1. **Escolher o critério de pesquisa**: O script oferece três opções para você escolher:
   - Pesquisar por extensão de arquivo
   - Pesquisar por nome de arquivo
   - Pesquisar por tamanho de arquivo (em bytes)
   
2. **Fornecer os parâmetros de pesquisa**: Dependendo da opção escolhida, o script pedirá os detalhes necessários:
   - Para extensão, digite a extensão (ex: `.txt`, `.pdf`, etc.)
   - Para nome, digite o nome completo do arquivo (ou parte dele)
   - Para tamanho, forneça o valor mínimo e máximo em bytes
   
3. **Salvar o Relatório**: Após realizar a busca, o script perguntará se você deseja salvar as informações encontradas em um arquivo de texto. Se você optar por sim, um arquivo chamado `relatorio.txt` será gerado.
