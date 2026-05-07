# Monotor_prace GitHub Bundle

Цей архів містить готовий мінімальний комплект для GitHub:
- GitHub Actions workflow для відправки CSV у Google Sheets через Apps Script
- Python-скрипт відправки
- Apps Script файли
- інструкції з налаштування
- приклад CSV

## Що додати в GitHub Secrets

- APPS_SCRIPT_WEBHOOK_URL
- APPS_SCRIPT_SHARED_SECRET

## Значення

APPS_SCRIPT_WEBHOOK_URL:
https://script.google.com/macros/s/AKfycbxa2MVo47OEX_5hDbajmnvQ2mQ_xsQTgFoQOni3aHLFDaTY0l77knRMfg-CNUoyjZjr1A/exec

APPS_SCRIPT_SHARED_SECRET:
MFtsg322c6fKVm_bBZup95VOmimvSNjZzxkyGHVWzos

## Структура

- .github/workflows/send-monitoring-to-apps-script.yml
- scripts/send_monitoring_to_apps_script.py
- apps-script/Code.gs
- apps-script/appsscript.json
- apps-script/README.md
- docs/github-actions-setup.md
- output/monitoring-2026-05-07.csv
