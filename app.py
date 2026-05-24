"""
Berkshire Hathaway 13F Portfolio Intelligence
Dark terminal theme — professional institutional analytics
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import snowflake.connector

@st.cache_resource
def get_connection():
    return snowflake.connector.connect(
        account   = st.secrets["snowflake"]["account"],
        user      = st.secrets["snowflake"]["user"],
        password  = st.secrets["snowflake"]["password"],
        warehouse = st.secrets["snowflake"]["warehouse"],
        database  = st.secrets["snowflake"]["database"],
        schema    = st.secrets["snowflake"]["schema"],
        role      = st.secrets["snowflake"]["role"],
    )

@st.cache_data(ttl=3600)
def run_query(sql):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(sql)
    cols = [d[0].lower() for d in cur.description]
    return pd.DataFrame(cur.fetchall(), columns=cols)

st.set_page_config(
    page_title="Berkshire 13F Intelligence",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Dark terminal CSS ──────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500&family=Inter:wght@400;500;600&display=swap');

html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
#MainMenu {visibility:hidden;} footer {visibility:hidden;} header {visibility:hidden;}
.stApp { background: #0E1117; }
.block-container { padding-top: 0.5rem !important; padding-bottom: 1rem !important; }
div[data-testid="stVerticalBlock"] > div { gap: 0.5rem !important; }
div[data-testid="element-container"] { margin: 0 !important; }

.term-header {
    background: #161B22;
    border: 1px solid #21262D;
    border-radius: 10px;
    padding: 14px 24px;
    margin-bottom: 14px;
}
.term-title {
    font-family: 'JetBrains Mono', monospace;
    font-size: 16px;
    font-weight: 500;
    color: #58A6FF;
    margin: 0;
    letter-spacing: 0.02em;
}
.term-sub { font-size: 11px; color: #6E7681; margin: 3px 0 0; font-family: 'JetBrains Mono', monospace; }

.kpi-terminal {
    background: #161B22;
    border: 1px solid #21262D;
    border-top: 2px solid;
    border-radius: 8px;
    padding: 14px 18px;
}
.kpi-label { font-size: 10px; color: #6E7681; text-transform: uppercase; letter-spacing: 0.1em; margin: 0 0 6px; font-family: 'JetBrains Mono', monospace; }
.kpi-value { font-family: 'JetBrains Mono', monospace; font-size: 24px; font-weight: 500; margin: 0 0 4px; }
.kpi-delta { font-size: 11px; margin: 0; color: #6E7681; font-family: 'JetBrains Mono', monospace; }

.card-terminal {
    background: #161B22;
    border: 1px solid #21262D;
    border-radius: 8px;
    padding: 16px 18px;
    margin-bottom: 12px;
}
.card-title {
    font-size: 11px;
    font-weight: 500;
    color: #C9D1D9;
    margin: 0 0 14px;
    font-family: 'JetBrains Mono', monospace;
    letter-spacing: 0.06em;
    text-transform: uppercase;
}

.tbl { width:100%; border-collapse:collapse; font-size:12px; font-family:'JetBrains Mono',monospace; }
.tbl th { padding:8px 12px; text-align:left; font-size:10px; color:#6E7681; text-transform:uppercase; letter-spacing:0.08em; border-bottom:1px solid #58A6FF55; font-weight:500; }
.tbl td { padding:8px 12px; border-bottom:1px solid #21262D; color:#C9D1D9; }
.tbl tr:hover td { background:#21262D88; }

.pill-new      { background:rgba(63,185,80,0.15);  color:#3FB950; font-size:10px; padding:2px 7px; border-radius:4px; font-family:'JetBrains Mono',monospace; }
.pill-increased{ background:rgba(88,166,255,0.15); color:#58A6FF; font-size:10px; padding:2px 7px; border-radius:4px; font-family:'JetBrains Mono',monospace; }
.pill-reduced  { background:rgba(210,153,34,0.15); color:#D29922; font-size:10px; padding:2px 7px; border-radius:4px; font-family:'JetBrains Mono',monospace; }
.pill-exited   { background:rgba(248,81,73,0.15);  color:#F85149; font-size:10px; padding:2px 7px; border-radius:4px; font-family:'JetBrains Mono',monospace; }
.pill-unchanged{ background:#21262D; color:#6E7681; font-size:10px; padding:2px 7px; border-radius:4px; font-family:'JetBrains Mono',monospace; }

::-webkit-scrollbar{width:4px} ::-webkit-scrollbar-track{background:#0E1117} ::-webkit-scrollbar-thumb{background:#21262D;border-radius:4px}

div[data-testid="stTabs"] button { font-family:'JetBrains Mono',monospace; font-size:12px; color:#6E7681 !important; }
div[data-testid="stTabs"] button[aria-selected="true"] { color:#58A6FF !important; }
div[data-baseweb="tab-highlight"] { background:#58A6FF !important; }
div[data-baseweb="tab-border"] { background:#21262D !important; }
</style>
""", unsafe_allow_html=True)

