# Stage 00 — Repository Baseline and Governance Structure

## 1. Цель задания

Создать базовую структуру репозитория проекта сетевого доступа через российский и зарубежный egress, настроить правила размещения артефактов, подготовить шаблоны стадий и обеспечить возможность внешнего аудита всех последующих изменений.

Репозиторий:

```text
https://github.com/dedvmedved-dot/hiddify-architecture
```

Рабочая ветка:

```text
main
```

На данном этапе запрещено:

* разрабатывать окончательную архитектуру;
* настраивать MikroTik;
* изменять VPS;
* размещать реальные рабочие конфигурации;
* размещать секреты;
* объявлять архитектуру принятой;
* начинать Stage 01.

## 2. Критические требования к поведению Hermes + Qwen 3.7 Max

1. Работать только с репозиторием:

   ```text
   dedvmedved-dot/hiddify-architecture
   ```

2. Перед началом проверить:

   ```bash
   git remote -v
   git status
   git branch --show-current
   ```

3. Не выполнять force push.

4. Не переписывать историю Git.

5. Не добавлять реальные:

   * пароли;
   * токены;
   * приватные ключи;
   * SSH host keys;
   * WireGuard private keys;
   * cookies;
   * session files;
   * `.env`;
   * резервные копии MikroTik;
   * экспорт конфигурации с секретами.

6. Все примеры секретов записывать только в формате:

   ```text
   <REPLACE_WITH_SECRET>
   ```

7. Не копировать автоматически исходную концепцию в качестве утвержденной архитектуры.

8. Любой документ, который еще не содержит подтвержденных данных, должен явно иметь статус:

   ```text
   DRAFT
   ```

9. Все Markdown-файлы должны быть в UTF-8 и заканчиваться переводом строки.

10. Не создавать каталоги и файлы за пределами согласованной структуры без отдельного обоснования в отчете.

11. Не выдавать статус `PASSED`. Статус этапа присваивает только внешний аудитор ChatGPT после проверки commit через GitHub connector.

## 3. Требуемая структура

Создать следующую структуру:

```text
README.md
LICENSE
CHANGELOG.md
CONTRIBUTING.md
SECURITY.md
.gitignore
.editorconfig
.gitattributes
Makefile

docs/
  README.md
  project/
    project-charter.md
    scope.md
    roles-and-responsibilities.md
    stage-gates.md
    definition-of-done.md
    terminology.md
  requirements/
    functional-requirements.md
    non-functional-requirements.md
    constraints.md
    assumptions.md
    traceability-matrix.md
  architecture/
    system-context.md
    logical-architecture.md
    physical-architecture.md
    network-flows.md
    addressing-plan.md
    routing-policy.md
    dns-architecture.md
    security-architecture.md
    availability-architecture.md
    candidate-solutions.md
  decisions/
    README.md
    ADR-000-template.md
  audit/
    README.md
    initial-concept.md
  testing/
    test-strategy.md
    test-environments.md
    acceptance-criteria.md
    test-case-template.md
  operations/
    deployment-guide.md
    operations-guide.md
    monitoring-guide.md
    backup-and-restore.md
    rollback-guide.md
    incident-response.md
    troubleshooting.md
  security/
    threat-model.md
    secret-management.md
    hardening-standard.md
    firewall-policy.md
    logging-policy.md
    security-test-plan.md

stages/
  README.md
  stage-00-repository-baseline/
    task.md
    report.md
    acceptance.md
    evidence-index.md
  templates/
    task-template.md
    report-template.md
    acceptance-template.md
    evidence-index-template.md

configs/
  README.md
  mikrotik/
    templates/
    generated/
  vps1/
    templates/
    generated/
  vps3/
    templates/
    generated/
  nftables/
  routing/
  dns/
  systemd/
  monitoring/

scripts/
  README.md
  bootstrap/
  deploy/
  validation/
  testing/
  rollback/
  inventory/
  security/

inventory/
  README.md
  templates/
  mikrotik/
  vps1/
  vps3/

tests/
  README.md
  static/
  functional/
  integration/
  performance/
  resilience/
  security/
  acceptance/

evidence/
  README.md

reports/
  README.md
  audit/
  testing/
  performance/
  security/
  acceptance/

diagrams/
  README.md
  source/
  rendered/

tools/
  README.md
  lint/
  validation/

.github/
  CODEOWNERS
  pull_request_template.md
  ISSUE_TEMPLATE/
    bug-report.yml
    architecture-change.yml
    test-failure.yml
  workflows/
    markdown-lint.yml
    shellcheck.yml
    secret-scan.yml
    repository-validation.yml
```

