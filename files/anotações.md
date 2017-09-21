## 1.2 Algorithms

- A classe de algoritmos foi divida em duas partes:
  - transformation Algorithms
  - adaptation Algorithms

- transformation Algorithms:
  - processa o dataset e converte o contexto para uma matriz de duas dimensões, que contém
  informações de usuários, itens e classificações(ratings). Uma das tecnicas utilizadas pelos
  pesquisadores é dividir(split)no dataset. Fazer isso usando python.

  - adaptation Algorithms:
    - tem duas subcategorias: independent modeling que assume que o contexto é independente de
  usuário e item e a dependent modeling que explora a dependencia entre usuario, item e contexto.

### dependent context
   - pode ser construido de duas manerias: modelando o contexto das classificações e aprendendo
  por similaridade. Neste processo de aprendizagem um posso usar a matriz de fatoração, uma vez
  que o processo de similaridade é aprendido pela relação entre o par (user, item).

  Para efeito final, eu devo verificar

## 1.3 Evaluations
- A maioria dos algoritmos do CARSKit possuem duas tarefas de recomendação:
  - rating prediction (previsão de classificação)
  - item recommendation (recomendação de item)

- Estudar
  - MAP (mean average precison)
  - NDGC (normalized discounted cumulative gain)
  - MMR (mean reciprocal rank)


## 2.1 Data Format
- O meu dataset possui os seguntes campos:
  - userid
  - itemid
  - rating (1, 2, 3, 4, 5)
  - Time (quando o filme foi visto (Weekend, Weekday))
  - Location (posso usar como informação do contexto) (Home, Cinema)
  - Companion (informação de contexto, se viu o filme) (Alone, Partner, Family)
- Programa aceita dois formatos de dataset, vou usar o formato Compact Format. Esse formato
cada linha representa um simples contexto
- Depois disso preciso converter para o formato binario
