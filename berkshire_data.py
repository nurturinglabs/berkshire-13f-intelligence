"""
berkshire_data.py
Sample Berkshire 13F data for immediate demo.
Replace with live Snowflake queries once dbt pipeline is running.
"""

QUARTERS = ["Q4 2024","Q3 2024","Q2 2024","Q1 2024","Q4 2023","Q3 2023","Q2 2023","Q1 2023"]

HOLDINGS = [
    # Q4 2024
    {"quarter":"Q4 2024","filing_date":"2025-02-14","issuer_name":"Apple Inc","sector":"Information Technology","value_usd":74850000000,"value_000s":74850000,"pct_of_portfolio":28.1,"holding_rank":1,"drift_flag":"REDUCED","value_change_usd":-5200000000},
    {"quarter":"Q4 2024","filing_date":"2025-02-14","issuer_name":"American Express","sector":"Financials","value_usd":41100000000,"value_000s":41100000,"pct_of_portfolio":15.4,"holding_rank":2,"drift_flag":"INCREASED","value_change_usd":3100000000},
    {"quarter":"Q4 2024","filing_date":"2025-02-14","issuer_name":"Bank of America","sector":"Financials","value_usd":31700000000,"value_000s":31700000,"pct_of_portfolio":11.9,"holding_rank":3,"drift_flag":"REDUCED","value_change_usd":-2800000000},
    {"quarter":"Q4 2024","filing_date":"2025-02-14","issuer_name":"Coca-Cola","sector":"Consumer Staples","value_usd":24100000000,"value_000s":24100000,"pct_of_portfolio":9.1,"holding_rank":4,"drift_flag":"UNCHANGED","value_change_usd":0},
    {"quarter":"Q4 2024","filing_date":"2025-02-14","issuer_name":"Chevron","sector":"Energy","value_usd":17500000000,"value_000s":17500000,"pct_of_portfolio":6.6,"holding_rank":5,"drift_flag":"REDUCED","value_change_usd":-1200000000},
    {"quarter":"Q4 2024","filing_date":"2025-02-14","issuer_name":"Occidental Petroleum","sector":"Energy","value_usd":13200000000,"value_000s":13200000,"pct_of_portfolio":5.0,"holding_rank":6,"drift_flag":"INCREASED","value_change_usd":800000000},
    {"quarter":"Q4 2024","filing_date":"2025-02-14","issuer_name":"Kraft Heinz","sector":"Consumer Staples","value_usd":10900000000,"value_000s":10900000,"pct_of_portfolio":4.1,"holding_rank":7,"drift_flag":"UNCHANGED","value_change_usd":0},
    {"quarter":"Q4 2024","filing_date":"2025-02-14","issuer_name":"Moodys Corp","sector":"Financials","value_usd":9800000000,"value_000s":9800000,"pct_of_portfolio":3.7,"holding_rank":8,"drift_flag":"INCREASED","value_change_usd":600000000},
    {"quarter":"Q4 2024","filing_date":"2025-02-14","issuer_name":"DaVita Inc","sector":"Health Care","value_usd":5200000000,"value_000s":5200000,"pct_of_portfolio":2.0,"holding_rank":9,"drift_flag":"UNCHANGED","value_change_usd":0},
    {"quarter":"Q4 2024","filing_date":"2025-02-14","issuer_name":"VeriSign","sector":"Information Technology","value_usd":3100000000,"value_000s":3100000,"pct_of_portfolio":1.2,"holding_rank":10,"drift_flag":"UNCHANGED","value_change_usd":0},
    {"quarter":"Q4 2024","filing_date":"2025-02-14","issuer_name":"Charter Communications","sector":"Communication Services","value_usd":2800000000,"value_000s":2800000,"pct_of_portfolio":1.1,"holding_rank":11,"drift_flag":"REDUCED","value_change_usd":-300000000},
    {"quarter":"Q4 2024","filing_date":"2025-02-14","issuer_name":"Chubb Ltd","sector":"Financials","value_usd":6900000000,"value_000s":6900000,"pct_of_portfolio":2.6,"holding_rank":12,"drift_flag":"NEW","value_change_usd":6900000000},
    {"quarter":"Q4 2024","filing_date":"2025-02-14","issuer_name":"US Bancorp","sector":"Financials","value_usd":2400000000,"value_000s":2400000,"pct_of_portfolio":0.9,"holding_rank":13,"drift_flag":"UNCHANGED","value_change_usd":0},
    {"quarter":"Q4 2024","filing_date":"2025-02-14","issuer_name":"BYD Co Ltd","sector":"Consumer Discretionary","value_usd":3200000000,"value_000s":3200000,"pct_of_portfolio":1.2,"holding_rank":14,"drift_flag":"UNCHANGED","value_change_usd":0},
    {"quarter":"Q4 2024","filing_date":"2025-02-14","issuer_name":"HP Inc","sector":"Information Technology","value_usd":3700000000,"value_000s":3700000,"pct_of_portfolio":1.4,"holding_rank":15,"drift_flag":"INCREASED","value_change_usd":400000000},
    # Q3 2024
    {"quarter":"Q3 2024","filing_date":"2024-11-14","issuer_name":"Apple Inc","sector":"Information Technology","value_usd":80050000000,"value_000s":80050000,"pct_of_portfolio":29.5,"holding_rank":1,"drift_flag":"REDUCED","value_change_usd":-15000000000},
    {"quarter":"Q3 2024","filing_date":"2024-11-14","issuer_name":"American Express","sector":"Financials","value_usd":38000000000,"value_000s":38000000,"pct_of_portfolio":14.0,"holding_rank":2,"drift_flag":"INCREASED","value_change_usd":2000000000},
    {"quarter":"Q3 2024","filing_date":"2024-11-14","issuer_name":"Bank of America","sector":"Financials","value_usd":34500000000,"value_000s":34500000,"pct_of_portfolio":12.7,"holding_rank":3,"drift_flag":"UNCHANGED","value_change_usd":0},
    {"quarter":"Q3 2024","filing_date":"2024-11-14","issuer_name":"Coca-Cola","sector":"Consumer Staples","value_usd":23400000000,"value_000s":23400000,"pct_of_portfolio":8.6,"holding_rank":4,"drift_flag":"UNCHANGED","value_change_usd":0},
    {"quarter":"Q3 2024","filing_date":"2024-11-14","issuer_name":"Chevron","sector":"Energy","value_usd":18700000000,"value_000s":18700000,"pct_of_portfolio":6.9,"holding_rank":5,"drift_flag":"UNCHANGED","value_change_usd":0},
    {"quarter":"Q3 2024","filing_date":"2024-11-14","issuer_name":"Occidental Petroleum","sector":"Energy","value_usd":12400000000,"value_000s":12400000,"pct_of_portfolio":4.6,"holding_rank":6,"drift_flag":"INCREASED","value_change_usd":1200000000},
    {"quarter":"Q3 2024","filing_date":"2024-11-14","issuer_name":"Kraft Heinz","sector":"Consumer Staples","value_usd":11200000000,"value_000s":11200000,"pct_of_portfolio":4.1,"holding_rank":7,"drift_flag":"UNCHANGED","value_change_usd":0},
    {"quarter":"Q3 2024","filing_date":"2024-11-14","issuer_name":"Moodys Corp","sector":"Financials","value_usd":9200000000,"value_000s":9200000,"pct_of_portfolio":3.4,"holding_rank":8,"drift_flag":"UNCHANGED","value_change_usd":0},
    # Q2 2024
    {"quarter":"Q2 2024","filing_date":"2024-08-14","issuer_name":"Apple Inc","sector":"Information Technology","value_usd":95300000000,"value_000s":95300000,"pct_of_portfolio":42.9,"holding_rank":1,"drift_flag":"REDUCED","value_change_usd":-20000000000},
    {"quarter":"Q2 2024","filing_date":"2024-08-14","issuer_name":"Bank of America","sector":"Financials","value_usd":34800000000,"value_000s":34800000,"pct_of_portfolio":15.7,"holding_rank":2,"drift_flag":"UNCHANGED","value_change_usd":0},
    {"quarter":"Q2 2024","filing_date":"2024-08-14","issuer_name":"American Express","sector":"Financials","value_usd":36000000000,"value_000s":36000000,"pct_of_portfolio":16.2,"holding_rank":3,"drift_flag":"UNCHANGED","value_change_usd":0},
    {"quarter":"Q2 2024","filing_date":"2024-08-14","issuer_name":"Coca-Cola","sector":"Consumer Staples","value_usd":23700000000,"value_000s":23700000,"pct_of_portfolio":10.7,"holding_rank":4,"drift_flag":"UNCHANGED","value_change_usd":0},
    {"quarter":"Q2 2024","filing_date":"2024-08-14","issuer_name":"Chevron","sector":"Energy","value_usd":18600000000,"value_000s":18600000,"pct_of_portfolio":8.4,"holding_rank":5,"drift_flag":"UNCHANGED","value_change_usd":0},
    # Q1 2024
    {"quarter":"Q1 2024","filing_date":"2024-05-15","issuer_name":"Apple Inc","sector":"Information Technology","value_usd":135400000000,"value_000s":135400000,"pct_of_portfolio":40.8,"holding_rank":1,"drift_flag":"UNCHANGED","value_change_usd":0},
    {"quarter":"Q1 2024","filing_date":"2024-05-15","issuer_name":"Bank of America","sector":"Financials","value_usd":39200000000,"value_000s":39200000,"pct_of_portfolio":11.8,"holding_rank":2,"drift_flag":"UNCHANGED","value_change_usd":0},
    {"quarter":"Q1 2024","filing_date":"2024-05-15","issuer_name":"American Express","sector":"Financials","value_usd":34500000000,"value_000s":34500000,"pct_of_portfolio":10.4,"holding_rank":3,"drift_flag":"UNCHANGED","value_change_usd":0},
    {"quarter":"Q1 2024","filing_date":"2024-05-15","issuer_name":"Coca-Cola","sector":"Consumer Staples","value_usd":25100000000,"value_000s":25100000,"pct_of_portfolio":7.6,"holding_rank":4,"drift_flag":"UNCHANGED","value_change_usd":0},
    {"quarter":"Q1 2024","filing_date":"2024-05-15","issuer_name":"Chevron","sector":"Energy","value_usd":19400000000,"value_000s":19400000,"pct_of_portfolio":5.8,"holding_rank":5,"drift_flag":"UNCHANGED","value_change_usd":0},
]

