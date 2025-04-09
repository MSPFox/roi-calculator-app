import streamlit as st

# App title
st.title("HighPoint + Rewst ROI Calculator")

st.markdown("### Input Your Data Below")

# Input fields
num_employees = st.number_input("Number of employees impacted", min_value=1, value=100)
labor_cost = st.number_input("Average labor cost per hour ($)", min_value=1, value=50)
manual_hours = st.number_input("Hours spent monthly on manual workflows", min_value=0, value=300)
monthly_tickets = st.number_input("Average monthly IT tickets", min_value=0, value=100)
time_per_ticket = st.number_input("Average time per manual ticket (hours)", min_value=0.0, value=0.75, step=0.1)
downtime_cost = st.number_input("Estimated downtime cost per hour ($)", min_value=0, value=1500)
downtime_hours = st.number_input("Estimated downtime hours impacted per month", min_value=0, value=8)
monthly_investment = st.number_input("Estimated monthly investment in service ($)", min_value=0, value=5000)

# Calculations
labor_hours_saved = manual_hours + (monthly_tickets * time_per_ticket)
labor_cost_savings = labor_hours_saved * labor_cost
downtime_savings = downtime_hours * downtime_cost
total_monthly_savings = labor_cost_savings + downtime_savings
annual_savings = total_monthly_savings * 12
annual_investment = monthly_investment * 12
roi_percentage = ((annual_savings - annual_investment) / annual_investment) * 100 if annual_investment != 0 else 0
payback_period = (annual_investment / total_monthly_savings) if total_monthly_savings != 0 else 0

# Results
st.markdown("### 📊 Results")
st.write(f"**Labor Hours Saved per Month:** {labor_hours_saved:.1f} hours")
st.write(f"**Labor Cost Savings per Month:** ${labor_cost_savings:,.2f}")
st.write(f"**Downtime Savings per Month:** ${downtime_savings:,.2f}")
st.write(f"**Total Monthly Savings:** ${total_monthly_savings:,.2f}")
st.write(f"**Annualized Savings:** ${annual_savings:,.2f}")
st.write(f"**Estimated Annual Investment:** ${annual_investment:,.2f}")
st.write(f"**ROI Percentage:** {roi_percentage:.1f}%")
st.write(f"**Estimated Payback Period:** {payback_period:.1f} months")

st.markdown("---")
st.markdown("✅ Powered by HighPoint Technology Group + Rewst")
