import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta

def compound_interest_calculator():
    """Calculate compound interest with visualization"""
    st.subheader("💰 Compound Interest Calculator")
    
    col1, col2 = st.columns(2)
    
    with col1:
        principal = st.number_input("Initial Investment ($)", min_value=0.0, value=10000.0, step=100.0)
        monthly_contribution = st.number_input("Monthly Contribution ($)", min_value=0.0, value=500.0, step=50.0)
        annual_rate = st.number_input("Annual Interest Rate (%)", min_value=0.0, value=7.0, step=0.1)
        years = st.number_input("Investment Period (Years)", min_value=1, value=30, step=1)
    
    with col2:
        # Calculate compound interest
        monthly_rate = annual_rate / 100 / 12
        months = years * 12
        
        # Future value of initial investment
        fv_principal = principal * (1 + monthly_rate) ** months
        
        # Future value of monthly contributions (annuity)
        if monthly_rate > 0:
            fv_contributions = monthly_contribution * (((1 + monthly_rate) ** months - 1) / monthly_rate)
        else:
            fv_contributions = monthly_contribution * months
        
        total_future_value = fv_principal + fv_contributions
        total_contributions = principal + (monthly_contribution * months)
        total_interest = total_future_value - total_contributions
        
        st.metric("Future Value", f"${total_future_value:,.2f}")
        st.metric("Total Contributions", f"${total_contributions:,.2f}")
        st.metric("Total Interest Earned", f"${total_interest:,.2f}")
        st.metric("Return Multiple", f"{total_future_value/total_contributions:.2f}x")
    
    # Create visualization
    year_data = []
    current_value = principal
    
    for year in range(years + 1):
        year_data.append({
            'Year': year,
            'Total Value': current_value,
            'Contributions': principal + (monthly_contribution * 12 * year),
            'Interest': current_value - (principal + (monthly_contribution * 12 * year))
        })
        
        if year < years:
            # Add monthly contributions and compound for one year
            for month in range(12):
                current_value = (current_value + monthly_contribution) * (1 + monthly_rate)
    
    df = pd.DataFrame(year_data)
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['Year'], y=df['Contributions'], 
                            mode='lines', name='Total Contributions', 
                            line=dict(color='blue')))
    fig.add_trace(go.Scatter(x=df['Year'], y=df['Total Value'], 
                            mode='lines', name='Total Value', 
                            line=dict(color='green')))
    fig.add_trace(go.Scatter(x=df['Year'], y=df['Interest'], 
                            mode='lines', name='Interest Earned', 
                            line=dict(color='orange')))
    
    fig.update_layout(
        title='Investment Growth Over Time',
        xaxis_title='Years',
        yaxis_title='Amount ($)',
        hovermode='x unified'
    )
    
    st.plotly_chart(fig, use_container_width=True)

def retirement_calculator():
    """Calculate retirement needs and savings"""
    st.subheader("🏖️ Retirement Planning Calculator")
    
    col1, col2 = st.columns(2)
    
    with col1:
        current_age = st.number_input("Current Age", min_value=18, max_value=100, value=30)
        retirement_age = st.number_input("Retirement Age", min_value=50, max_value=100, value=65)
        current_income = st.number_input("Current Annual Income ($)", min_value=0.0, value=75000.0, step=1000.0)
        income_replacement = st.slider("Income Replacement in Retirement (%)", min_value=50, max_value=100, value=80)
        current_savings = st.number_input("Current Retirement Savings ($)", min_value=0.0, value=50000.0, step=1000.0)
    
    with col2:
        expected_return = st.number_input("Expected Annual Return (%)", min_value=0.0, value=7.0, step=0.1)
        inflation_rate = st.number_input("Expected Inflation Rate (%)", min_value=0.0, value=3.0, step=0.1)
        life_expectancy = st.number_input("Life Expectancy", min_value=retirement_age, max_value=120, value=90)
    
    # Calculations
    years_to_retirement = retirement_age - current_age
    years_in_retirement = life_expectancy - retirement_age
    
    # Calculate needed retirement income (adjusted for inflation)
    future_income_needed = current_income * (income_replacement / 100) * ((1 + inflation_rate / 100) ** years_to_retirement)
    
    # Calculate total retirement needs (assuming 4% withdrawal rate)
    total_retirement_needs = future_income_needed / 0.04
    
    # Future value of current savings
    future_value_current = current_savings * ((1 + expected_return / 100) ** years_to_retirement)
    
    # Additional savings needed
    additional_needed = max(0, total_retirement_needs - future_value_current)
    
    # Monthly savings required
    if expected_return > 0:
        monthly_rate = expected_return / 100 / 12
        months = years_to_retirement * 12
        if months > 0:
            monthly_savings_needed = additional_needed * monthly_rate / (((1 + monthly_rate) ** months) - 1)
        else:
            monthly_savings_needed = 0
    else:
        monthly_savings_needed = additional_needed / (years_to_retirement * 12) if years_to_retirement > 0 else 0
    
    # Display results
    st.subheader("Retirement Analysis Results")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Years to Retirement", f"{years_to_retirement}")
        st.metric("Future Income Needed", f"${future_income_needed:,.0f}/year")
    
    with col2:
        st.metric("Total Retirement Needs", f"${total_retirement_needs:,.0f}")
        st.metric("Future Value of Current Savings", f"${future_value_current:,.0f}")
    
    with col3:
        st.metric("Additional Savings Needed", f"${additional_needed:,.0f}")
        st.metric("Monthly Savings Required", f"${monthly_savings_needed:,.0f}")
    
    # Progress bar
    if total_retirement_needs > 0:
        progress = min(future_value_current / total_retirement_needs, 1.0)
        st.progress(progress)
        st.write(f"You're {progress:.1%} of the way to your retirement goal!")

