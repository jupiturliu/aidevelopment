import streamlit as st
import yfinance as yf
import pandas as pd

# Streamlit App
st.title('股票基本分析工具')

# 用户输入股票代码
ticker = st.text_input('请输入股票代码:')

if ticker:
    # 获取股票数据
    stock = yf.Ticker(ticker)
    
    # 获取基本信息
    info = stock.info
    
    st.header('公司信息')
    st.write(f"公司名称: {info.get('longName', 'N/A')}")
    st.write(f"行业: {info.get('industry', 'N/A')}")
    st.write(f"国家: {info.get('country', 'N/A')}")
    
    # 获取财务数据
    st.header('财务数据')
    try:
        financials = stock.financials
        st.write(financials.head())
    except:
        st.write("无法获取财务数据")
    
    # 获取最近股票行情
    st.header('历史股价')
    data = stock.history(period='1y')
    st.line_chart(data['Close'])
    
    # 其他一些关键指标
    st.header('关键指标')
    st.write(f"市盈率 (PE Ratio): {info.get('trailingPE', 'N/A')}")
    st.write(f"市值 (Market Cap): {info.get('marketCap', 'N/A') / 1e9:.2f} 亿美元")
    st.write(f"每股收益 (EPS): {info.get('trailingEps', 'N/A')}")
    st.write(f"股息率 (Dividend Yield): {info.get('dividendYield', 'N/A')}")