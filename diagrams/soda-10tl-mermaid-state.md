```{mermaid}
stateDiagram-v2
    direction LR

    [*] --> q0 : Başlangıç
    q0 --> q5 : 5 TL
    q5 --> q_soda : 5 TL
    q_soda --> q_soda : 5 TL

    q0 : q0 (0 TL)
    q5 : q5 (5 TL)
    q_soda : q_soda (10 TL) [Kabul Durumu]  
```