def debt_payoff_calculator():
    """Calculate debt payoff strategies"""
    st.subheader("💳 Debt Payoff Calculator")
    
    # Allow user to add multiple debts
    if 'debts' not in st.session_state:
        st.session_state.debts = []
    
    with st.expander("Add New Debt", expanded=len(st.session_state.debts) == 0):
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            debt_name = st.text_input("Debt Name", placeholder="Credit Card 1")
        with col2:
            balance = st.number_input("Balance ($)", min_value=0.0, value=5000.0, step=100.0, key="debt_balance")
        with col3:
            interest_rate = st.number_input("Interest Rate (%)", min_value=0.0, value=18.0, step=0.1, key="debt_rate")
        with col4:
            min_payment = st.number_input("Minimum Payment ($)", min_value=0.0, value=100.0, step=10.0, key="debt_payment")
        
        if st.button("Add Debt"):
            if debt_name and balance > 0:
                st.session_state.debts.append({
                    'name': debt_name,
                    'balance': balance,
                    'rate': interest_rate,
                    'min_payment': min_payment
                })
                st.rerun()
    
    if st.session_state.debts:
        # Display current debts
        st.subheader("Current Debts")
        debt_df = pd.DataFrame(st.session_state.debts)
        st.dataframe(debt_df)
        
        # Clear debts button
        if st.button("Clear All Debts"):
            st.session_state.debts = []
            st.rerun()
        
        # Extra payment amount
        extra_payment = st.number_input("Extra Monthly Payment ($)", min_value=0.0, value=200.0, step=50.0)
        
        # Calculate debt avalanche (highest interest first) and snowball (smallest balance first)
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("🏔️ Debt Avalanche (Highest Interest First)")
            avalanche_debts = sorted(st.session_state.debts, key=lambda x: x['rate'], reverse=True)
            avalanche_result = calculate_payoff_strategy(avalanche_debts, extra_payment)
            
            for debt in avalanche_result['order']:
                st.write(f"**{debt['name']}**: ${debt['balance']:,.0f} at {debt['rate']:.1f}%")
            
            st.metric("Total Time to Payoff", f"{avalanche_result['months']} months")
            st.metric("Total Interest Paid", f"${avalanche_result['total_interest']:,.0f}")
        
        with col2:
            st.subheader("⛄ Debt Snowball (Smallest Balance First)")
            snowball_debts = sorted(st.session_state.debts, key=lambda x: x['balance'])
            snowball_result = calculate_payoff_strategy(snowball_debts, extra_payment)
            
            for debt in snowball_result['order']:
                st.write(f"**{debt['name']}**: ${debt['balance']:,.0f} at {debt['rate']:.1f}%")
            
            st.metric("Total Time to Payoff", f"{snowball_result['months']} months")
            st.metric("Total Interest Paid", f"${snowball_result['total_interest']:,.0f}")

