# 🌱 Vegan News Curator

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Azure](https://img.shields.io/badge/Azure-Cloud%20Platform-0078D4.svg?logo=microsoft-azure&logoColor=white)](https://azure.microsoft.com)
[![Azure AI Foundry](https://img.shields.io/badge/Azure%20AI%20Foundry-AI%20Services-0078D4.svg?logo=microsoft-azure&logoColor=white)](https://ai.azure.com)
![Plant-Based](https://img.shields.io/badge/Plant--Based-100%25-green)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)](https://github.com/yourusername/vegan-news-curator)

**Uma plataforma inteligente de curadoria de notícias sobre veganismo, vegetarianismo e sustentabilidade alimentar, potenciada por IA do Azure AI Foundry.**

## 📋 Visão Geral

O **Vegan News Curator** é uma plataforma inteligente de curadoria de notícias sobre veganismo, vegetarianismo e sustentabilidade alimentar, potenciada por **IA do Azure AI Foundry**.
A aplicação utiliza um **agente GPT integrado no AI Foundry** para processar e analisar o conteúdo de múltiplas fontes globais, gerando uma **newsletter profissional em design de jornal**, distribuída automaticamente por email.

### ✨ Características Principais

- 🤖 **IA Especializada**: Agente Azure AI que filtra e cuida notícias com credibilidade
- 🌍 **Coleta Global**: Integração com GNews API para notícias mundiais
- 📰 **Design Profissional**: Template HTML responsivo estilo jornal clássico
- 🏷️ **Categorização Automática**: Organização em 5 categorias especializadas
- ✉️ **Distribuição por Email**: Envio automatizado via SMTP
- 🔄 **Processamento Assíncrono**: Arquitetura async para melhor performance

---

### 📧 Visualização do Email Gerado

Confira como ficou o email curado pelo **Agent AI Vegan News**:

[📄 Abrir PDF do Email](docs/images/email_vegan_news.pdf)

---

### 🎬 Vídeo de Demonstração

Assista à execução do **Agent AI Vegan News** em ação:

[![Play](https://img.shields.io/badge/Play_Video-000?style=for-the-badge)](https://vegan-news-curator.my.canva.site/)

---

### 📄 Capturas de Tela do Projeto

Confira o passo a passo do projeto com prints:

[Visualizar PDF com capturas de tela](docs/capturas_de_tela.pdf)

---

### 🌱 Por que criar o Vegan News?
Com o aumento do interesse em veganismo e alimentação sustentável, acompanhar notícias confiáveis de diferentes fontes tornou-se um desafio. O **Vegan News Curator** surge para centralizar e filtrar conteúdos relevantes, trazendo apenas informações verificadas sobre saúde, mercado, sustentabilidade e inovação plant-based.

---

### 💡 Objetivo da plataforma
A ideia é oferecer uma **newsletter semanal de alta qualidade**, utilizando inteligência artificial para traduzir, organizar e formatar notícias de forma clara e profissional. Assim, leitores recebem insights confiáveis e atualizados, economizando tempo e promovendo escolhas mais conscientes.

---

## 🚀 Início Rápido

### Pré-requisitos

- Python 3.11 ou superior
- UV instalado (gerenciador ultrarrápido de pacotes Python)
- Azure CLI instalado e autenticado (az login)
- Conta Azure com acesso ao Azure AI Foundry
- Chave de API do GNews (ou outra API de notícias compatível)
- Conta de e-mail SMTP ativa (Gmail, Outlook, SendGrid, etc.)

### Instalação

#### 1. Clone o repositório

```bash
git clone https://github.com/mariana-reis/vegan-news-curator
cd vegan-news-curator
```

#### 2. Instale as dependências

```bash
uv install

```

#### 3. Configure as variáveis de ambiente

```bash
cp .env.example .env
```

Edite o arquivo `.env.exemple` com suas credenciais:

```dotenv
# Azure AI
AZURE_AI_PROJECT_ENDPOINT=https://seu-projeto.azure.com/
AZURE_AI_MODEL_DEPLOYMENT_NAME=seu-modelo-deployment
AGENT_ID=seu-agent-id

# API NEWS
GNEWS_API_KEY=sua-chave-gnews

# Email (SMTP)
EMAIL_SENDER=seu_email@gmail.com
EMAIL_PASSWORD=sua_senha_app
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587

# Destinatário
RECIPIENT_EMAIL=destinatario@example.com
```

#### 4. Execute a aplicação

```bash
uv run main.py
```

---

## 📚 Guia de Configuração Detalhado

### Azure AI Foundry Setup

---

### **Passo 1: Criar Resource Group**

Antes de criar qualquer serviço, é necessário um Resource Group.

1. Acesse o [Azure Portal](https://portal.azure.com)
2. No menu superior, clique em **Create a resource**
3. Pesquise por **Resource Group**
4. Clique em **Create**
5. Preencha:

   * **Resource Group Name**: `rg-vegan-news` (sugestão)
   * **Region**: `East US` (recomendado)
6. Clique em **Review + Create** → **Create**

---

### **Passo 2: Criar Projeto no Azure AI Foundry**

1. No Azure Portal, pesquise por **Azure AI Foundry**
2. Clique em **Create Project**
3. Preencha:

   * **Name**: `vegan-news-curator`
   * **Region**: `East US`
   * **Resource Group**: selecione o que criou no passo anterior
4. Confirme a criação

---

### **Passo 3: Configurar o Agent**

1. Acesse o projeto recém-criado
2. No menu lateral, clique em **Agents**
3. Clique em **Create Agent**
4. Configure:

   * **Name**: `Newsletter Generator`
   * **Model**: `gpt-4` (ou modelo disponível no workspace)
   * **Description**: Editor especializado em jornalismo sobre veganismo e sustentabilidade
5. Finalize a criação


---

### **Passo 4: Obter Credenciais**

1. Dentro do projeto, acesse **Project Settings**
2. Copie:

   * `AZURE_AI_PROJECT_ENDPOINT`
   * `AGENT_ID`
3. Para o modelo:

   * Vá em **Models → Deployments**
   * Copie o nome do deployment do modelo utilizado pelo agent

---

### GNews API Configuration

#### Passo 1: Registre-se

1. Acesse [GNews.io](https://gnews.io)
2. Clique em "Sign Up"
3. Crie sua conta (gratuita ou premium)

#### Passo 2: Gere a API Key

1. Acesse seu Dashboard
2. Clique em "API Keys"
3. Copie a chave padrão ou crie uma nova

### Email SMTP Configuration

#### Para Gmail

1. Ative "[Senhas de Aplicativo](https://myaccount.google.com/apppasswords)"
2. Gere uma senha para "Email"
3. Configure:
   ```
   EMAIL_SENDER=seu_email@gmail.com
   EMAIL_PASSWORD=xxxx-xxxx-xxxx-xxxx
   SMTP_SERVER=smtp.gmail.com
   SMTP_PORT=587
   ```

#### Para Outlook/Office 365

```
EMAIL_SENDER=seu_email@outlook.com
EMAIL_PASSWORD=sua_senha
SMTP_SERVER=smtp-mail.outlook.com
SMTP_PORT=587
```

#### Para servidor customizado

Configure conforme as credenciais fornecidas pelo seu provedor.

---

## 🏗️ Arquitetura

```
┌─────────────────┐
│   GNews API     │
│  (Notícias)     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   Collector     │ (collector.py)
│  (Coleta dados) │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Formatter      │ (converters.py)
│ (Prepara para   │
│   IA)           │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Generator      │ (generator.py)
│ (Azure AI       │
│  curador)       │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Converter      │ (converters.py)
│  (HTML/Email)   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Template       │ (email_template.py)
│  (Design final) │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   Sender        │ (sender.py)
│  (SMTP Email)   │
└─────────────────┘
```

---

## 📁 Estrutura do Projeto

```
vegan-news-curator/
├── config.py                 # Configurações centralizadas
├── collector.py              # Coleta de notícias (GNews API)
├── converters.py             # Formatadores e conversores
├── generator.py              # Gerador com Azure AI
├── sender.py                 # Envio de emails SMTP
├── email_template.py         # Template HTML do email
├── main.py                   # Aplicação principal
├── pyproject.toml            # Dependências do projeto
├── .env.example              # Exemplo de variáveis de ambiente
├── README.md                 # Este arquivo
├── docs/
│   └── images/               # Screenshots de configuração
└── .gitignore                # Arquivos a ignorar no Git
```

---

## 🔄 Fluxo de Execução

### 1. Inicialização

```python
python main.py
```

**Output esperado:**
```
📰 Iniciando coleta de notícias...
✅ Coletados 20 artigos
🤖 Gerando newsletter com Azure AI...
✅ Newsletter gerada com sucesso
🎨 Convertendo para HTML...
📧 Enviando email...
✅ Email enviado com sucesso!
```

### 2. Coleta de Notícias (5-10s)

- Faz requisições à GNews API
- Coleta notícias de 5 categorias
- Remove duplicatas
- Retorna até 20 artigos únicos

### 3. Processamento com IA (30-60s)

- Formata artigos para análise
- Envia ao agente Azure AI
- IA filtra por credibilidade
- Categoriza e traduz para PT-BR
- Retorna HTML estruturado

### 4. Renderização (2-5s)

- Converte Markdown para HTML
- Aplica template profissional
- Gera email final

### 5. Envio (5-10s)

- Conecta ao servidor SMTP
- Autentica com credenciais
- Envia email

---

## 🛠️ Componentes Principais

### Config (config.py)

Gerencia todas as configurações via variáveis de ambiente:

```python
config = AppConfig()
is_valid, errors = config.validate()
```

### Collector (collector.py)

Coleta notícias da GNews API:

```python
collector = NewsCollector(config.gnews)
articles = collector.collect()
```

### Generator (generator.py)

Processa notícias com IA Azure:

```python
generator = NewsletterGenerator(config.azure)
newsletter = await generator.generate(articles_text)
```

### Sender (sender.py)

Envia emails via SMTP:

```python
sender = EmailSender(config.email)
success = sender.send(subject, html_body)
```

---

## 📊 Categorias de Notícias

A IA organiza automaticamente as notícias em:

| Emoji | Categoria | Descrição |
|-------|-----------|-----------|
| 🏥 | Saúde & Nutrição | Pesquisas médicas, benefícios nutricionais |
| 📈 | Mercado & Negócios | Empresas plant-based, startups, crescimento |
| 🌍 | Sustentabilidade & ambiente | Impacto climático, recursos naturais |
| 👨‍🍳 | Culinária | Chefs veganos, receitas, gastronomia |
| 🔬 | Tecnologia | Carnes cultivadas, proteínas alternativas |
| 📺 | Documentários Recomendados | conteúdos sobre veganismo, link oficial para trailer |

---

## 🎨 Template de Email

O design segue o padrão de jornal profissional:

- **Header**: Masthead clássico com data
- **Subnews**: Manchetes secundárias
- **Conteúdo**: Artigos em colunas com placeholders
- **Metadados**: Fonte, país, link para leitura completa
- **Footer**: Editorial final e créditos
- **Responsivo**: Adapta-se para mobile

---

## 🔐 Variáveis de Ambiente

### Obrigatórias

| Variável | Descrição | Exemplo |
|----------|-----------|---------|
| `AZURE_AI_PROJECT_ENDPOINT` | Endpoint do projeto Azure | `https://projeto.seu-projeto.azure.com/` |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Nome do deployment | `gpt-4-deployment` |
| `AGENT_ID` | ID do agente Azure | `agent-123-abc` |
| `GNEWS_API_KEY` | Chave da API GNews | `abc123xyz789` |
| `EMAIL_SENDER` | Email remetente | `seu_email@gmail.com` |
| `EMAIL_PASSWORD` | Senha/App Password | `xxxx-xxxx-xxxx` |
| `RECIPIENT_EMAIL` | Email destinatário | `destinatario@exemplo.com` |

### Opcionais

| Variável | Descrição | Padrão |
|----------|-----------|--------|
| `SMTP_SERVER` | Servidor SMTP | `smtp.gmail.com` |
| `SMTP_PORT` | Porta SMTP | `587` |

---

## 📈 Performance

| Operação | Tempo Médio |
|----------|------------|
| Coleta de notícias | 5-10s |
| Processamento com IA | 30-60s |
| Renderização HTML | 2-5s |
| Envio de email | 5-10s |
| **Total** | **45-85s** |

---

### 🎓 Sobre o Desafio e a Origem do Projeto

Este projeto foi desenvolvido como entrega final do **Build Your First Copilot Challenge (Foundry Edition)**, proposto no curso **Azure Frontier Girls**, ministrado pela **[WoMakersCode](https://www.maismulheres.tech/)**. O desafio incentivava a criação de soluções reais utilizando o **Azure AI Foundry**, explorando agentes, processamento inteligente e automações práticas.

A atividade oficial do challenge pode ser consultada no repositório:
**[https://github.com/Miyake-Diogo/AzureFrontierGirls-AI-Challenge](https://github.com/Miyake-Diogo/AzureFrontierGirls-AI-Challenge)**


## 📄 Licença

Este projeto está sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---
