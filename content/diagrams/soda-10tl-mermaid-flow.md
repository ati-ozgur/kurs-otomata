```{mermaid}
flowchart LR
    Start((" ")) --> q0

    q0("q0<br/>(0 TL)") -- 5 TL --> q5("q5<br/>(5 TL)")
    q5 -- 5 TL --> qsoda((("q_soda<br/>(10 TL)<br/>[Kabul]")))
    qsoda -- 5 TL --> qsoda

    style Start fill:none,stroke:none
    style q0 stroke:#333,stroke-width:2px
    style q5 stroke:#333,stroke-width:2px
    style qsoda stroke:#28a745,stroke-width:3px,fill:#d4edda
```