def calculate_payoff_strategy(debts, extra_payment):
    """Calculate debt payoff timeline and total interest"""
    # This is a simplified calculation
    total_months = 0
    total_interest = 0
    
    for debt in debts:
        balance = debt['balance']
        monthly_rate = debt['rate'] / 100 / 12
        payment = debt['min_payment'] + (extra_payment if debt == debts[0] else 0)
        
        if monthly_rate > 0 and payment > balance * monthly_rate:
            months = -np.log(1 - (balance * monthly_rate) / payment) / np.log(1 + monthly_rate)
            interest = (payment * months) - balance
        else:
            months = balance / payment if payment > 0 else float('inf')
            interest = 0
        
        total_months = max(total_months, months)
        total_interest += interest
    
    return {
        'months': int(total_months),
        'total_interest': total_interest,
        'order': debts
    }

def emergency_fund_calculator():
    """Calculate emergency fund needs"""
    st.subheader("🚨 Emergency Fund Calculator")
    
    col1, col2 = st.columns(2)
    
    with col1:
        monthly_expenses = st.number_input("Monthly Expenses ($)", min_value=0.0, value=4000.0, step=100.0)
        months_coverage = st.slider("Months of Coverage Desired", min_value=3, max_value=12, value=6)
        current_emergency_fund = st.number_input("Current Emergency Fund ($)", min_value=0.0, value=5000.0, step=100.0)
        monthly_savings_capacity = st.number_input("Monthly Savings Capacity ($)", min_value=0.0, value=300.0, step=50.0)
    
    with col2:
        target_emergency_fund = monthly_expenses * months_coverage
        shortfall = max(0, target_emergency_fund - current_emergency_fund)
        months_to_goal = shortfall / monthly_savings_capacity if monthly_savings_capacity > 0 else float('inf')
        
        st.metric("Target Emergency Fund", f"${target_emergency_fund:,.0f}")
        st.metric("Current Emergency Fund", f"${current_emergency_fund:,.0f}")
        st.metric("Shortfall", f"${shortfall:,.0f}")
        
        if months_to_goal != float('inf'):
            st.metric("Months to Goal", f"{months_to_goal:.1f}")
        else:
            st.metric("Months to Goal", "∞")
    
    # Progress visualization
    progress = min(current_emergency_fund / target_emergency_fund, 1.0) if target_emergency_fund > 0 else 0
    st.progress(progress)
    st.write(f"Emergency Fund Progress: {progress:.1%}")

def investment_risk_calculator():
    """Calculate investment risk and return scenarios"""
    st.subheader("📊 Investment Risk Calculator")
    
    col1, col2 = st.columns(2)
    
    with col1:
        investment_amount = st.number_input("Investment Amount ($)", min_value=0.0, value=10000.0, step=500.0)
        expected_return = st.number_input("Expected Annual Return (%)", min_value=0.0, value=7.0, step=0.5)
        volatility = st.number_input("Expected Volatility (Standard Deviation %)", min_value=0.0, value=15.0, step=1.0)
        time_horizon = st.number_input("Time Horizon (Years)", min_value=1, value=10, step=1)
    
    with col2:
        # Calculate scenarios
        best_case = investment_amount * ((1 + (expected_return + volatility) / 100) ** time_horizon)
        expected_case = investment_amount * ((1 + expected_return / 100) ** time_horizon)
        worst_case = investment_amount * ((1 + max(expected_return - volatility, -50) / 100) ** time_horizon)
        
        st.metric("Best Case Scenario", f"${best_case:,.0f}")
        st.metric("Expected Case", f"${expected_case:,.0f}")
        st.metric("Worst Case Scenario", f"${worst_case:,.0f}")
        
        # Risk metrics
        potential_gain = expected_case - investment_amount
        potential_loss = investment_amount - worst_case
        
        st.metric("Potential Gain", f"${potential_gain:,.0f}")
        st.metric("Potential Loss", f"${potential_loss:,.0f}")

def render_financial_calculators():
    """Main function to render all financial calculators"""
    st.title("🧮 Financial Planning Calculators")
    
    calculator_choice = st.selectbox(
        "Choose a Calculator",
        [
            "Compound Interest Calculator",
            "Retirement Planning Calculator", 
            "Debt Payoff Calculator",
            "Emergency Fund Calculator",
            "Investment Risk Calculator"
        ]
    )
    
    st.divider()
    
    if calculator_choice == "Compound Interest Calculator":
        compound_interest_calculator()
    elif calculator_choice == "Retirement Planning Calculator":
        retirement_calculator()
    elif calculator_choice == "Debt Payoff Calculator":
        debt_payoff_calculator()
    elif calculator_choice == "Emergency Fund Calculator":
        emergency_fund_calculator()
    elif calculator_choice == "Investment Risk Calculator":
        investment_risk_calculator()