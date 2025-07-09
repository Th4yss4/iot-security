# Sensor de Movimento 

Este repositório contém duas versões de código para controle de um sensor de movimento (PIR) com LEDs indicadores e integração opcional com Wi-Fi e Telegram

![{F2BEE6EF-8B77-4FDD-B3A3-007FBC81CFEA}](https://github.com/user-attachments/assets/4d8eb95d-00f3-4ff6-86bc-effecb00dd5f)


## 📂 Arquivos

* **`sensor-de-movimento.ino`**

  * Versão básica do código para ESP32 ou Arduino.
  * Não possui conexão com rede.
  * Gerencia três LEDs (vermelho, amarelo e verde) com base no movimento detectado pelo sensor PIR.
  * **Lógica**:

    * LED vermelho: Sempre ligado (indica o funcionamento do sistema).
    * LED amarelo: Liga ao detectar movimento.
    * LED verde: Liga após 5 segundos de movimento contínuo.
    * Desliga LEDs amarelo e verde após 2 segundos sem movimento.

* **`sensor-de-movimento_versao-com-wifi.ino`**

  * Versão com conexão Wi-Fi e envio de notificações para o Telegram.
  * Requer credenciais de Wi-Fi e token de bot do Telegram.
  * Além do comportamento dos LEDs descrito acima, envia uma mensagem para um chat do Telegram quando o movimento é detectado.
  * **Adições principais**:

    * Biblioteca `WiFi.h` e `HTTPClient.h` para conexão e requisições HTTP.
    * Função para enviar notificação ao Telegram com o token e chat ID.
    * Verificação de conexão à rede antes de tentar enviar mensagens.

## 🔑 Diferenças entre as versões

| Funcionalidade                      | `sensor-de-movimento.ino` | `sensor-de-movimento_versao-com-wifi.ino` |
| ----------------------------------- | ------------------------- | ----------------------------------------- |
| Detecção de movimento com PIR       | ✅                         | ✅                                         |
| Controle de LEDs                    | ✅                         | ✅                                         |
| Conexão Wi-Fi                       | ❌                         | ✅                                         |
| Envio de notificações para Telegram | ❌                         | ✅                                         |
| Dependências adicionais             | ❌                         | `WiFi.h`, `HTTPClient.h`                  |

## 🚀 Como usar

### 1️⃣ Versão Básica (`sensor-de-movimento.ino`)

* Carregue o código em um ESP32 ou Arduino.
* Conecte o sensor PIR e os LEDs nos pinos especificados no código.
* O sistema funciona sem precisar de rede.

### 2️⃣ Versão com Wi-Fi e Telegram (`sensor-de-movimento_versao-com-wifi.ino`)

* Insira suas credenciais Wi-Fi nas variáveis `ssid` e `password`.
* Crie um bot no Telegram e insira o token e o chat ID no código.
* Carregue o código no ESP32.
* Ao detectar movimento, o sistema enviará uma notificação via Telegram.

## 📌 Requisitos de Hardware

* ESP32 ou Arduino (ESP32 recomendado para Wi-Fi)
* Sensor de movimento PIR
* 3 LEDs (vermelho, amarelo e verde)
* Resistores apropriados para os LEDs
