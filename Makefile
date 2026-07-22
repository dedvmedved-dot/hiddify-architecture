# Hiddify Architecture Project - Makefile
# Safe targets that do not modify the system or install packages

.DEFAULT_GOAL := help

.PHONY: help validate lint-markdown lint-shell scan-secrets tree

help: ## Show this help message
	@echo "Hiddify Architecture Project - Available targets:"
	@echo ""
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2}'
	@echo ""
	@echo "Run 'make <target>' to execute."

validate: ## Validate repository structure
	@echo "Running repository validation..."
	@if [ -f "tools/validation/validate-repository.sh" ]; then \
		bash tools/validation/validate-repository.sh; \
	else \
		echo "ERROR: Validation script not found: tools/validation/validate-repository.sh"; \
		exit 1; \
	fi

lint-markdown: ## Lint Markdown files
	@echo "Linting Markdown files..."
	@if command -v markdownlint-cli2 >/dev/null 2>&1; then \
		markdownlint-cli2 "**/*.md" "!node_modules" "!*.template.md"; \
	elif command -v markdownlint >/dev/null 2>&1; then \
		markdownlint "**/*.md" --ignore node_modules; \
	else \
		echo "WARNING: markdownlint not installed. Install with: npm install -g markdownlint-cli2"; \
		echo "Skipping Markdown lint."; \
		exit 1; \
	fi

lint-shell: ## Lint shell scripts
	@echo "Linting shell scripts..."
	@if command -v shellcheck >/dev/null 2>&1; then \
		find . -type f -name "*.sh" -not -path "./.git/*" -exec shellcheck {} +; \
	else \
		echo "WARNING: shellcheck not installed. Install with: apt install shellcheck"; \
		echo "Skipping shell script lint."; \
		exit 1; \
	fi

scan-secrets: ## Scan for accidentally committed secrets
	@echo "Scanning for secrets..."
	@echo "Running grep-based scan..."
	@grep -RniE \
		--exclude-dir=.git \
		--exclude='secret-scan.txt' \
		'(BEGIN [A-Z ]*PRIVATE KEY|password[[:space:]]*=|token[[:space:]]*=|secret[[:space:]]*=|api[_-]?key[[:space:]]*=)' \
		. || echo "No obvious secrets found by grep scan."
	@echo ""
	@if command -v gitleaks >/dev/null 2>&1; then \
		echo "Running Gitleaks scan..."; \
		gitleaks detect --source . --no-git --redact; \
	else \
		echo "INFO: gitleaks not installed. Install from: https://github.com/gitleaks/gitleaks"; \
		echo "Only grep-based scan was performed."; \
	fi

tree: ## Show repository tree structure
	@echo "Repository structure:"
	@find . -type f -not -path './.git/*' -print | LC_ALL=C sort | head -100
	@echo ""
	@echo "Total files: $$(find . -type f -not -path './.git/*' | wc -l)"
	@echo "Total directories: $$(find . -type d -not -path './.git/*' | wc -l)"