# ── Color palette ──────────────────────────────────────────────────────────────
C_CYAN    = "#58A6FF"
C_GREEN   = "#3FB950"
C_AMBER   = "#D29922"
C_RED     = "#F85149"
C_PURPLE  = "#7C3AED"
C_YELLOW  = "#E3B341"
C_GRAY    = "#6E7681"
BG_CARD   = "#161B22"
BG_MAIN   = "rgba(10,10,15,1)"
BORDER    = "#21262D"

SECTOR_COLORS = {
    "Financials":             C_CYAN,
    "Information Technology": C_GREEN,
    "Consumer Staples":       C_YELLOW,
    "Energy":                 C_AMBER,
    "Consumer Discretionary": C_PURPLE,
    "Communication Services": "#BC8CFF",
    "Health Care":            "#56D364",
    "Industrials":            "#E3B341",
    "Materials":              "#7C3AED",
    "Other":                  C_GRAY,
}

DRIFT_COLORS = {
    "NEW":       C_GREEN,
    "INCREASED": C_CYAN,
    "REDUCED":   C_AMBER,
    "EXITED":    C_RED,
    "UNCHANGED": C_GRAY,
}

def fmt_b(v):
    if v >= 1e9:  return f"${v/1e9:.2f}B"
    if v >= 1e6:  return f"${v/1e6:.0f}M"
    return f"${v:,.0f}"

def fmt_pct(v): return f"{v:.2f}%"

def plotly_dark_layout(height=320, margin=None):
    return dict(
        height=height,
        margin=margin or dict(l=0,r=20,t=20,b=0),
        paper_bgcolor='#161B22',
        plot_bgcolor='#161B22',
        font=dict(family='JetBrains Mono', color='#C9D1D9', size=11),
        xaxis=dict(showgrid=True, gridcolor='#21262D', color='#6E7681', zeroline=False),
        yaxis=dict(showgrid=True, gridcolor='#21262D', color='#6E7681', zeroline=False),
        legend=dict(bgcolor='#161B22', bordercolor='#21262D', font=dict(size=10)),
    )

# ── Load data from Snowflake ──────────────────────────────────────────────────
@st.cache_data(ttl=3600)
def load_snapshot():
    return run_query("""
        SELECT quarter, filing_date, issuer_name, cusip, sector, industry,
               CAST(value_usd AS FLOAT) AS value_usd,
               CAST(pct_of_portfolio AS FLOAT) AS pct_of_portfolio,
               holding_rank, drift_flag,
               CAST(value_change_usd AS FLOAT) AS value_change_usd,
               CAST(total_value_usd AS FLOAT) AS total_value_usd,
               total_holdings, is_top_5, is_top_10
        FROM BERKSHIRE_ANALYTICS.RAW_MARTS.MART_PORTFOLIO_SNAPSHOT
        ORDER BY holding_rank
    """).to_dict("records")

