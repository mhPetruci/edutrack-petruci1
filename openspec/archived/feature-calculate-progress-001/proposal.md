# feature-calculate-progress Proposal

## Why
Os usuários precisam de um cálculo simples e confiável do progresso nas tarefas, expresso como porcentagem de itens concluídos em relação ao total. Um script Python dedicado em `scripts/calculate_progress.py` permitirá reutilização fácil, integração com dados existentes e geração direta de JSON para consumo por outras partes do sistema.

## What Changes
Será criado um script Python em `scripts/calculate_progress.py` que:
- Recebe uma lista de tarefas com status
- Calcula a porcentagem de progresso como `concluídas / total`
- Retorna um JSON com os resultados

## Impact
- **Baixo risco**: funcionalidade isolada em script utilitário
- **Compatibilidade**: pode ser usado por backend, automações ou frontends sem alterar a base de dados
- **Reutilização**: prepara o caminho para futuras integrações de dashboards e relatórios