Во все каталоги, которые иначе останутся пустыми, добавить `.gitkeep`.

## 4. Назначение основных каталогов

### `docs/`

Содержит утверждаемую проектную документацию.

Не размещать здесь:

* сырые логи;
* выводы команд;
* бинарные evidence;
* временные файлы.

### `stages/`

Содержит задания, отчеты и решения о приемке по каждой стадии.

Для каждой стадии использовать структуру:

```text
stages/stage-NN-name/
  task.md
  report.md
  acceptance.md
  evidence-index.md
```

### `configs/`

Содержит шаблоны и обезличенные конфигурации.

Правила:

* `templates/` — шаблоны с placeholders;
* `generated/` — сгенерированные, но очищенные конфигурации;
* реальные секреты запрещены;
* production backup-файлы запрещены.

### `scripts/`

Содержит только исполняемые или библиотечные скрипты проекта.

Каждый shell-скрипт в дальнейшем должен:

* использовать `#!/usr/bin/env bash`;
* по возможности использовать `set -Eeuo pipefail`;
* возвращать ненулевой exit code при ошибке;
* иметь комментарий о назначении;
* проходить ShellCheck.

### `inventory/`

Содержит только очищенные технические сведения об узлах.

### `tests/`

Содержит тестовые сценарии и автоматизацию тестов.

### `evidence/`

Содержит неизмененные либо минимально обработанные доказательства выполнения конкретной стадии.

Каждый будущий этап должен использовать:

```text
evidence/stage-NN/
```

### `reports/`

Содержит итоговые и сводные отчеты, которые могут ссылаться на evidence.

### `diagrams/source/`

Исходники Mermaid, PlantUML, Graphviz или draw.io.

### `diagrams/rendered/`

Рендерированные SVG/PNG/PDF, если они создаются автоматически.

## 5. Обязательное содержимое корневых файлов

### `README.md`

Включить:

* название проекта;
* статус `DRAFT`;
* цель проекта;
* краткое описание исходной задачи;
* предупреждение, что архитектура пока не утверждена;
* роли ChatGPT и Hermes + Qwen;
* описание stage-gate процесса;
* карту каталогов;
* правила перехода к следующей стадии;
* ссылку на `stages/stage-00-repository-baseline/report.md`.

Не утверждать, что Hiddify обязательно будет частью финального решения. Название репозитория не является архитектурным решением.

### `CHANGELOG.md`

Использовать формат Keep a Changelog.

Начальная версия:

```text
[Unreleased]

- Repository baseline created.
```

### `CONTRIBUTING.md`

Зафиксировать:

* именование веток;
* требования к commit messages;
* запрет секретов;
* правила evidence;
* правила изменений архитектуры;
* требование внешнего аудита перед началом новой стадии.

Рекомендуемое именование веток:

```text
stage/NN-short-name
fix/short-description
docs/short-description
```

Для Stage 00 допускается commit непосредственно в `main`, поскольку репозиторий пуст. Начиная со следующей стадии использовать отдельные ветки и pull requests, если это технически возможно.

### `SECURITY.md`

Включить:

* запрет публикации секретов;
* процедуру удаления случайно опубликованного секрета;
* требование немедленной ротации;
* правила sanitization;
* допустимые placeholders;
* правила хранения evidence.

### `.gitignore`

Минимально исключить:

