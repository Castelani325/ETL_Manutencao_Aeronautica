
# ✈️ Pipeline ETL: Monitoramento de Frota e Manutenção Aeronáutica

### 1. Origem dos Dados
Os dados utilizados foram **gerados sinteticamente** via script Python para simular um ambiente real de logística militar (inspirado no contexto da Força Aérea Brasileira).
* **Formato:** Arquivo CSV (`manutencao_aeronaves.csv`).
* **Características:** O dataset propositalmente continha "dados sujos", incluindo:
    * Registros duplicados;
    * Campos nulos (componentes sem identificação);
    * Inconsistências lógicas (horas de voo negativas);
    * Erros de padronização de texto (uso inconsistente de acentos e caixa baixa).

### 2. O que foi feito (O Pipeline)
Implementou-se um ciclo completo de Engenharia de Dados dividido em três estágios:
* **EXTRACT (Extração):** Leitura dos dados brutos do arquivo CSV simulando um sistema legado.
* **TRANSFORM (Transformação):**
    * **Sanitização:** Remoção de duplicatas e registros inválidos (nulos/negativos).
    * **Normalização:** Uso da biblioteca `unicodedata` para remover acentos e converter todo texto para *UPPERCASE*, garantindo padrão logístico.
    * **Enriquecimento:** Criação de novas colunas (`horas_restantes` e `status`) aplicando regras de negócio baseadas no TBO (*Time Between Overhaul*).
* **LOAD (Carga):** Exportação dos dados limpos para CSV (`relatorio_final_frota.csv`) e geração de gráficos para análise gerencial.

### 3. Resultado Obtido
O processo transformou dados brutos e não confiáveis em **informação estratégica**:
* **Classificação Automática:** A frota foi categorizada em status `OPERACIONAL`, `ALERTA` ou `VENCIDO`.
* **Dashboards:** Geração de visualizações gráficas (Pizza e Barras) demonstrando a disponibilidade da frota e a previsão orçamentária por aeronave.
* **Integridade:** O relatório final contém apenas dados padronizados, prontos para importação em sistemas de ERP ou BI.

### 4. Lições Aprendidas
* **Gestão de Dependências:** A importância de fixar versões de bibliotecas (`numpy==1.26.4`, `pandas==2.2.2`) para garantir a reprodutibilidade do código e evitar conflitos (ex: incompatibilidade com Numpy 2.0).
* **Tratamento de Strings:** A simples remoção de acentos evita erros graves de *join* em bancos de dados relacionais futuros.
* **Valor do ETL:** A engenharia de dados não é apenas "limpar linhas", mas sim aplicar regras de negócio que transformam dados em suporte à decisão (manutenção preventiva vs. corretiva).

---
**Aluno:** Otávio Castelani e Francisco Moreira

**Curso:** Engenharia da Computação - FUCAPI
