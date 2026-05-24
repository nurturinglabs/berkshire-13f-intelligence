# Berkshire 13F Intelligence

Institutional portfolio analytics built on Berkshire Hathaway's public
SEC 13F-HR filings — 8 quarters of drift, concentration, and sector rotation analysis.

**Stack:** SEC EDGAR → Python → Snowflake → dbt → Streamlit

**Live data:**
- 901 holdings across 8 quarters (Q2 2024 – Q1 2026)
- CIK: 0001067983 (Berkshire Hathaway Inc)
- dbt pipeline: staging → intermediate → 4 mart tables

## Deploy on Streamlit Community Cloud

1. Fork this repo
2. Go to share.streamlit.io
3. Connect your GitHub account
4. Select this repo and `app.py`
5. Add secrets in the Streamlit Cloud dashboard:
```toml
[snowflake]
account   = "your-account"
user      = "your-user"
password  = "your-password"
warehouse = "NM_WH"
database  = "BERKSHIRE_ANALYTICS"
schema    = "RAW_MARTS"
role      = "SYSADMIN"
```