```gitignore
.env
.env.*
!.env.example

*.key
*.pem
*.p12
*.pfx
*.ovpn
*.mobileconfig

id_rsa
id_rsa.*
id_ed25519
id_ed25519.*

*.backup
*.backup.*
*.rsc.private
*.secret
*.secrets

secrets/
private/
credentials/

*.log
tmp/
.cache/
__pycache__/
.pytest_cache/

.DS_Store
Thumbs.db
.idea/
.vscode/
```

Не игнорировать все файлы `.rsc`, потому что очищенные MikroTik templates будут храниться в репозитории.

### `.editorconfig`

Задать:

* UTF-8;
* LF;
* final newline;
* удаление trailing whitespace;
* Markdown trailing spaces не удалять, если они используются для line breaks;
* отступ по умолчанию 2 пробела;
* shell-файлы — 2 пробела.

### `.gitattributes`

Минимально:

```gitattributes

* text=auto eol=lf
*.sh text eol=lf
*.md text eol=lf
*.yml text eol=lf
*.yaml text eol=lf
*.rsc text eol=lf
*.svg text eol=lf
```

### `LICENSE`

Использовать лицензию MIT, если владелец репозитория ранее не установил другую лицензию.

В отчете явно отметить выбор MIT как первоначальное решение, подлежащее пересмотру владельцем.

## 6. Обязательные документы управления проектом

### `docs/project/roles-and-responsibilities.md`

Зафиксировать:

#### ChatGPT

* ведущий архитектор;
* критик;
* постановщик задач;
* внешний аудитор;
* authority по stage acceptance.

#### Hermes + Qwen 3.7 Max

* реализация;
* сбор evidence;
* создание конфигураций;
* тестирование;
* создание отчетов;
* commit и push.

#### Owner

* предоставляет доступ;
* передает задания Hermes;
* предоставляет исходные данные;
* передает commit hash;
* принимает бизнес-решения;
* разрешает изменения production.

Зафиксировать:

```text
Hermes + Qwen не имеет права самостоятельно присваивать стадии статус PASSED.
```

### `docs/project/stage-gates.md`

Определить статусы:

```text
NOT STARTED
IN PROGRESS
READY FOR EXTERNAL AUDIT
FAILED
CONDITIONAL PASS
PASSED
CONNECTOR VERIFIED
```

Переход к следующей стадии допускается только после:

```text
PASSED / CONNECTOR VERIFIED
```

### `docs/project/definition-of-done.md`

Включить минимум:

* файлы находятся в заданных путях;
* документы не противоречат друг другу;
* конфигурации не содержат секретов;
* тесты воспроизводимы;
* evidence доступно;
* SHA-256 checksums созданы, когда применимо;
* отчет ссылается на evidence;
* commit доступен через GitHub;
* внешний аудит завершен.

## 7. Шаблоны стадий

### `stages/templates/task-template.md`

Обязательные секции:

1. Цель стадии.
2. Исходные данные.
3. Критические требования к поведению Hermes + Qwen.
4. Scope.
5. Out of scope.
6. Требуемые действия.
7. Куда размещать каждый файл.
8. Требования к evidence.
9. Требования безопасности.
10. Тесты.
11. Критерии приемки.
12. Что вернуть внешнему аудитору.
13. Запрет самостоятельного `PASSED`.

### `stages/templates/report-template.md`

Обязательные секции:

* Summary;
* Changes made;
* Files created;
* Commands executed;
* Test results;
* Evidence;
* Deviations;
* Known issues;
* Risks;
* Rollback information;
* Secret scan;
* Commit information;
* Readiness statement.

### `stages/templates/acceptance-template.md`

Содержит поля:

```text
Stage:
Commit:
Audit date:
Auditor:
Result:
Blocking findings:
Non-blocking findings:
Required corrections:
Connector verification:
```

Поле `Result` Hermes не заполняет.

### `stages/templates/evidence-index-template.md`

Таблица:

