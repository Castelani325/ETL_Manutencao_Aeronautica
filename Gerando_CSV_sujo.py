import pandas as pd

# 1. Dicionário com os dados
dados_aeronauticos = {
    'matricula_aeronave': ['FAB-2850', 'FAB-2401', 'FAB-2850', 'FAB-5500', 'FAB-2401', 'FAB-9999', 'CIV-PT-X'],
    'componente': ['Motor PT6', 'Radar Meteorológico', 'Motor PT6', 'Trem de Pouso', 'Altímetro', None, 'Hélice'],
    'horas_voo_atuais': [1800.5, 200.0, 1800.5, 4200.0, -50.0, 10.0, 500.0],
    'tbo_horas_limite': [2000, 5000, 2000, 4000, 1000, 100, 2000],
    'custo_manutencao_previsto': [15000.00, 2500.00, 15000.00, 45000.00, 300.00, 0.0, 1200.00],
    'data_ultima_inspecao': ['2024-01-10', '2023-11-22', '2024-01-10', None, '2024-02-15', '2024-01-01', '2023-05-20']
}

# 2. Cria o DataFrame DIRETAMENTE do dicionário (Correção aqui)
df = pd.DataFrame(dados_aeronauticos)

# 3. Salva o CSV
df.to_csv('manutencao_aeronaves.csv', index=False)

print("Arquivo 'manutencao_aeronaves.csv' gerado com sucesso.")