CONCENTRATION_DATA = [
    {"quarter":"Q1 2023","filing_date":"2023-05-15","top_1_pct":38.9,"top_3_pct":64.2,"top_5_pct":72.1,"top_10_pct":84.3,"top_20_pct":93.1,"hhi_score":2180,"total_value_usd":295000000000,"total_holdings":47},
    {"quarter":"Q2 2023","filing_date":"2023-08-14","top_1_pct":45.2,"top_3_pct":67.8,"top_5_pct":75.4,"top_10_pct":86.2,"top_20_pct":94.0,"hhi_score":2540,"total_value_usd":318000000000,"total_holdings":46},
    {"quarter":"Q3 2023","filing_date":"2023-11-14","top_1_pct":48.1,"top_3_pct":70.2,"top_5_pct":77.9,"top_10_pct":87.8,"top_20_pct":94.8,"hhi_score":2820,"total_value_usd":322000000000,"total_holdings":45},
    {"quarter":"Q4 2023","filing_date":"2024-02-14","top_1_pct":50.2,"top_3_pct":72.1,"top_5_pct":79.4,"top_10_pct":89.1,"top_20_pct":95.6,"hhi_score":3050,"total_value_usd":354000000000,"total_holdings":45},
    {"quarter":"Q1 2024","filing_date":"2024-05-15","top_1_pct":40.8,"top_3_pct":63.0,"top_5_pct":71.4,"top_10_pct":83.9,"top_20_pct":93.2,"hhi_score":2310,"total_value_usd":331000000000,"total_holdings":44},
    {"quarter":"Q2 2024","filing_date":"2024-08-14","top_1_pct":42.9,"top_3_pct":74.8,"top_5_pct":82.1,"top_10_pct":91.4,"top_20_pct":96.8,"hhi_score":2680,"total_value_usd":280000000000,"total_holdings":42},
    {"quarter":"Q3 2024","filing_date":"2024-11-14","top_1_pct":29.5,"top_3_pct":56.2,"top_5_pct":65.8,"top_10_pct":79.4,"top_20_pct":91.2,"hhi_score":1820,"total_value_usd":271000000000,"total_holdings":43},
    {"quarter":"Q4 2024","filing_date":"2025-02-14","top_1_pct":28.1,"top_3_pct":55.4,"top_5_pct":66.1,"top_10_pct":80.2,"top_20_pct":92.1,"hhi_score":1750,"total_value_usd":266000000000,"total_holdings":44},
]