| Evidence ID | File | Host | Command/Test | Timestamp UTC | SHA-256 | Sanitized | Description |
| ----------- | ---- | ---- | ------------ | ------------- | ------- | --------- | ----------- |

## 8. Stage 00 files

### `stages/stage-00-repository-baseline/task.md`

Сохранить полный текст данного задания.

Допускается удаление только служебных фраз, не относящихся к заданию. Требования, пути и критерии приемки сокращать запрещено.

### `stages/stage-00-repository-baseline/report.md`

Указать:

* UTC-время начала и завершения;
* локальный путь клона;
* исходное состояние репозитория;
* созданные файлы и каталоги;
* результаты проверок;
* отступления от задания;
* результаты secret scan;
* commit hash;
* tree listing;
* известные ограничения.

### `stages/stage-00-repository-baseline/acceptance.md`

Создать, но оставить:

```text
Result: PENDING EXTERNAL AUDIT
Connector verification: PENDING
```

### `stages/stage-00-repository-baseline/evidence-index.md`

Сослаться минимум на:

```text
evidence/stage-00/repository-tree.txt
evidence/stage-00/git-status.txt
evidence/stage-00/git-log.txt
evidence/stage-00/markdown-files.txt
evidence/stage-00/secret-scan.txt
evidence/stage-00/validation.txt
evidence/stage-00/checksums.sha256
```

## 9. Evidence Stage 00

Создать каталог:

```text
evidence/stage-00/
```

Сохранить:

### `repository-tree.txt`

Полный список файлов:

```bash
find . -type f \
  -not -path './.git/*' \
  -print | LC_ALL=C sort
```

### `git-status.txt`

```bash
git status --short
git status --branch
```

Файл должен отражать чистое состояние после commit.

Если evidence собирается до commit, повторить команду после commit и записать финальное состояние.

### `git-log.txt`

После commit:

```bash
git log -1 --decorate --stat
git show --summary --format=fuller HEAD
```

### `markdown-files.txt`

```bash
find . -type f -name '*.md' \
  -not -path './.git/*' \
  -print | LC_ALL=C sort
```

### `secret-scan.txt`

Выполнить минимум:

```bash
grep -RniE \
  --exclude-dir=.git \
  --exclude='secret-scan.txt' \
  '(BEGIN [A-Z ]*PRIVATE KEY|password[[:space:]]*=|token[[:space:]]*=|secret[[:space:]]*=|api[_-]?key[[:space:]]*=)' \
  . || true
```

Если доступен Gitleaks:

```bash
gitleaks detect --source . --no-git --redact
```

Сохранить:

* команду;
* версию инструмента;
* exit code;
* результат;
* объяснение каждого false positive.

### `validation.txt`

Выполнить и сохранить результаты:

```bash
git diff --check HEAD^ HEAD
find . -type f -empty -not -path './.git/*' -print
find . -type f -name '*.sh' -not -path './.git/*' -print
find . -type f -name '*.md' -not -path './.git/*' -print | wc -l
```

Если `HEAD^` отсутствует из-за первого commit, вместо первой команды выполнить:

```bash
git show --check HEAD
```

Проверить отсутствие запрещенных имен:

```bash
find . -type f \
  \( -name '*.key' -o -name '*.pem' -o -name '*.p12' \
     -o -name '*.pfx' -o -name '.env' -o -name '*.backup' \) \
  -not -path './.git/*' -print
```

### `checksums.sha256`

Создать после подготовки остальных evidence:

```bash
find evidence/stage-00 -type f \
  ! -name 'checksums.sha256' \
  -print0 |
  LC_ALL=C sort -z |
  xargs -0 sha256sum > evidence/stage-00/checksums.sha256
```

## 10. GitHub Actions

Создать минимальные workflow-файлы.

### `markdown-lint.yml`

Должен проверять Markdown через `markdownlint-cli2`.

### `shellcheck.yml`

Должен запускать ShellCheck только при наличии `.sh` файлов и не завершаться ошибкой из-за отсутствия скриптов.

### `secret-scan.yml`

