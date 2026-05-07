# GitHub Actions для запису в Google Таблицю

Цей workflow автоматизує **запис готового CSV** у Google Таблицю через Apps Script.

Він **ще не збирає ціни самостійно**. Його завдання зараз:
- взяти файл `output/monitoring-*.csv`;
- відправити рядки у ваш Apps Script вебхук;
- дати стабільний запис без попапа Google Drive connector.

## Файли

- Workflow: `.github/workflows/send-monitoring-to-apps-script.yml`
- Клієнт відправки: `scripts/send_monitoring_to_apps_script.py`

## Що треба зробити в GitHub

1. Створити репозиторій або відкрити існуючий.
2. Завантажити в нього:
   - `.github/workflows/send-monitoring-to-apps-script.yml`
   - `scripts/send_monitoring_to_apps_script.py`
   - ваші CSV у папку `output/`
3. У репозиторії відкрити:
   `Settings` -> `Secrets and variables` -> `Actions`
4. Додати два `Repository secrets`:
   - `APPS_SCRIPT_WEBHOOK_URL`
   - `APPS_SCRIPT_SHARED_SECRET`

## Значення секретів

`APPS_SCRIPT_WEBHOOK_URL`

```text
https://script.google.com/macros/s/AKfycbxa2MVo47OEX_5hDbajmnvQ2mQ_xsQTgFoQOni3aHLFDaTY0l77knRMfg-CNUoyjZjr1A/exec
```

`APPS_SCRIPT_SHARED_SECRET`

```text
MFtsg322c6fKVm_bBZup95VOmimvSNjZzxkyGHVWzos
```

## Як запустити вручну

1. Відкрити вкладку `Actions`
2. Обрати workflow `Send Monitoring CSV To Apps Script`
3. Натиснути `Run workflow`
4. За потреби вказати `csv_path`, наприклад:

```text
output/monitoring-2026-05-07.csv
```

## Як працює запуск за розкладом

У workflow вже стоїть cron:

```text
15 6 * * *
```

Це `06:15 UTC` щодня.

Для Києва це:
- `09:15` під час літнього часу
- `08:15` під час зимового часу

## Важливо

Якщо у репозиторії не з’являтиметься новий `output/monitoring-*.csv`, workflow просто відправлятиме останній наявний файл. Дублікатів у таблиці не буде, бо Apps Script уже перевіряє пару `дата + найменування`.
