---
name: ADR-015 AIOS Workflow (DEV→PROD)
description: Workflow correto para sincronizar AIOS meta-system: DEV is source of truth
type: feedback
---

## Regra Crítica

**DEV → push → origin/master → pull → PROD**

Nunca:
- ❌ Commitar direto em PROD (`/workspace/AIOS`)
- ❌ Fazer pull de PROD para DEV (traz master para dev, inverte autoridade)
- ❌ Fazer push de DEV para PROD diretamente

**Why:** ADR-015 estabelece `/workspace/AIOS/Projects-dev/AIOS-dev-workspace/AIOS-dev` como source of truth. PROD (`/workspace/AIOS`) é cópia sincronizada. Violação inverte a cadeia de autoridade.

## Como aplicar

Ao fazer mudanças em AIOS meta-system (hooks, commands, guides, skills):

1. **Editar em DEV**
   ```bash
   # Editar arquivos em:
   /workspace/AIOS/Projects-dev/AIOS-dev-workspace/AIOS-dev/.claude/hooks/
   /workspace/AIOS/Projects-dev/AIOS-dev-workspace/AIOS-dev/.claude/commands/
   /workspace/AIOS/Projects-dev/AIOS-dev-workspace/AIOS-dev/.claude/skills/
   ```

2. **Commit & Push em DEV**
   ```bash
   git -C /workspace/AIOS/Projects-dev/AIOS-dev-workspace/AIOS-dev add -u
   git -C /workspace/AIOS/Projects-dev/AIOS-dev-workspace/AIOS-dev commit -m "..."
   git -C /workspace/AIOS/Projects-dev/AIOS-dev-workspace/AIOS-dev push origin HEAD:master
   ```

3. **Pull em PROD via aios-update** (usar skill `/aios-update`)
   - Faz pull de origin/master em PROD
   - Sincroniza tudo

4. **Nunca:**
   - Editar direto em `/workspace/AIOS/.claude/`
   - Fazer `git pull` em DEV depois de commits em PROD (inverte fluxo)

## Incidente

2026-03-18: Commitei `7999fbe feat: add tc-stop-hook implementation` direto em PROD, depois fiz pull em DEV. Resultado final foi correto (todos sincronizados), mas violou autoridade de DEV. Evitar repetir.