SECTOR_DATA = []
sector_weights = {
    "Q1 2023": {"Financials":28.1,"Information Technology":38.9,"Consumer Staples":18.2,"Energy":8.4,"Consumer Discretionary":3.1,"Communication Services":1.8,"Health Care":1.5},
    "Q2 2023": {"Financials":25.4,"Information Technology":45.2,"Consumer Staples":16.8,"Energy":7.9,"Consumer Discretionary":2.8,"Communication Services":1.2,"Health Care":0.7},
    "Q3 2023": {"Financials":23.8,"Information Technology":48.1,"Consumer Staples":15.9,"Energy":7.2,"Consumer Discretionary":2.9,"Communication Services":1.4,"Health Care":0.7},
    "Q4 2023": {"Financials":24.1,"Information Technology":50.2,"Consumer Staples":15.2,"Energy":6.8,"Consumer Discretionary":2.2,"Communication Services":1.0,"Health Care":0.5},
    "Q1 2024": {"Financials":26.2,"Information Technology":40.8,"Consumer Staples":18.0,"Energy":8.2,"Consumer Discretionary":3.8,"Communication Services":1.5,"Health Care":1.5},
    "Q2 2024": {"Financials":34.2,"Information Technology":42.9,"Consumer Staples":15.3,"Energy":4.2,"Consumer Discretionary":2.1,"Communication Services":0.8,"Health Care":0.5},
    "Q3 2024": {"Financials":33.8,"Information Technology":29.5,"Consumer Staples":12.7,"Energy":11.5,"Consumer Discretionary":8.4,"Communication Services":2.8,"Health Care":1.3},
    "Q4 2024": {"Financials":33.6,"Information Technology":30.7,"Consumer Staples":13.2,"Energy":11.6,"Consumer Discretionary":7.2,"Communication Services":2.2,"Health Care":1.5},
}

for q, sectors in sector_weights.items():
    for sector, pct in sectors.items():
        SECTOR_DATA.append({
            "quarter": q,
            "sector":  sector,
            "sector_pct": pct,
            "sector_value_usd": pct * 2700000000,
        })
