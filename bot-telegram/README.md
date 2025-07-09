# 🚨 Bot de Segurança com Telegram e WhatsApp

Este projeto consiste em dois bots Telegram integrados a funcionalidades de segurança:

1. **app.py** – Um bot avançado que:

   * Envia e recebe imagens.
   * Recebe localização do usuário e salva em arquivo.
   * Envia alertas via WhatsApp usando Twilio.
   * Fornece mapas de locais específicos com comandos personalizados.

2. **bot.py** – Um bot simples que:

   * Retorna o `chat_id` do usuário para configuração rápida.

---

## 📂 Estrutura

```
.
├── app.py           # Bot Telegram com integração ao Twilio (WhatsApp)
├── bot.py           # Bot Telegram para obter chat_id
├── localizacoes.txt # Armazena as localizações recebidas (gerado em runtime)
├── mapa_ccn.jpg     # (Opcional) Mapa do CCN para envio
├── mapa_cchl.jpg    # (Opcional) Mapa do CCHL para envio
```

---

## ⚙️ Configuração

### 1️⃣ Pré-requisitos

* Python 3.8+
* Bibliotecas:

  ```bash
  pip install python-telegram-bot==20.0b0 twilio
  ```

### 2️⃣ Configurar credenciais

Edite os arquivos:

#### `app.py`

Substitua os valores de configuração:

```python
TELEGRAM_TOKEN = 'SEU_TOKEN_TELEGRAM'
ACCOUNT_SID = 'SEU_ACCOUNT_SID_TWILIO'
AUTH_TOKEN = 'SEU_AUTH_TOKEN_TWILIO'
TWILIO_WHATSAPP_NUMBER = 'whatsapp:+14155238886'  # Exemplo Twilio Sandbox
NUMERO_DESTINO = 'whatsapp:+55SEUNUMERO'
```

#### `bot.py`

Substitua o token pelo do seu bot:

```python
TOKEN = 'SEU_TOKEN_TELEGRAM'
```

---

## 🚀 Como usar

### 📱 Executar bot principal

```bash
python app.py
```

O bot estará pronto com os comandos:

* `/start` – Inicializa o bot.
* `/ccn` – Envia o mapa do CCN.
* `/cchl` – Envia o mapa do CCHL.
* `/alerta` – Envia alerta via WhatsApp.
* 📸 Envie uma **foto** – O bot baixa e confirma.
* 🗂️ Envie um **documento de imagem** – O bot baixa e confirma.
* 📍 Envie **localização** – O bot salva e responde.

### 🔑 Obter seu chat\_id (opcional)

Use o `bot.py` para obter o `chat_id` do Telegram:

```bash
python bot.py
```

No Telegram, envie `/start` ao bot e veja o `chat_id` retornado.

---

## 🛡️ Aplicações

✅ Envio e recebimento de imagens para suporte remoto.

## 📌 Observação

* Certifique-se de que o Twilio esteja configurado para envio de mensagens WhatsApp (ativar sandbox ou número verificado).
* Adicione os arquivos `mapa_ccn.jpg` e `mapa_cchl.jpg` na mesma pasta para uso dos comandos de mapa.
