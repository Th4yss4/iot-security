# Sistema de Segurança Pessoal IoT

Um sistema de segurança pessoal baseado em IoT que permite acionar rapidamente uma emergência por meio de um app, integrando localização em tempo real, comunicação instantânea e automação de iluminação para aumentar a segurança do usuário.




## Funcionalidades Principais

- **Aplicativo Mobile ou Web**
    - Botão de emergência virtual.
    - Registro de características do incidente.
    - Exibição de locais menos iluminados para evitar durante a noite.

- **Geolocalização**
    - Envio da localização em tempo real ao ser acionado.

- **Central de Monitoramento**
    - Recebe alertas e coordena ações.
    - Pode ser uma central profissional ou uma rede de contatos pré-definidos (amigos/familiares).

- **Notificações por Mensageria**
    - Envio imediato de alertas via SMS, WhatsApp, Telegram ou outros canais para contatos de emergência.

- **Integração com Iluminação Inteligente**
    - Aumenta a visibilidade em ambientes menos iluminados.
    - **Modo Presença:**
        - Ausência de movimento: luz baixa ou desligada.
        - Presença detectada: luz alta.

## Fluxo de Dados do Sistema

O sistema é estruturado em três camadas principais: **Entrada**, **Processamento (IoT/Backend)** e **Ações (Iluminação e Mensageria)**. Cada camada se comunica entre si para garantir uma resposta rápida e eficiente em situações de emergência.

![Usuário (APP) (1)](https://github.com/user-attachments/assets/08487bdd-720c-4d9b-8924-8e0975fc52c9)

---

### 1º Andar — Entrada e Processamento Inicial

| Componente         | Descrição |
|--------------------|-----------|
| **Usuário (APP)**  | Interface principal para o acionamento do botão de emergência, envio de localização e visualização de locais perigosos. Inicia o fluxo de dados com um alerta. |
| **Localização + Alerta** | Dados de GPS e status de emergência enviados ao backend. |
| **API Flask**      | Backend responsável por receber e processar alertas, comunicar-se com o banco de dados e coordenar os módulos de notificação e hardware. |

---

### 2º Andar — Camada de Dispositivos e Sensores

| Componente       | Descrição |
|------------------|-----------|
| **ESP32**        | Microcontrolador responsável por controlar os sensores e a iluminação inteligente. Pode comunicar-se com o backend. |
| **Sensores (Proximidade e Iluminação)** | Captam movimento (sensor PIR) e luminosidade (LDR), fornecendo dados ao ESP32 para ativar a iluminação conforme necessidade. |
| **Banco de Dados** | Armazena informações como localização do usuário, histórico de alertas, logs de sensores e registros de mensagens enviadas. |

---

### 3º Andar — Camada de Ação e Saída

| Componente                 | Descrição |
|----------------------------|-----------|
| **Iluminação Inteligente** | LEDs controlados via ESP32 que se adaptam ao movimento e luminosidade do ambiente, aumentando a segurança em locais escuros. |
| **Mensagem de Alerta**     | Envio automático de notificações via Telegram, WhatsApp ou SMS para contatos cadastrados, contendo a localização e o tipo de alerta. |

---

## Tecnologias Utilizadas

- IoT (Internet das Coisas)
- Geolocalização (GPS)
- APIs de mensageria (SMS, WhatsApp e/ou Telegram)
- Automação de iluminação inteligente
- Aplicativo Mobile (Android/iOS) ou Web

## Como Funciona

1. O usuário aciona o botão de emergência no app.
2. O sistema envia a localização em tempo real para a central de monitoramento.
3. Notificações são enviadas imediatamente para contatos de emergência.
4. O sistema mostra os locais menos ilumindos, para serem evitados durante a noite.

## Contribuição



## Licença

