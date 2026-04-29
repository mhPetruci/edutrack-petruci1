# feature-subjects-crud Proposal

## Why
Os usuários precisam gerenciar suas disciplinas (`subjects`) com operações completas de criação, leitura, atualização e exclusão. Para garantir segurança e privacidade, cada usuário só deve acessar e modificar seus próprios dados.

## What Changes
Será implementado um conjunto de endpoints CRUD para a tabela `subjects`:
- `POST /subjects` para criar uma nova disciplina
- `GET /subjects` para listar disciplinas do usuário autenticado
- `PATCH /subjects/{subject_id}` para atualizar uma disciplina existente
- `DELETE /subjects/{subject_id}` para remover uma disciplina

A implementação incluirá validação de propriedade de dados, garantindo que apenas o proprietário de cada subject possa visualizar ou modificar o registro.

## Impact
- **Baixo risco**: adiciona endpoints em uma área lógica nova, sem alterar a estrutura de dados existente.
- **Segurança**: reforça controles de acesso para evitar vazamento ou modificação de dados de outros usuários.
- **Escalabilidade**: provê base para futuras automações e relatórios por usuário.
