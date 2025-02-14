# 🚀 API de Conversão de Números para Texto

Esta API converte números inteiros para sua representação por extenso em português. Desenvolvida com **FastAPI** e implantada na **AWS Lambda** utilizando **API Gateway**. 🔥

## 🌟 Tecnologias Utilizadas
- 🐍 **Python** com **FastAPI**
- ☁️ **AWS Lambda** + **API Gateway**
- ⚡ **Serverless Framework**
- 🔢 **num2words** para conversão numérica

## 📌 Endpoints
### 🔄 Converter número para texto
```http
GET /convert/{number}
```
📌 **Parâmetros:**
- `number` (int) → Número a ser convertido

📌 **Exemplo de resposta:**
```json
{
  "number": 123,
  "text": "cento e vinte e três"
}
```

## 📥 Instalação e Deploy
### 🔧 Requisitos
- Python 3.9+
- Node.js + Serverless Framework
- Conta AWS configurada

### 🚀 Rodando Localmente
```bash
git clone https://github.com/seu-usuario/fastapi-number-text.git
cd fastapi-number-text
pip install -r requirements.txt
uvicorn main:app --reload
```
Acesse: [http://127.0.0.1:8000/convert/123](http://127.0.0.1:8000/convert/123)

### 🌍 Deploy na AWS
```bash
serverless deploy
```

## 📷 Imagens do Projeto
_Aqui você pode adicionar capturas de tela da API em funcionamento._

---
🛠 **Criado por:** Pedro Henrique Araújo Mattos Ribeiro

