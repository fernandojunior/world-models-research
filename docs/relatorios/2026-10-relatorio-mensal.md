# Relatório Mensal de Atividades — Outubro/2026

**Projeto:** Antecipação e Exploração Estratégica de World Models para Inovação em Inteligência Artificial (400988/2026-7)
**Bolsista:** Fernando Felix · **Tutor:** Gilliard Custodio · **Empresa:** Instituto Itaú de Ciência, Tecnologia e Inovação (ICTi)
**Período:** 01/10/2026 a 31/10/2026 (mês 1 de 12)

## Resumo

Primeiro mês do projeto, dedicado a onboarding, configuração de ambiente, capacitações obrigatórias do Programa Inova Talentos e início da Macroação 1 (Planejamento e Fundamentação Conceitual). Foram produzidos um relatório de pesquisa sobre o estado da arte em World Models, dois guias de estudo interativos (conceitual e matemático), o mapeamento inicial de implementações open source e o plano de trabalho detalhado do projeto. Todo o material está versionado em https://github.com/fernandojunior/world-models-research.

## Atividades realizadas

### Macroação 1 — Planejamento e Fundamentação Conceitual

| Sub | Atividade | Situação | O que foi feito |
|---|---|---|---|
| 1.1 | Definição do escopo conceitual e critérios de seleção da literatura | Em andamento | Escopo delimitado em três famílias de World Models (reconstrução de pixels, predição latente/JEPA, simuladores explícitos / real-to-sim) e em dados sequenciais; definido o eixo prático do ano 1 (reprodução de abordagens open source com base real-to-sim). Critérios de seleção em consolidação. |
| 1.2 | Levantamento inicial de artigos e organização do repositório de referências | Em andamento | Levantamento de literatura consolidado no relatório *World models: fundamentos, fronteira e teses viáveis* ([docs/relatorio-fundamentos](https://github.com/fernandojunior/world-models-research/blob/main/docs/relatorio-fundamentos/world-models-fundamentos-e-pesquisa.md)), cobrindo história (Craik 1943, Schmidhuber 1990, Dyna, Ha & Schmidhuber 2018), sete escolas, surveys de 2025–2026 e referências com marcação de verificação em fonte primária. Organização em repositório de referências (Zotero/planilha) pendente. |
| 1.3 | Elaboração de guias de fundamentos e glossário técnico sobre World Models | Concluída (revisão final pendente) | Dois guias publicados e revisados em duas rodadas de correção factual: **World models do zero** ([HTML](https://github.com/fernandojunior/world-models-research/blob/main/docs/guias/world-models-do-zero.html) · [visualizar](https://htmlpreview.github.io/?https://github.com/fernandojunior/world-models-research/blob/main/docs/guias/world-models-do-zero.html)) — 15 seções, notação, glossário bilíngue, roteiro de leitura de papers e perguntas de autoavaliação; **Matemática para world models** ([HTML](https://github.com/fernandojunior/world-models-research/blob/main/docs/guias/matematica-para-world-models.html) · [visualizar](https://htmlpreview.github.io/?https://github.com/fernandojunior/world-models-research/blob/main/docs/guias/matematica-para-world-models.html)) — 19 módulos do nível 0 (média, variância, probabilidade) a inferência variacional, difusão e erro composto, com simuladores interativos, experimentos reproduzíveis e scripts Python. |
| 1.4 | Mapeamento de implementações open source relativas a World Models, requisitos de processamento e infraestrutura | Em andamento | Tabela de ferramentas na §6 do relatório de fundamentos (DreamerV3 oficial e ports, SheepRL, TD-MPC2, IRIS, DIAMOND, stable-worldmodel, Cosmos, V-JEPA 2, Craftax, Minari) com licença, stack, requisito de hardware declarado e status de manutenção, mais análise do que é viável em hardware modesto. Ferramentas de real-to-sim e levantamento da infraestrutura do ICTi ficam para novembro. |
| 1.5 | Levantamento inicial das perguntas de pesquisa | Em andamento | Catálogo de 14 problemas abertos etiquetados por viabilidade (§7 do relatório) e recorte prático em real-to-sim como fonte de dados e verificação para World Models. Perguntas-guia do projeto a fixar em novembro. |

### Macroação 4 — Monitoramento de Tendências e Consolidação

| Sub | Atividade | Situação | O que foi feito |
|---|---|---|---|
| 4.1 | Monitoramento contínuo de novas publicações e tendências | Iniciada (prevista para nov) | O relatório de fundamentos já incorpora lançamentos de 2026 (LeWorldModel, V-JEPA 2.1, Cosmos 3, Genie 3, surveys de avaliação). Rotina mensal de monitoramento começa em novembro, conforme plano. |

### Macroação 5 — Acompanhamento, Disseminação e Prestação de Contas

| Sub | Atividade | Situação | O que foi feito |
|---|---|---|---|
| 5.1 | Relatório mensal ao IEL com validação do tutor | Em andamento | Este relatório. |
| 5.3 | Elaboração e validação do Plano de Trabalho com tutor e IEL | Concluída (validação com IEL pendente) | Plano de trabalho detalhado com 5 macroações, 24 subatividades, datas e cronograma visual ([plano](https://github.com/fernandojunior/world-models-research/blob/main/docs/plano-de-trabalho/plano-de-trabalho.md) · [cronograma](https://htmlpreview.github.io/?https://github.com/fernandojunior/world-models-research/blob/main/docs/plano-de-trabalho/cronograma.html)). Preenchido em conjunto com o tutor no formulário do Inova Talentos. |
| 5.4 | Capacitações EAD do Programa Inova Talentos | Em andamento | Onboarding Inova Talentos: 100%. Competências para Inovação e Alta Performance: 60%. Trilha de Soft Skills: 8%. |

### Atividades de integração (fora das macroações)

- Configuração de notebook corporativo, VPN e acessos.
- Participação na integração de bolsistas (plantão de dúvidas IEL/SENAI).

## Entregáveis produzidos no mês

| Entregável | Link |
|---|---|
| Relatório *World models: fundamentos, fronteira e teses viáveis* | [docs/relatorio-fundamentos/world-models-fundamentos-e-pesquisa.md](https://github.com/fernandojunior/world-models-research/blob/main/docs/relatorio-fundamentos/world-models-fundamentos-e-pesquisa.md) |
| Guia *World models do zero* | [docs/guias/world-models-do-zero.html](https://github.com/fernandojunior/world-models-research/blob/main/docs/guias/world-models-do-zero.html) |
| Guia *Matemática para world models* | [docs/guias/matematica-para-world-models.html](https://github.com/fernandojunior/world-models-research/blob/main/docs/guias/matematica-para-world-models.html) |
| Plano de trabalho detalhado | [docs/plano-de-trabalho/plano-de-trabalho.md](https://github.com/fernandojunior/world-models-research/blob/main/docs/plano-de-trabalho/plano-de-trabalho.md) |
| Cronograma por macroação | [docs/plano-de-trabalho/cronograma.html](https://github.com/fernandojunior/world-models-research/blob/main/docs/plano-de-trabalho/cronograma.html) |

## Próximos passos (novembro/2026)

- Concluir 1.1 (critérios de seleção formalizados) e 1.2 (repositório de referências organizado).
- Passada final nos guias (1.3) e consolidação do Entregável 1: documento de planejamento + baseline conceitual, até 30/11.
- Completar 1.4 com ferramentas de real-to-sim e levantamento da infraestrutura disponível no ICTi (GPU, rede, política de download de pesos e datasets).
- Fixar as perguntas-guia do projeto (1.5).
- Validar o plano de trabalho com o IEL (5.3) e avançar nas trilhas EAD (5.4).
- Iniciar o monitoramento mensal de tendências (4.1).

## Observações

Outubro foi em parte consumido por onboarding e configuração de acessos, como previsto para o primeiro mês. A Macroação 1 concentra-se em novembro, o que é viável porque os guias de fundamentos e o levantamento de literatura já estão adiantados. Nenhum impedimento registrado; o principal ponto de atenção para a Macroação 3 (março/2027) é a infraestrutura de processamento, a ser mapeada em novembro.