@st.cache_data(ttl=3600)
def load_all_holdings():
    return run_query("""
        SELECT quarter, filing_date, issuer_name, cusip, sector,
               CAST(value_usd AS FLOAT) AS value_usd,
               CAST(pct_of_portfolio AS FLOAT) AS pct_of_portfolio,
               holding_rank, drift_flag,
               CAST(value_change_usd AS FLOAT) AS value_change_usd
        FROM BERKSHIRE_ANALYTICS.RAW_MARTS.MART_DRIFT_ANALYSIS
        ORDER BY filing_date DESC, holding_rank
    """).to_dict("records")

@st.cache_data(ttl=3600)
def load_concentration():
    return run_query("""
        SELECT quarter, filing_date,
               CAST(top_1_pct AS FLOAT) AS top_1_pct,
               CAST(top_3_pct AS FLOAT) AS top_3_pct,
               CAST(top_5_pct AS FLOAT) AS top_5_pct,
               CAST(top_10_pct AS FLOAT) AS top_10_pct,
               CAST(top_20_pct AS FLOAT) AS top_20_pct,
               CAST(hhi_score AS FLOAT) AS hhi_score,
               CAST(total_value_usd AS FLOAT) AS total_value_usd,
               total_holdings
        FROM BERKSHIRE_ANALYTICS.RAW_MARTS.MART_CONCENTRATION_METRICS
        ORDER BY filing_date
    """).to_dict("records")

@st.cache_data(ttl=3600)
def load_sectors():
    return run_query("""
        SELECT quarter, filing_date, sector,
               CAST(sector_pct AS FLOAT) AS sector_pct,
               CAST(sector_value_usd AS FLOAT) AS sector_value_usd,
               holding_count, sector_rank
        FROM BERKSHIRE_ANALYTICS.RAW_MARTS.MART_SECTOR_ROTATION
        ORDER BY filing_date DESC, sector_pct DESC
    """).to_dict("records")

snapshot_holdings  = load_snapshot()
HOLDINGS           = load_all_holdings()
QUARTERS           = sorted(list(set(h["quarter"] for h in HOLDINGS)), reverse=True)
CONCENTRATION_DATA = load_concentration()
SECTOR_DATA        = load_sectors()

# ── Header ─────────────────────────────────────────────────────────────────────
latest_q  = QUARTERS[0] if QUARTERS else "Q1 2026"
latest_holdings_all = [h for h in HOLDINGS if h.get('quarter') == latest_q]
total_aum = sum(h.get("value_usd", 0) or 0 for h in snapshot_holdings) if snapshot_holdings else sum(h.get("value_usd", 0) or 0 for h in HOLDINGS if h.get("quarter") == latest_q)
total_pos = len(snapshot_holdings) if snapshot_holdings else len([h for h in HOLDINGS if h.get("quarter") == latest_q])
top_holding = sorted(snapshot_holdings or [h for h in HOLDINGS if h.get('quarter') == latest_q],
                      key=lambda x: x.get("value_usd", 0) or 0, reverse=True)[0] if (snapshot_holdings or HOLDINGS) else {}

