### This is a parsing code of CoAP messages on IoTivity protocol analysis.
<img width="500" alt="coap" src="https://user-images.githubusercontent.com/80508931/133028059-b17c23dc-d7e1-445d-a6b0-e270bd6786b0.png">

- This is the CoAP Protocol, which I used for parsing.
- You can see the message format, the first lines are composed with 32-bit message.
- Python compiles the binary numbers starting with '0b', and this message shouldn't be included in the parsing code. 
- Changing from hex to bin, it only shows 31 bits, because when the number changes it, skips the 0.
