**Table of Contents**

---

# 24 March 2026

**Key Outcomes:** RFC and Operation Type analysis progressing well with concrete next steps identified. The strategy of focusing Laura on smaller, bounded challenges is working — she appeared more focused and relaxed with more insightful outcomes to present.

**RFC Jira Projects Standardization:** Laura's holidays were booked on the team calendar. We discussed updating RFC Jira projects (Production and Demo) to ensure both projects have similar content structure. The next step will be extending this standardization work to RDINC project.

**Operation Type Analysis and Runbook Refinement:** Laura presented the numbers from her RFC and Operation Type analysis. We decided to move forward with refinement of the top operation types mentioned and drill down on runbook analysis to centralize and create a 1:1 connection between operation types and catalog articles. This involves either refining the operation type definitions or standardizing the repeated catalog articles.

**RFC Framework Review:** Laura shared the framework review for RFCs. Vera will read and provide feedback on the proposed framework.

**Progress and Focus:** The plan established in the previous 1:1 to focus Laura on smaller challenges is working effectively. Laura looked more focused and relaxed during this meeting with more insightful outcomes to present. Laura will continue to work closely with Paulo on the Change Management track.

**Next Steps:**

- Ensure Production and Demo RFC Jira projects have similar content - Laura
- Start RDINC Jira project update - Laura
- Move forward with refinement of top operation types - Laura
- Drill down on runbook analysis to centralize and create 1:1 connection - Laura
- Read and provide feedback on RFC framework review - Vera
- Continue working closely with Paulo on Change Management track - Laura

---

# 12 March 2025

**Key Outcomes:** Adjusted onboarding expectations to focus on small, deliverable wins over the next week. Laura will work collaboratively with Inês on two priorities: reviewers framework (Method 2.2) and catalog articles lifecycle. Clear signal given to ask for help earlier before stress escalates.

**Managing Onboarding Pressure:** Laura has been navigating tighter expectations and more assertive timelines. We recalibrated to focus on small wins and reduced the scope on analysis work that was causing stress. The goal is to build momentum through concrete, bounded deliverables rather than broad initiatives.

**Asking for Help Earlier:** Pattern identified: Laura only asks for help when explicitly prompted or when stress is already high. Reinforced that asking for help is expected during onboarding, not a weakness. Emphasis on team support and raising blockers proactively.

**Collaborative Work with Inês:** Laura and Inês will work together next week on the two priority topics. Inês brings context and stakeholder knowledge, which will help Laura build confidence for future independent work. Inês will handle Operations Review preparation this week so Laura can focus on Method 2 deliverables.

**Metrics and SMART Goals:** Sent Laura metrics as a foundation for implementation planning. Next step is for Laura to define her own SMART goals aligned with her method ownership and team presence.

[PE-STRAT-03] - V2MOM Measurement Plan

**Process Documentation and Automation:** Laura is updating documentation with new links and ensuring the space reflects current processes. Discussion on automating repetitive tasks (reviewers, frameworks) and distinguishing between virtual team work and internal team operations. Documentation updates targeted for end of week.

**Next Steps:**

- Focus on two small wins next week: reviewers framework and catalog articles lifecycle - Laura
- Work collaboratively with Inês on both topics - Laura & Inês
- Define SMART goals for method ownership - Laura
- Complete documentation updates by end of week - Laura
- Ask for help proactively when blockers arise - Laura
- Schedule follow-up on metrics implementation discussion - Vera

---

# 10 Outubro 2025

Vera explicou para Laura os processos de gestão de mudanças e operações de processos, incluindo a organização do Change Advisory Board, a moderação de eventos e a importância das métricas como Change Failure Rate. A conversa abordou a arquitetura de rings e regiões da empresa, o sistema de gestão de incidentes, e os diferentes níveis de incidentes e mudanças. Vera e Laura discutiram problemas no processo de aprovação de mudanças e definiram como objetivo principal organizar e centralizar o catálogo de operações, começando com uma análise detalhada dos dados do último mês.

## Os próximos passos