st.markdown(f"""
<div class="term-header">
  <div style="display:flex;align-items:center;justify-content:space-between;">
    <div>
      <p class="term-title">▶ BERKSHIRE HATHAWAY — 13F PORTFOLIO INTELLIGENCE</p>
      <p class="term-sub">SEC EDGAR · 13F-HR · CIK: 0001067983 · {len(QUARTERS)} quarters · dbt + Snowflake</p>
    </div>
    <div style="display:flex;gap:10px;align-items:center;">
      <span style="background:rgba(63,185,80,0.15);color:#3FB950;font-size:10px;font-weight:500;padding:4px 10px;border-radius:4px;font-family:'JetBrains Mono',monospace;">● LIVE</span>
      <span style="background:rgba(88,166,255,0.15);color:#58A6FF;font-size:10px;padding:4px 10px;border-radius:4px;font-family:'JetBrains Mono',monospace;">Snowflake</span>
      <span style="background:#21262D;color:#4A5568;font-size:10px;padding:4px 10px;border-radius:4px;font-family:'JetBrains Mono',monospace;">dbt passing</span>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# ── KPI row ────────────────────────────────────────────────────────────────────
k1, k2, k3, k4 = st.columns(4)
kpis = [
    (k1, "PORTFOLIO AUM", fmt_b(total_aum), f"as of {latest_q}", C_CYAN),
    (k2, "EQUITY POSITIONS", str(total_pos), f"{len(QUARTERS)} quarters tracked", C_GREEN),
    (k3, "TOP HOLDING", top_holding.get("issuer_name","—")[:20], f"{fmt_pct(top_holding.get('pct_of_portfolio',0))} of portfolio", C_AMBER),
    (k4, "DATA QUARTERS", str(len(QUARTERS)), "13F-HR filings", C_PURPLE),
]
for col, label, value, delta, color in kpis:
    with col:
        st.markdown(f"""<div class="kpi-terminal" style="border-top-color:{color};">
            <p class="kpi-label">{label}</p>
            <p class="kpi-value" style="color:{color};">{value}</p>
            <p class="kpi-delta" style="color:{C_GRAY};">{delta}</p>
        </div>""", unsafe_allow_html=True)

st.markdown("<div style='height:4px'></div>", unsafe_allow_html=True)

# ── Tabs ───────────────────────────────────────────────────────────────────────
tab1, tab2, tab3, tab4 = st.tabs([
    "◉  Portfolio snapshot",
    "⟳  Portfolio drift",
    "◈  Concentration risk",
    "⬡  Sector rotation",
])

# ══════════════════════════════════════════════════════════════════════════════
# TAB 1 — PORTFOLIO SNAPSHOT
# ══════════════════════════════════════════════════════════════════════════════
with tab1:
    latest_holdings = sorted(
        snapshot_holdings or [h for h in HOLDINGS if h.get("quarter") == latest_q],
        key=lambda x: x.get("value_usd", 0) or 0, reverse=True
    )

    col_l, col_r = st.columns([3, 2])

    with col_l:
        st.markdown('<div class="card-terminal"><p class="card-title">TOP 20 HOLDINGS · ' + latest_q + '</p>', unsafe_allow_html=True)

        drift_pill = {
            "NEW":       '<span class="pill-new">NEW</span>',
            "INCREASED": '<span class="pill-increased">▲ INC</span>',
            "REDUCED":   '<span class="pill-reduced">▼ RED</span>',
            "EXITED":    '<span class="pill-exited">EXIT</span>',
            "UNCHANGED": '<span class="pill-unchanged">—</span>',
        }

        rows = ""
        for i, h in enumerate(latest_holdings[:20]):
            bg = f"background:#21262D44;" if i % 2 == 0 else ""
            drift = drift_pill.get(h.get("drift_flag","UNCHANGED"), "—")
            rows += f"""<tr style="{bg}">
                <td style="color:{C_GRAY};width:28px;">{h.get('holding_rank', i+1)}</td>
                <td style="color:#E8E8F0;font-weight:500;">{h['issuer_name'][:30]}</td>
                <td style="color:{C_GRAY};">{h.get('sector','Other')[:16]}</td>
                <td style="color:{C_CYAN};text-align:right;">{fmt_b(h['value_usd'])}</td>
                <td style="color:{C_GREEN};text-align:right;">{fmt_pct(h.get('pct_of_portfolio',0))}</td>
                <td style="text-align:center;">{drift}</td>
            </tr>"""

        st.markdown(f"""
        <table class="tbl">
            <thead><tr>
                <th>#</th><th>Issuer</th><th>Sector</th>
                <th style="text-align:right">Value</th>
                <th style="text-align:right">Weight</th>
                <th style="text-align:center">Drift</th>
            </tr></thead>
            <tbody>{rows}</tbody>
        </table>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col_r:
        # Sector donut
        st.markdown('<div class="card-terminal"><p class="card-title">SECTOR ALLOCATION</p>', unsafe_allow_html=True)
        sector_agg = {}
        for h in latest_holdings:
            s = h.get("sector", "Other")
            sector_agg[s] = sector_agg.get(s, 0) + h["value_usd"]
        sector_df = pd.DataFrame(
            [{"sector": k, "value": v} for k,v in sorted(sector_agg.items(), key=lambda x: -x[1])]
        )
        sector_df["color"] = sector_df["sector"].map(lambda x: SECTOR_COLORS.get(x, C_GRAY))

        fig = go.Figure(go.Pie(
            labels=sector_df["sector"],
            values=sector_df["value"],
            hole=0.5,
            marker_colors=sector_df["color"].tolist(),
            textinfo="label+percent",
            textfont=dict(size=10, family='JetBrains Mono', color='#C9D1D9'),
            hovertemplate="<b>%{label}</b><br>%{value:$.2s}<br>%{percent}<extra></extra>",
        ))
        fig.update_layout(**plotly_dark_layout(height=260))
        fig.update_layout(showlegend=False)
        st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})
        st.markdown('</div>', unsafe_allow_html=True)

        # AUM over time
        st.markdown('<div class="card-terminal"><p class="card-title">AUM OVER TIME</p>', unsafe_allow_html=True)
        aum_by_q = {}
        for h in HOLDINGS:
            aum_by_q[h["quarter"]] = aum_by_q.get(h["quarter"], 0) + h["value_usd"]
        aum_df = pd.DataFrame(
            [{"quarter": k, "aum": v} for k,v in aum_by_q.items()]
        ).sort_values("quarter")

        fig2 = go.Figure(go.Scatter(
            x=aum_df["quarter"], y=aum_df["aum"]/1e9,
            mode="lines+markers",
            line=dict(color='#58A6FF', width=1.5),
            marker=dict(color='#58A6FF', size=5),
            fill="tozeroy",
            fillcolor="rgba(88,166,255,0.08)",
            hovertemplate="%{x}<br>$%{y:.2f}B<extra></extra>",
        ))
        fig2.update_layout(**plotly_dark_layout(height=180))
        fig2.update_layout(yaxis=dict(tickformat="$.1f", ticksuffix="B"))
        st.plotly_chart(fig2, use_container_width=True, config={"displayModeBar": False})
        st.markdown('</div>', unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# TAB 2 — PORTFOLIO DRIFT
# ══════════════════════════════════════════════════════════════════════════════
with tab2:
    st.markdown('<div class="card-terminal"><p class="card-title">POSITION CHANGES · QUARTER OVER QUARTER</p>', unsafe_allow_html=True)

    quarter_options = QUARTERS[:7] if len(QUARTERS) > 1 else QUARTERS
    selected_q = st.selectbox("Quarter", quarter_options, key="drift_q",
                               label_visibility="collapsed")

    drift_holdings = sorted(
        [h for h in HOLDINGS if h["quarter"] == selected_q and h.get("drift_flag","") != "UNCHANGED"],
        key=lambda x: abs(x.get("value_change_usd", 0) or 0), reverse=True
    )

    d1, d2, d3, d4 = st.columns(4)
    for col, flag, color, label in [
        (d1, "NEW",       C_GREEN,  "New positions"),
        (d2, "INCREASED", C_CYAN,   "Increased"),
        (d3, "REDUCED",   C_AMBER,  "Reduced"),
        (d4, "EXITED",    C_RED,    "Exited"),
    ]:
        count = len([h for h in drift_holdings if h.get("drift_flag") == flag])
        with col:
            st.markdown(f"""<div class="kpi-terminal" style="border-top-color:{color};">
                <p class="kpi-label">{label}</p>
                <p class="kpi-value" style="color:{color};font-size:22px;">{count}</p>
            </div>""", unsafe_allow_html=True)

    st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)

    if drift_holdings:
        # Waterfall-style bar chart
        top_drifts = sorted(drift_holdings, key=lambda x: x.get("value_change_usd", 0) or 0)[:30]
        names  = [h["issuer_name"][:25] for h in top_drifts]
        values = [(h.get("value_change_usd", 0) or 0)/1e9 for h in top_drifts]
        colors = ["#3FB950" if v >= 0 else "#F85149" for v in values]

        fig = go.Figure(go.Bar(
            x=values, y=names, orientation="h",
            marker_color=colors,
            text=[f"${abs(v):.2f}B" for v in values],
            textposition="outside",
            textfont=dict(size=9, color='#C9D1D9'),
        ))
        fig.update_layout(**plotly_dark_layout(height=max(300, len(top_drifts)*22)))
        fig.update_layout(
            xaxis=dict(tickformat="$.1f", ticksuffix="B", title="Change in value"),
            shapes=[dict(type="line", x0=0, x1=0, y0=-0.5, y1=len(top_drifts)-0.5,
                        line=dict(color='#21262D', width=1))]
        )
        st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})
    st.markdown('</div>', unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# TAB 3 — CONCENTRATION RISK
# ══════════════════════════════════════════════════════════════════════════════
with tab3:
    col_a, col_b = st.columns(2)

    with col_a:
        st.markdown('<div class="card-terminal"><p class="card-title">CONCENTRATION OVER TIME · TOP N %</p>', unsafe_allow_html=True)

        if CONCENTRATION_DATA:
            conc_df = pd.DataFrame(CONCENTRATION_DATA).sort_values("quarter")
            fig = go.Figure()
            for label, col, color in [
                ("Top 1",  "top_1_pct",  C_RED),
                ("Top 5",  "top_5_pct",  C_AMBER),
                ("Top 10", "top_10_pct", C_CYAN),
                ("Top 20", "top_20_pct", C_GREEN),
            ]:
                if col in conc_df.columns:
                    fig.add_trace(go.Scatter(
                        x=conc_df["quarter"], y=conc_df[col],
                        name=label, mode="lines+markers",
                        line=dict(color=color, width=2),
                        marker=dict(size=5),
                        hovertemplate=f"{label}: %{{y:.1f}}%<extra></extra>",
                    ))
            fig.update_layout(**plotly_dark_layout(height=280))
            fig.update_layout(yaxis=dict(ticksuffix="%"))
            st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})
        st.markdown('</div>', unsafe_allow_html=True)

    with col_b:
        st.markdown('<div class="card-terminal"><p class="card-title">HHI CONCENTRATION INDEX</p>', unsafe_allow_html=True)

        if CONCENTRATION_DATA:
            hhi_df = pd.DataFrame(CONCENTRATION_DATA).sort_values("quarter")
            fig2 = go.Figure(go.Bar(
                x=hhi_df["quarter"], y=hhi_df.get("hhi_score", []),
                marker_color='#7C3AED',
                text=[f"{v:.0f}" for v in hhi_df.get("hhi_score", [])],
                textposition="outside",
                textfont=dict(size=9, color='#C9D1D9'),
            ))
            fig2.update_layout(**plotly_dark_layout(height=280))
            fig2.update_layout(
                yaxis=dict(title="HHI Score"),
                shapes=[
                    dict(type="line", x0=-0.5, x1=len(hhi_df)-0.5, y0=2500, y1=2500,
                         line=dict(color='#D29922', width=1, dash='dash')),
                ]
            )
            st.plotly_chart(fig2, use_container_width=True, config={"displayModeBar": False})
            st.markdown(f'<p style="font-size:10px;color:{C_GRAY};font-family:JetBrains Mono,monospace;margin:4px 0 0;">Dashed line = HHI 2500 (highly concentrated threshold)</p>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # Cumulative concentration curve — latest quarter
    st.markdown('<div class="card-terminal"><p class="card-title">CUMULATIVE WEIGHT CURVE · ' + latest_q + '</p>', unsafe_allow_html=True)
    latest_sorted = sorted(
        [h for h in HOLDINGS if h["quarter"] == latest_q],
        key=lambda x: x["value_usd"], reverse=True
    )
    if latest_sorted:
        cumulative = []
        running = 0
        for h in latest_sorted[:40]:
            running += h.get("pct_of_portfolio", 0)
            cumulative.append({"rank": h.get("holding_rank", 0), "issuer": h["issuer_name"][:20], "cumulative_pct": running})
        cum_df = pd.DataFrame(cumulative)
        fig3 = go.Figure()
        fig3.add_trace(go.Scatter(
            x=cum_df["rank"], y=cum_df["cumulative_pct"],
            mode="lines+markers",
            line=dict(color='#58A6FF', width=1.5),
            marker=dict(size=4),
            fill="tozeroy", fillcolor="rgba(88,166,255,0.07)",
            hovertemplate="Rank %{x}<br>Cumulative: %{y:.1f}%<extra></extra>",
        ))
        for pct_line in [50, 75, 90]:
            fig3.add_hline(y=pct_line, line_dash="dash", line_color='#6E7681',
                          annotation_text=f"{pct_line}%",
                          annotation_font=dict(color='#6E7681', size=9))
        fig3.update_layout(**plotly_dark_layout(height=220))
        fig3.update_layout(
            xaxis=dict(title="Holding rank"),
            yaxis=dict(ticksuffix="%"),
        )
        st.plotly_chart(fig3, use_container_width=True, config={"displayModeBar": False})
    st.markdown('</div>', unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# TAB 4 — SECTOR ROTATION
# ══════════════════════════════════════════════════════════════════════════════
with tab4:
    st.markdown('<div class="card-terminal"><p class="card-title">SECTOR ALLOCATION HEATMAP · % OF PORTFOLIO</p>', unsafe_allow_html=True)

    if SECTOR_DATA:
        sector_df = pd.DataFrame(SECTOR_DATA)
        pivot = sector_df.pivot_table(
            index="sector", columns="quarter", values="sector_pct", fill_value=0
        )
        quarters_sorted = sorted(pivot.columns)
        pivot = pivot[quarters_sorted]

        fig = go.Figure(go.Heatmap(
            z=pivot.values,
            x=pivot.columns.tolist(),
            y=pivot.index.tolist(),
            colorscale=[[0,'#0E1117'],[0.4,'rgba(88,166,255,0.3)'],[0.75,'#58A6FF'],[1.0,'#3FB950']],
            text=[[f"{v:.1f}%" for v in row] for row in pivot.values],
            texttemplate="%{text}",
            textfont=dict(size=10, family="JetBrains Mono"),
            hovertemplate="<b>%{y}</b> · %{x}<br>%{z:.1f}%<extra></extra>",
            showscale=True,
            colorbar=dict(
                tickfont=dict(color="#6B7280", size=9),
                bgcolor='#161B22',
                bordercolor='#21262D',
                ticksuffix="%",
            )
        ))
        fig.update_layout(
            **plotly_dark_layout(height=320, margin=dict(l=0,r=60,t=10,b=0))
        )
        fig.update_layout(
            xaxis=dict(side="top", tickfont=dict(size=10, color='#C9D1D9')),
            yaxis=dict(tickfont=dict(size=10, color='#C9D1D9')),
        )
        st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})
    st.markdown('</div>', unsafe_allow_html=True)

    # Sector bar chart — quarter selector
    st.markdown('<div class="card-terminal"><p class="card-title">SECTOR BREAKDOWN BY QUARTER</p>', unsafe_allow_html=True)
    sel_q2 = st.selectbox("Select quarter", QUARTERS, key="sector_q", label_visibility="collapsed")
    q_sectors = [h for h in SECTOR_DATA if h["quarter"] == sel_q2] if SECTOR_DATA else []
    if q_sectors:
        q_sec_df = pd.DataFrame(q_sectors).sort_values("sector_pct", ascending=True)
        fig4 = go.Figure(go.Bar(
            x=q_sec_df["sector_pct"], y=q_sec_df["sector"],
            orientation="h",
            marker_color=[SECTOR_COLORS.get(s, '#6E7681') for s in q_sec_df["sector"]],
            text=[f"{v:.1f}%" for v in q_sec_df["sector_pct"]],
            textposition="outside",
            textfont=dict(size=10, color="#E8E8F0"),
        ))
        fig4.update_layout(**plotly_dark_layout(height=250))
        fig4.update_layout(
            xaxis=dict(ticksuffix="%", showgrid=True),
            yaxis=dict(showgrid=False),
        )
        st.plotly_chart(fig4, use_container_width=True, config={"displayModeBar": False})
    st.markdown('</div>', unsafe_allow_html=True)
