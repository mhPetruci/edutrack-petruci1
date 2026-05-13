# Configuração do EduTrack AI

## 🔧 Variáveis de Ambiente Necessárias

Para executar o EduTrack AI localmente, você precisa configurar o arquivo `.streamlit/secrets.toml`:

```toml
# API Backend
API_BASE_URL = "http://localhost:3000"  # URL da sua API Xano/Backend

# Opcional: Configurações de Email para Password Reset (futuro)
# SMTP_SERVER = "smtp.gmail.com"
# SMTP_PORT = 587
# SMTP_USERNAME = "seu-email@gmail.com"
# SMTP_PASSWORD = "sua-senha-de-app"
# SENDER_EMAIL = "seu-email@gmail.com"
```

## 📍 Localização

O arquivo `.streamlit/secrets.toml` deve estar localizado em:
- Windows: `C:\Users\<usuario>\.streamlit\secrets.toml`
- macOS: `~/.streamlit/secrets.toml`
- Linux: `~/.streamlit/secrets.toml`

## ✅ Verificação

Após criar o arquivo, você pode verificar se está funcionando executando:

```bash
streamlit run app.py
```

Se a variável `API_BASE_URL` não for encontrada, o padrão é `http://localhost:3000`.

## 🚀 Executando o Projeto

1. Instale as dependências:
```bash
pip install -r requirements.txt
```

2. Configure o `.streamlit/secrets.toml`

3. Execute a aplicação:
```bash
streamlit run app.py
```

4. Acesse em: `http://localhost:8501`

## 📦 Dependências Principais

- `streamlit` - Framework UI
- `requests` - HTTP client
- `pandas` - Manipulação de dados
- `python-dateutil` - Manipulação de datas

Veja `requirements.txt` para a lista completa.