- [Laura: Documentar o processo de diferenciação entre falhas e incidentes para o projeto Deployment Failure Reporting.](https://tasks.zoom.us?meetingId=swfAfnACRWitm6nQjE%2FBIQ%3D%3D&stepId=b620f89a-a5fb-11f0-90ba-a243bd341e1b)
- [Vera: Compartilhar documentação sobre arquitetura de ringues e regiões com Laura.](https://tasks.zoom.us?meetingId=swfAfnACRWitm6nQjE%2FBIQ%3D%3D&stepId=b62102fb-a5fb-11f0-ae17-a243bd341e1b)
- [Laura: Revisar a documentação do ODC Illustrated para entender melhor a relação entre ringues e regiões.](https://tasks.zoom.us?meetingId=swfAfnACRWitm6nQjE%2FBIQ%3D%3D&stepId=b62107a5-a5fb-11f0-82fe-a243bd341e1b)
- [Vera: Adicionar Laura aos canais de CAB para acompanhamento.](https://tasks.zoom.us?meetingId=swfAfnACRWitm6nQjE%2FBIQ%3D%3D&stepId=b6210af1-a5fb-11f0-9189-a243bd341e1b)
- [Vera: Compartilhar informações sobre os SLAs de disponibilidade e os limites de downtime permitidos.](https://tasks.zoom.us?meetingId=swfAfnACRWitm6nQjE%2FBIQ%3D%3D&stepId=b6210e92-a5fb-11f0-b99d-a243bd341e1b)
- [Laura: Organizar uma simulação com António do suporte português para entender o fluxo de trabalho entre Zendesk e Jira.](https://tasks.zoom.us?meetingId=swfAfnACRWitm6nQjE%2FBIQ%3D%3D&stepId=b62111f3-a5fb-11f0-9f9e-a243bd341e1b)

## Resumo do relatório

### Gestão de Mudanças e Operações

Vera explicou para Laura os diferentes aspectos dos processos de gestão de mudanças e operações de processos, incluindo a organização do Change Advisory Board e a moderação de eventos como retrospetivas. Vera esclareceu que a equipe normalmente modera e coordena esses processos, mas não os executa diretamente, entregando as operações aos processos executores. A conversa também abordou a importância das métricas como Change Failure Rate, que faz parte do DORA Framework para organizações de desenvolvimento de produtos.

### Medição Precisa do Change Failure Rate

Vera explicou que a equipe atualmente não consegue medir com precisão o change failure rate porque está a medir um deployment failure rate diferente. Ela descreveu como o sistema atual de incidentes se tornou complexo e impossível de gerir, gerando um volume excessivo de incidentes que não impactam diretamente os clientes. Vera decidiu que o projeto de deployment daily reporting deve avançar primeiro para separar as falhas da pipeline dos incidentes reais, permitindo depois implementar com precisão o change failure rate.

### Processo Incidentes

Vera detalhou o processo de incidentes, explicando como os alarmes são convertidos em incidentes e como a equipe SRE (Site Reliability Engineering) define a severidade e confirma se um incidente tem impacto sistema amplo. Vera também descreveu os diferentes papéis no processo de incidentes, incluindo o Incident Commander e o Internal Communications Lead, e mencionou que Inês lançou recentemente uma nova status page interna para monitorizar incidentes.

### Arquitetura de Rings e Regiões

Vera explicou a Laura sobre a arquitetura de rings e regiões da ODC, esclarecendo que existem múltiplas regiões geográficas (Londres, Ásia, Israel, Canadá) onde os servidores são alojados. Vera explicou que incidentes de clientes são categorizados entre os rings 1 e 3, sendo o ringue 3 o ambiente de produção principal onde os clientes pagantes estão localizados. Vera também esclareceu que os ringues -1, -2 e -3 (rings negativos) são ambientes de desenvolvimento que têm diferentes níveis de disponibilidade e requisitos de qualidade, com o ring +3 tendo tolerância menor à indisponibilidade e um SLA de 99.9% que permite apenas 43 minutos de downtime mensal em produção.

### Sistema de Gestão de Incidentes

Vera explicou a Laura como funciona o sistema de gestão de incidentes, esclarecendo que o suporte trabalha através do Zendesk enquanto a engenharia usa o Jira para casos complexos. Vera detalhou as diferenças entre arquiteturas multi-tenant e single-tenant, explicando que no ODC não é possível fazer marteladas no sistema devido à infraestrutura compartilhada entre vários clientes. A discussão também abordou os diferentes níveis de incidentes (SEV1, SEV2, SEV3, SEV4) e como são roteados automaticamente para as equipes apropriadas, com casos Sev1 sendo tratados como incidentes SRE se impactarem áreas críticas do sistema.

### Mecanismos de Incident Response

Vera e Laura discutiram a necessidade de criar action items para detectar problemas mais cedo durante as retrospectivas, já que questões como falta de documentação ou ferramentas não existentes foram identificadas apenas retrospetivamente. Vera apresentou diagramas detalhados dos use cases de incident response que cobrem 99% dos casos, explicando que os mecanismos de mobilização são geridos pela equipe SRE através da ferramenta Rootly. Vera também esclareceu a diferença entre os três tipos de mudanças: emergency (com maior risco e necessitando aprovação hierárquica), standard (baixo risco e aprovadas automaticamente) e normal (com risco mínimo e não necessitando aprovação).

### Processo de Aprovação de Changes

Vera explicou o processo de aprovação de changes, distinguindo entre emergências que não passam por revisão e normal changes que requerem aprovação via catalogue articles. Ela enfatizou a importância da segregação de direitos e deveres, onde revisores não podem pertencer à equipe que solicita o change, e explicou que o processo inclui aprovação de líderes de área e revisores independentes. Vera identificou um problema atual onde as equipes estão fazendo mudanças manualmente em vez de através do pipeline certificado, resultando em uma pipeline de changes descontrolada, e indicou que o trabalho de Laura focará em resolver essa situação.

### Análise de Operações via Change Requests

Vera apresentou uma análise dos tipos de operações realizadas através de change requests, usando dados do Power BI para identificar artigos de catálogo mencionados. A análise revelou 227 operações distintas identificadas, mas ainda existem 106 operações não identificadas que precisam de análise manual. Vera definiu como primeiro objetivo do projeto de Laura a organização e centralização do catálogo de operações, começando com uma análise detalhada dos dados do último mês para determinar quais operações estão sendo executadas e criar um framework para classificação.

### Processo de Aprovação de Mudanças

Vera e Laura discutiram problemas no processo de aprovação de mudanças, em que o controle só se estende até as descidas serem aprovadas, e depois perdem o rasto sobre se as mudanças foram implementadas. Vera explicou que precisam desenvolver um sistema para forçar a transição para a implementação e recolher evidências de que as mudanças foram executadas, mencionando que a equipe de run time data model já está a fazer algo similar. Vera também descreveu um projeto de análise manual de operações que precisará de trabalho manual para classificar mudanças que não podem ser identificadas automaticamente, e pediu a Laura que comece a pensar como fazer essa análise de forma eficiente nas próximas semanas.