Использовать Gitleaks либо эквивалентный scanner.

Не передавать секреты workflow в команды и не печатать GitHub token.

### `repository-validation.yml`

Проверять:

* обязательные корневые файлы;
* обязательные каталоги;
* отсутствие запрещенных файлов;
* отсутствие пустых Markdown-файлов;
* отсутствие trailing whitespace через `git diff --check` или аналог;
* наличие Stage 00 report;
* наличие Stage 00 evidence index.

Не добавлять actions с плавающим тегом `@master`.

Использовать закрепленные major versions или commit SHA. В отчете перечислить используемые сторонние actions.

## 11. Makefile

Реализовать безопасные targets:

```text
help
validate
lint-markdown
lint-shell
scan-secrets
tree
```

`make help` должен быть target по умолчанию.

Targets не должны изменять систему или устанавливать пакеты без явного согласия.

Если инструмент отсутствует, target должен:

* вывести понятное сообщение;
* вернуть ненулевой код для обязательной проверки;
* не выполнять скрытую установку.

## 12. Проверка структуры

Создать скрипт:

```text
tools/validation/validate-repository.sh
```

Скрипт должен:

* проверить обязательные файлы;
* проверить обязательные каталоги;
* проверить Stage 00 artifacts;
* проверить отсутствие запрещенных файлов;
* проверить отсутствие пустых Markdown-файлов;
* завершиться с `0` только при успешной проверке;
* печатать отдельный результат каждого check.

Скрипт должен быть исполняемым.

Запустить:

```bash
bash tools/validation/validate-repository.sh
```

Результат сохранить в:

```text
evidence/stage-00/validation.txt
```

## 13. Commit

Создать один логически цельный commit:

```text
chore(repo): establish project baseline and governance structure
```

Перед commit:

```bash
git status
git diff --check
```

После commit:

```bash
git status
git log -1 --oneline
```

Push:

```bash
git push origin main
```

Force push запрещен.

## 14. Критерии готовности к внешнему аудиту

Stage 00 готов к проверке только если:

1. Созданы все обязательные файлы и каталоги.
2. Пустые каталоги сохранены через `.gitkeep`.
3. Все Markdown-файлы непустые.
4. Корневой README описывает процесс stage-gate.
5. Роли участников явно определены.
6. Зафиксировано, что `PASSED` назначает только ChatGPT.
7. Созданы шаблоны будущих заданий и отчетов.
8. Созданы четыре GitHub Actions workflow.
9. Создан работающий repository validation script.
10. Secret scan не обнаруживает реальных секретов.
11. Evidence содержит полный список файлов.
12. Evidence содержит checksums.
13. Working tree после commit и push чистый.
14. Commit доступен в GitHub.
15. `acceptance.md` имеет статус `PENDING EXTERNAL AUDIT`.
16. Hermes не начал Stage 01.

## 15. Что вернуть для проверки

После push вернуть строго следующий блок:

```text
Stage: 00 — Repository Baseline
Repository: https://github.com/dedvmedved-dot/hiddify-architecture
Branch: main
Commit: <FULL_40_CHARACTER_COMMIT_SHA>
Commit URL: <URL>
Tree evidence: evidence/stage-00/repository-tree.txt
Stage report: stages/stage-00-repository-baseline/report.md
Acceptance file: stages/stage-00-repository-baseline/acceptance.md
Evidence index: stages/stage-00-repository-baseline/evidence-index.md
Validation evidence: evidence/stage-00/validation.txt
Secret scan evidence: evidence/stage-00/secret-scan.txt
Checksums: evidence/stage-00/checksums.sha256
GitHub Actions URLs:
- markdown-lint:
- shellcheck:
- secret-scan:
- repository-validation:
Deviations:
Known blockers:
```

Не присылать только сокращенный SHA.

Не присылать архив вместо commit.

Не объявлять:

```text
PASSED
CONNECTOR VERIFIED
ACCEPTED
```

После передачи данных остановить работу и ожидать внешнего аудита.
