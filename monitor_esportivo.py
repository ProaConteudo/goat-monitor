#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Sistema de Monitoramento Esportivo - Protótipo
Desenvolvido para o Canal GOAT

Este protótipo demonstra as funcionalidades básicas do sistema de monitoramento
de tendências esportivas em redes sociais e outras fontes online.
"""

import os
import json
import random
import datetime
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

class MonitorEsportivo:
    """
    Classe principal do sistema de monitoramento esportivo.
    """
    
    def __init__(self):
        """Inicializa o sistema de monitoramento."""
        self.dados_simulados = {}
        self.clubes = [
            "Corinthians", "Flamengo", "Palmeiras", "São Paulo", "Santos", 
            "Vasco", "Fluminense", "Grêmio", "Internacional", "Cruzeiro",
            "Atlético-MG", "Botafogo", "Bahia", "Sport", "Fortaleza",
            "Ceará", "Athletico-PR", "Coritiba", "Goiás", "Red Bull Bragantino"
        ]
        self.temas = [
            "transferências", "contratações", "lesões", "escalação", 
            "técnico", "tática", "gols", "classificação", "arbitragem",
            "torcida", "estádio", "títulos", "rivalidade", "clássicos",
            "campeonato brasileiro", "libertadores", "copa do brasil",
            "seleção brasileira", "jogadores estrangeiros", "base"
        ]
        self.redes_sociais = ["Instagram", "Twitter/X", "Facebook", "Bluesky"]
        self.sentimentos = ["positivo", "neutro", "negativo"]
        
        # Inicializa dados simulados
        self.gerar_dados_simulados()
    
    def gerar_dados_simulados(self):
        """Gera dados simulados para demonstração do sistema."""
        # Simulação de dados de menções por clube
        mencoes_clubes = {}
        for clube in self.clubes:
            # Corinthians e Flamengo com mais menções, conforme pesquisa
            if clube == "Corinthians":
                mencoes = random.randint(18000, 22000)
            elif clube == "Flamengo":
                mencoes = random.randint(17000, 21000)
            elif clube in ["Palmeiras", "São Paulo", "Santos"]:
                mencoes = random.randint(5000, 9000)
            else:
                mencoes = random.randint(1000, 5000)
            
            mencoes_clubes[clube] = mencoes
        
        self.dados_simulados["mencoes_clubes"] = mencoes_clubes
        
        # Simulação de dados de temas em alta
        temas_alta = {}
        for tema in self.temas:
            temas_alta[tema] = random.randint(100, 10000)
        
        self.dados_simulados["temas_alta"] = temas_alta
        
        # Simulação de dados de sentimento por clube
        sentimento_clubes = {}
        for clube in self.clubes:
            sentimento_clubes[clube] = {
                "positivo": random.randint(20, 70),
                "neutro": random.randint(10, 40),
                "negativo": random.randint(10, 40)
            }
            # Ajuste para garantir que somem 100%
            total = sum(sentimento_clubes[clube].values())
            for sentimento in sentimento_clubes[clube]:
                sentimento_clubes[clube][sentimento] = round(sentimento_clubes[clube][sentimento] / total * 100)
            
            # Correção final para garantir 100%
            diff = 100 - sum(sentimento_clubes[clube].values())
            sentimento_clubes[clube]["neutro"] += diff
        
        self.dados_simulados["sentimento_clubes"] = sentimento_clubes
        
        # Simulação de dados de engajamento por rede social
        engajamento_redes = {}
        for rede in self.redes_sociais:
            engajamento_redes[rede] = random.randint(1000, 10000)
        
        self.dados_simulados["engajamento_redes"] = engajamento_redes
        
        # Simulação de tendências emergentes
        tendencias_emergentes = [
            {
                "tema": "Neymar no Santos",
                "crescimento": random.randint(150, 300),
                "sentimento": "positivo",
                "redes": ["Instagram", "Twitter/X"],
                "relevancia": "alta"
            },
            {
                "tema": "Técnico da Seleção",
                "crescimento": random.randint(100, 200),
                "sentimento": "neutro",
                "redes": ["Twitter/X", "Facebook"],
                "relevancia": "média"
            },
            {
                "tema": "Arbitragem VAR",
                "crescimento": random.randint(80, 150),
                "sentimento": "negativo",
                "redes": ["Twitter/X", "Bluesky"],
                "relevancia": "alta"
            },
            {
                "tema": "Jogador Revelação",
                "crescimento": random.randint(50, 120),
                "sentimento": "positivo",
                "redes": ["Instagram", "Twitter/X"],
                "relevancia": "média"
            },
            {
                "tema": "Futebol Feminino",
                "crescimento": random.randint(70, 130),
                "sentimento": "positivo",
                "redes": ["Instagram", "Facebook"],
                "relevancia": "alta"
            }
        ]
        
        self.dados_simulados["tendencias_emergentes"] = tendencias_emergentes
    
    def obter_clubes_mais_mencionados(self, limite=5):
        """Retorna os clubes mais mencionados."""
        mencoes = self.dados_simulados["mencoes_clubes"]
        clubes_ordenados = sorted(mencoes.items(), key=lambda x: x[1], reverse=True)
        return clubes_ordenados[:limite]
    
    def obter_temas_em_alta(self, limite=5):
        """Retorna os temas em alta."""
        temas = self.dados_simulados["temas_alta"]
        temas_ordenados = sorted(temas.items(), key=lambda x: x[1], reverse=True)
        return temas_ordenados[:limite]
    
    def obter_sentimento_clube(self, clube):
        """Retorna o sentimento associado a um clube específico."""
        return self.dados_simulados["sentimento_clubes"].get(clube, {})
    
    def obter_engajamento_redes(self):
        """Retorna o engajamento por rede social."""
        return self.dados_simulados["engajamento_redes"]
    
    def obter_tendencias_emergentes(self, relevancia=None):
        """Retorna as tendências emergentes."""
        tendencias = self.dados_simulados["tendencias_emergentes"]
        if relevancia:
            return [t for t in tendencias if t["relevancia"] == relevancia]
        return tendencias
    
    def gerar_sugestoes_posts(self, quantidade=3):
        """Gera sugestões de posts com base nas tendências identificadas."""
        tendencias = self.obter_tendencias_emergentes()
        clubes_populares = [c[0] for c in self.obter_clubes_mais_mencionados()]
        
        sugestoes = []
        for _ in range(quantidade):
            tendencia = random.choice(tendencias)
            clube = random.choice(clubes_populares)
            
            # Templates de sugestões
            templates = [
                f"O que você acha sobre {tendencia['tema']}? Os torcedores do {clube} estão comentando muito sobre isso! #CanalGOAT #Futebol",
                f"A tendência do momento é {tendencia['tema']}! Vamos discutir isso na próxima transmissão? #CanalGOAT #AoVivo",
                f"Está acompanhando a repercussão de {tendencia['tema']}? Isso está bombando nas redes sociais! #CanalGOAT #TendênciasEsportivas",
                f"Os fãs do {clube} não param de falar sobre {tendencia['tema']}. Qual sua opinião? #CanalGOAT #Análise",
                f"ALERTA DE TENDÊNCIA: {tendencia['tema']} está em alta nas redes sociais com sentimento {tendencia['sentimento']}! #CanalGOAT"
            ]
            
            sugestao = {
                "texto": random.choice(templates),
                "tema": tendencia["tema"],
                "sentimento": tendencia["sentimento"],
                "redes_recomendadas": tendencia["redes"],
                "horario_recomendado": "Tarde" if random.random() > 0.5 else "Noite",
                "potencial_engajamento": "Alto" if tendencia["relevancia"] == "alta" else "Médio"
            }
            
            sugestoes.append(sugestao)
        
        return sugestoes
    
    def visualizar_clubes_mencionados(self, salvar_caminho=None):
        """Gera visualização dos clubes mais mencionados."""
        mencoes = self.dados_simulados["mencoes_clubes"]
        clubes_ordenados = sorted(mencoes.items(), key=lambda x: x[1], reverse=True)[:10]
        
        clubes = [c[0] for c in clubes_ordenados]
        valores = [c[1] for c in clubes_ordenados]
        
        plt.figure(figsize=(12, 6))
        plt.bar(clubes, valores, color='royalblue')
        plt.title('Top 10 Clubes Mais Mencionados nas Redes Sociais', fontsize=15)
        plt.xlabel('Clubes', fontsize=12)
        plt.ylabel('Número de Menções', fontsize=12)
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        
        if salvar_caminho:
            plt.savefig(salvar_caminho)
            plt.close()
            return salvar_caminho
        else:
            plt.show()
            plt.close()
    
    def visualizar_temas_alta(self, salvar_caminho=None):
        """Gera visualização dos temas em alta."""
        temas = self.dados_simulados["temas_alta"]
        temas_ordenados = sorted(temas.items(), key=lambda x: x[1], reverse=True)[:8]
        
        temas_nomes = [t[0] for t in temas_ordenados]
        valores = [t[1] for t in temas_ordenados]
        
        plt.figure(figsize=(12, 6))
        plt.bar(temas_nomes, valores, color='green')
        plt.title('Temas em Alta no Mundo Esportivo', fontsize=15)
        plt.xlabel('Temas', fontsize=12)
        plt.ylabel('Popularidade (menções)', fontsize=12)
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        
        if salvar_caminho:
            plt.savefig(salvar_caminho)
            plt.close()
            return salvar_caminho
        else:
            plt.show()
            plt.close()
    
    def visualizar_sentimento_clube(self, clube, salvar_caminho=None):
        """Gera visualização do sentimento associado a um clube."""
        sentimento = self.obter_sentimento_clube(clube)
        if not sentimento:
            return None
        
        labels = list(sentimento.keys())
        sizes = list(sentimento.values())
        colors = ['green', 'gray', 'red']
        
        plt.figure(figsize=(8, 8))
        plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
        plt.axis('equal')
        plt.title(f'Sentimento nas Menções ao {clube}', fontsize=15)
        
        if salvar_caminho:
            plt.savefig(salvar_caminho)
            plt.close()
            return salvar_caminho
        else:
            plt.show()
            plt.close()
    
    def visualizar_engajamento_redes(self, salvar_caminho=None):
        """Gera visualização do engajamento por rede social."""
        engajamento = self.obter_engajamento_redes()
        
        redes = list(engajamento.keys())
        valores = list(engajamento.values())
        
        plt.figure(figsize=(10, 6))
        plt.bar(redes, valores, color='purple')
        plt.title('Engajamento por Rede Social', fontsize=15)
        plt.xlabel('Rede Social', fontsize=12)
        plt.ylabel('Nível de Engajamento', fontsize=12)
        plt.tight_layout()
        
        if salvar_caminho:
            plt.savefig(salvar_caminho)
            plt.close()
            return salvar_caminho
        else:
            plt.show()
            plt.close()
    
    def gerar_relatorio(self, caminho_saida):
        """Gera um relatório completo com as análises."""
        hoje = datetime.datetime.now().strftime("%d/%m/%Y")
        
        with open(caminho_saida, 'w', encoding='utf-8') as f:
            f.write(f"# Relatório de Tendências Esportivas - {hoje}\n\n")
            
            f.write("## Clubes Mais Mencionados\n\n")
            clubes = self.obter_clubes_mais_mencionados(10)
            for i, (clube, mencoes) in enumerate(clubes, 1):
                f.write(f"{i}. {clube}: {mencoes} menções\n")
            
            f.write("\n## Temas em Alta\n\n")
            temas = self.obter_temas_em_alta(8)
            for i, (tema, valor) in enumerate(temas, 1):
                f.write(f"{i}. {tema}: {valor} pontos\n")
            
            f.write("\n## Tendências Emergentes\n\n")
            tendencias = self.obter_tendencias_emergentes()
            for i, tendencia in enumerate(tendencias, 1):
                f.write(f"{i}. **{tendencia['tema']}**\n")
                f.write(f"   - Crescimento: {tendencia['crescimento']}%\n")
                f.write(f"   - Sentimento predominante: {tendencia['sentimento']}\n")
                f.write(f"   - Redes sociais principais: {', '.join(tendencia['redes'])}\n")
                f.write(f"   - Relevância: {tendencia['relevancia']}\n\n")
            
            f.write("\n## Sugestões de Posts\n\n")
            sugestoes = self.gerar_sugestoes_posts(5)
            for i, sugestao in enumerate(sugestoes, 1):
                f.write(f"### Sugestão {i}\n\n")
                f.write(f"**Texto sugerido:**\n{sugestao['texto']}\n\n")
                f.write(f"**Tema:** {sugestao['tema']}\n")
                f.write(f"**Sentimento:** {sugestao['sentimento']}\n")
                f.write(f"**Redes recomendadas:** {', '.join(sugestao['redes_recomendadas'])}\n")
                f.write(f"**Horário recomendado:** {sugestao['horario_recomendado']}\n")
                f.write(f"**Potencial de engajamento:** {sugestao['potencial_engajamento']}\n\n")
            
            f.write("\n## Conclusão\n\n")
            f.write("Este relatório apresenta uma visão geral das tendências esportivas atuais, ")
            f.write("com foco especial em futebol. As sugestões de posts foram geradas com base ")
            f.write("nas tendências identificadas e visam maximizar o engajamento nas redes sociais ")
            f.write("do Canal GOAT.\n\n")
            f.write("Relatório gerado automaticamente pelo Sistema de Monitoramento Esportivo.")
        
        return caminho_saida

def main():
    """Função principal para demonstração do sistema."""
    # Cria diretório para gráficos se não existir
    graficos_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "graficos")
    os.makedirs(graficos_dir, exist_ok=True)
    
    # Inicializa o sistema
    monitor = MonitorEsportivo()
    
    # Gera visualizações
    monitor.visualizar_clubes_mencionados(os.path.join(graficos_dir, "clubes_mencionados.png"))
    monitor.visualizar_temas_alta(os.path.join(graficos_dir, "temas_alta.png"))
    monitor.visualizar_sentimento_clube("Corinthians", os.path.join(graficos_dir, "sentimento_corinthians.png"))
    monitor.visualizar_sentimento_clube("Flamengo", os.path.join(graficos_dir, "sentimento_flamengo.png"))
    monitor.visualizar_engajamento_redes(os.path.join(graficos_dir, "engajamento_redes.png"))
    
    # Gera relatório
    relatorio_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "relatorio_tendencias.md")
    monitor.gerar_relatorio(relatorio_path)
    
    print(f"Sistema de Monitoramento Esportivo - Demonstração")
    print(f"Relatório gerado em: {relatorio_path}")
    print(f"Gráficos gerados em: {graficos_dir}")
    
    # Exibe algumas sugestões de posts
    print("\nSugestões de Posts:")
    sugestoes = monitor.gerar_sugestoes_posts(3)
    for i, sugestao in enumerate(sugestoes, 1):
        print(f"\n{i}. {sugestao['texto']}")
        print(f"   Redes recomendadas: {', '.join(sugestao['redes_recomendadas'])}")
        print(f"   Potencial de engajamento: {sugestao['potencial_engajamento']}")

if __name__ == "__main__":
    main()
